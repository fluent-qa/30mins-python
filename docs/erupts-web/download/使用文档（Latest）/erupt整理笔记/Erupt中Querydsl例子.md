# Erupt中Querydsl例子


# Erupt中Querydsl例子

> 作者: 白石([https://github.com/wjw465150](https://github.com/wjw465150))



## 内连接(省市区联动的例子)

- 表的DDL:

```sql
CREATE TABLE `test_district` (
  `id` bigint(20) NOT NULL COMMENT '主键自增',
  `pid` bigint(20) DEFAULT NULL COMMENT '父类id',
  `district_name` varchar(255) DEFAULT NULL COMMENT '城市的名字',
  `type` bigint(20) DEFAULT NULL COMMENT '城市的类型，0是国，1是省，2是市，3是区',
  `hierarchy` bigint(20) DEFAULT NULL COMMENT '地区所处的层级',
  `district_sqe` varchar(255) DEFAULT NULL COMMENT '层级序列',
  PRIMARY KEY (`id`),
  KEY `FKdlvfu74qyf5v8n2krft9vbcjn` (`pid`),
  CONSTRAINT `FKdlvfu74qyf5v8n2krft9vbcjn` FOREIGN KEY (`pid`) REFERENCES `test_district` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```

- 实体类:

```java
package org.wjw.mt.entity.district;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import org.hibernate.annotations.GenericGenerator;

import xyz.erupt.annotation.Erupt;
import xyz.erupt.annotation.EruptField;
import xyz.erupt.annotation.sub_field.View;

/**
 * @description test_district
 * @author WS
 * @date 2021-04-28
 */
@Erupt(name = "地区表")
@Entity
@Table(name = "test_district")
public class District implements Serializable {
  private static final long serialVersionUID = 1L;

  /**
   * 主键自增
   */
  @Id
  /*@wjw_comment: 自己控制主键生成
  @GeneratedValue(generator = "generator")
  @GenericGenerator(name = "generator",
                    strategy = "native")
  */                  
  @Column(name = "id")
  @EruptField
  private Long id;

  /**
   * 父类id
   */
  @ManyToOne
  @JoinColumn(name = "pid")
  private District pid;

  /**
   * 城市的名字
   */
  @EruptField(views = @View(title = "名称"))
  @Column(name = "district_name")
  private String districtName;

  /**
   * 城市的类型，0是国，1是省，2是市，3是区
   */
  @Column(name = "type",columnDefinition="bigint(20)")
  private Integer type;

  /**
   * 地区所处的层级
   */
  @EruptField(views = @View(title = "层级"))
  @Column(name = "hierarchy",columnDefinition="bigint(20)")
  private Integer hierarchy;

  /**
   * 层级序列
   */
  @Column(name = "district_sqe")
  private String districtSqe;

  public District() {
  }

  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }

  public District getPid() {
    return pid;
  }

  public void setPid(District pid) {
    this.pid = pid;
  }

  public String getDistrictName() {
    return districtName;
  }

  public void setDistrictName(String districtName) {
    this.districtName = districtName;
  }

  public Integer getType() {
    return type;
  }

  public void setType(Integer type) {
    this.type = type;
  }

  public Integer getHierarchy() {
    return hierarchy;
  }

  public void setHierarchy(Integer hierarchy) {
    this.hierarchy = hierarchy;
  }

  public String getDistrictSqe() {
    return districtSqe;
  }

  public void setDistrictSqe(String districtSqe) {
    this.districtSqe = districtSqe;
  }

  @Override
  public String toString() {
    // @formatter:off
    return "TestDistrict [id=" + id + ", pid=" + pid + ", districtName=" + districtName 
           + ", type=" + type + ", hierarchy=" + hierarchy + ", districtSqe=" + districtSqe + "]";
    // @formatter:on
  }

}
```

- 设计的内连接的SQL语句:

```sql
    select * 
    from 
      test_district as sheng,
      test_district as shi
    where sheng.id=shi.pid 
      and sheng.district_name='河南'
```

- Querydsl实现的代码:

```java
  @Test
  public void testSelfJoin() {
    QDistrict sheng = new QDistrict("sheng");
    QDistrict shi = new QDistrict("shi");
    
    System.out.println("----------------------------------------------");
    jpaQueryFactory
    .select(sheng.id,sheng.pid.id,sheng.districtName,sheng.type,sheng.hierarchy,sheng.districtSqe,
            shi.id,shi.pid.id,shi.districtName,shi.type,shi.hierarchy,shi.districtSqe)
    .from(sheng).from(shi)
    .where(sheng.id.eq(shi.pid.id).and(sheng.districtName.eq("河南")))
    .fetch()
    .stream()
    .forEach(tuple -> {
      System.out.println(tuple);
    });
    System.out.println("----------------------------------------------");
  }
```

- Querydsl生成的JPQL:

```sql
  select
      sheng.id,
      sheng.pid.id,
      sheng.districtName,
      sheng.type,
      sheng.hierarchy,
      sheng.districtSqe,
      shi.id,
      shi.pid.id,
      shi.districtName,
      shi.type,
      shi.hierarchy,
      shi.districtSqe 
  from
      District sheng,
      District shi 
  where
      sheng.id = shi.pid.id 
      and sheng.districtName = ?1
```

- JPA通过JPQL生成的Native SQL:

```sql
  select
          district0_.id as col_0_0_,
          district0_.pid as col_1_0_,
          district0_.district_name as col_2_0_,
          district0_.type as col_3_0_,
          district0_.hierarchy as col_4_0_,
          district0_.district_sqe as col_5_0_,
          district1_.id as col_6_0_,
          district1_.pid as col_7_0_,
          district1_.district_name as col_8_0_,
          district1_.type as col_9_0_,
          district1_.hierarchy as col_10_0_,
          district1_.district_sqe as col_11_0_ 
      from
          test_district district0_  
      cross join
          test_district district1_ 
      where
          district0_.id=district1_.pid 
          and district0_.district_name=?
```

输出的结果:

```
-----------------------------------------------------------
[11, 1, 河南, 1, 2, .1.11., 149, 11, 郑州, 2, 3, .1.11.149.]
[11, 1, 河南, 1, 2, .1.11., 150, 11, 洛阳, 2, 3, .1.11.150.]
[11, 1, 河南, 1, 2, .1.11., 151, 11, 开封, 2, 3, .1.11.151.]
[11, 1, 河南, 1, 2, .1.11., 152, 11, 安阳, 2, 3, .1.11.152.]
[11, 1, 河南, 1, 2, .1.11., 153, 11, 鹤壁, 2, 3, .1.11.153.]
[11, 1, 河南, 1, 2, .1.11., 154, 11, 济源, 2, 3, .1.11.154.]
[11, 1, 河南, 1, 2, .1.11., 155, 11, 焦作, 2, 3, .1.11.155.]
[11, 1, 河南, 1, 2, .1.11., 156, 11, 南阳, 2, 3, .1.11.156.]
[11, 1, 河南, 1, 2, .1.11., 157, 11, 平顶山, 2, 3, .1.11.157.]
[11, 1, 河南, 1, 2, .1.11., 158, 11, 三门峡, 2, 3, .1.11.158.]
[11, 1, 河南, 1, 2, .1.11., 159, 11, 商丘, 2, 3, .1.11.159.]
[11, 1, 河南, 1, 2, .1.11., 160, 11, 新乡, 2, 3, .1.11.160.]
[11, 1, 河南, 1, 2, .1.11., 161, 11, 信阳, 2, 3, .1.11.161.]
[11, 1, 河南, 1, 2, .1.11., 162, 11, 许昌, 2, 3, .1.11.162.]
[11, 1, 河南, 1, 2, .1.11., 163, 11, 周口, 2, 3, .1.11.163.]
[11, 1, 河南, 1, 2, .1.11., 164, 11, 驻马店, 2, 3, .1.11.164.]
[11, 1, 河南, 1, 2, .1.11., 165, 11, 漯河, 2, 3, .1.11.165.]
[11, 1, 河南, 1, 2, .1.11., 166, 11, 濮阳, 2, 3, .1.11.166.]
-----------------------------------------------------------
```


## 懒加载问题解决

如果一对多或者多对多中的关系是懒加载的,可是使用`.join(关系Q对象).fetchJoin()`的方式来解决

```java
  @Test
  public void testB() {
    List<EruptUser> qEruptUser = jpaQueryFactory.select(QEruptUser.eruptUser)
        .from(QEruptUser.eruptUser)
        .join(QEruptUser.eruptUser.roles).fetchJoin()
        .where(QEruptUser.eruptUser.name.eq("test"))
        .fetch();
    for (EruptUser user : qEruptUser) {
      Set<EruptRole> roles = user.getRoles();
      System.out.println(roles);
      System.out.println(user);
    }
  }
```

- Querydsl生成的JPQL:

```sql
select
        eruptUser 
    from
        EruptUser eruptUser   
    inner join
        fetch eruptUser.roles 
    where
        eruptUser.name = ?1
```

- JPA通过JPQL生成的Native SQL:

```sql
select
            eruptuser0_.id as id1_33_0_,
            eruptrole2_.id as id1_31_1_,
            eruptuser0_.create_time as create_t2_33_0_,
            eruptuser0_.create_user_id as create_14_33_0_,
            eruptuser0_.update_time as update_t3_33_0_,
            eruptuser0_.update_user_id as update_15_33_0_,
            eruptuser0_.account as account4_33_0_,
            eruptuser0_.email as email5_33_0_,
            eruptuser0_.erupt_menu_id as erupt_m16_33_0_,
            eruptuser0_.erupt_org_id as erupt_o17_33_0_,
            eruptuser0_.erupt_post_id as erupt_p18_33_0_,
            eruptuser0_.is_admin as is_admin6_33_0_,
            eruptuser0_.is_md5 as is_md7_33_0_,
            eruptuser0_.name as name8_33_0_,
            eruptuser0_.password as password9_33_0_,
            eruptuser0_.phone as phone10_33_0_,
            eruptuser0_.remark as remark11_33_0_,
            eruptuser0_.status as status12_33_0_,
            eruptuser0_.white_ip as white_i13_33_0_,
            eruptrole2_.code as code2_31_1_,
            eruptrole2_.name as name3_31_1_,
            eruptrole2_.power_off as power_of4_31_1_,
            eruptrole2_.status as status5_31_1_,
            roles1_.user_id as user_id2_34_0__,
            roles1_.role_id as role_id1_34_0__ 
        from
            e_upms_user eruptuser0_ 
        inner join
            e_upms_user_role roles1_ 
                on eruptuser0_.id=roles1_.user_id 
        inner join
            e_upms_role eruptrole2_ 
                on roles1_.role_id=eruptrole2_.id 
        where
            eruptuser0_.name=?
```


## 子查询(JPAExpressions)

要创建子查询，您可以使用`JPAExpressions` 的静态工厂方法并通过 `from` 、`where`  等定义查询参数。

```java
  /*
   * 要创建子查询，您可以使用`JPAExpressions` 的静态工厂方法并通过 `from` 、`where` 等定义查询参数。
   */
  @Test
  public void testJPAExpressions1() {
    QDistrict district = QDistrict.district;
    QDistrict d        = new QDistrict("d");

    jpaQueryFactory.selectFrom(district)
        .where(district.hierarchy.in(
            JPAExpressions.select(d.hierarchy).from(d).where(d.hierarchy.eq(2))))
        .fetch()
        .stream()
        .forEach(it -> {
          System.out.println(it);
        });
  }
```

- Querydsl生成的JPQL:

```sql
select
        district 
    from
        District district 
    where
        district.hierarchy in (
            select
                d.hierarchy 
            from
                District d 
            where
                d.hierarchy = ?1
```

- JPA通过JPQL生成的Native SQL:

```sql
 select
            district0_.id as id1_43_,
            district0_.district_name as district2_43_,
            district0_.district_sqe as district3_43_,
            district0_.hierarchy as hierarch4_43_,
            district0_.pid as pid6_43_,
            district0_.type as type5_43_ 
        from
            test_district district0_ 
        where
            district0_.hierarchy in (
                select
                    district1_.hierarchy 
                from
                    test_district district1_ 
                where
                    district1_.hierarchy=?
```

输出的结果:

```
TestDistrict [id=2, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=北京, type=1, hierarchy=2, districtSqe=.1.2.]
TestDistrict [id=3, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=安徽, type=1, hierarchy=2, districtSqe=.1.3.]
TestDistrict [id=4, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=福建, type=1, hierarchy=2, districtSqe=.1.4.]
TestDistrict [id=5, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=甘肃, type=1, hierarchy=2, districtSqe=.1.5.]
TestDistrict [id=6, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=广东, type=1, hierarchy=2, districtSqe=.1.6.]
TestDistrict [id=7, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=广西, type=1, hierarchy=2, districtSqe=.1.7.]
TestDistrict [id=8, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=贵州, type=1, hierarchy=2, districtSqe=.1.8.]
TestDistrict [id=9, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=海南, type=1, hierarchy=2, districtSqe=.1.9.]
TestDistrict [id=10, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=河北, type=1, hierarchy=2, districtSqe=.1.10.]
TestDistrict [id=11, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=河南, type=1, hierarchy=2, districtSqe=.1.11.]
TestDistrict [id=12, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=黑龙江, type=1, hierarchy=2, districtSqe=.1.12.]
TestDistrict [id=13, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=湖北, type=1, hierarchy=2, districtSqe=.1.13.]
TestDistrict [id=14, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=湖南, type=1, hierarchy=2, districtSqe=.1.14.]
TestDistrict [id=15, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=吉林, type=1, hierarchy=2, districtSqe=.1.15.]
TestDistrict [id=16, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=江苏, type=1, hierarchy=2, districtSqe=.1.16.]
TestDistrict [id=17, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=江西, type=1, hierarchy=2, districtSqe=.1.17.]
TestDistrict [id=18, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=辽宁, type=1, hierarchy=2, districtSqe=.1.18.]
TestDistrict [id=19, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=内蒙古, type=1, hierarchy=2, districtSqe=.1.19.]
TestDistrict [id=20, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=宁夏, type=1, hierarchy=2, districtSqe=.1.20.]
TestDistrict [id=21, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=青海, type=1, hierarchy=2, districtSqe=.1.21.]
TestDistrict [id=22, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=山东, type=1, hierarchy=2, districtSqe=.1.22.]
TestDistrict [id=23, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=山西, type=1, hierarchy=2, districtSqe=.1.23.]
TestDistrict [id=24, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=陕西, type=1, hierarchy=2, districtSqe=.1.24.]
TestDistrict [id=25, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=上海, type=1, hierarchy=2, districtSqe=.1.25.]
TestDistrict [id=26, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=四川, type=1, hierarchy=2, districtSqe=.1.26.]
TestDistrict [id=27, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=天津, type=1, hierarchy=2, districtSqe=.1.27.]
TestDistrict [id=28, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=西藏, type=1, hierarchy=2, districtSqe=.1.28.]
TestDistrict [id=29, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=新疆, type=1, hierarchy=2, districtSqe=.1.29.]
TestDistrict [id=30, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=云南, type=1, hierarchy=2, districtSqe=.1.30.]
TestDistrict [id=31, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=浙江, type=1, hierarchy=2, districtSqe=.1.31.]
TestDistrict [id=32, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=重庆, type=1, hierarchy=2, districtSqe=.1.32.]
TestDistrict [id=33, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=香港, type=1, hierarchy=2, districtSqe=.1.33.]
TestDistrict [id=34, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=澳门, type=1, hierarchy=2, districtSqe=.1.34.]
TestDistrict [id=35, pid=TestDistrict [id=1, pid=null, districtName=中国, type=0, hierarchy=1, districtSqe=.1.], districtName=台湾, type=1, hierarchy=2, districtSqe=.1.35.]
```


## 动态添加where条件(BooleanBuilder)

如果有条件就会拼接上where语句,没有就不会有where子句;不需要像以前的解决方案那样先拼凑一个 `where 1=1` :

```java
 @Test
  public void testBooleanBuilder2() {
    JPAQuery<MtCity> query = jpaQueryFactory.selectFrom(QMtCity.mtCity);

    BooleanBuilder builder = new BooleanBuilder();

    builder.or(QMtCity.mtCity.name.eq("北京"));
    builder.or(QMtCity.mtCity.name.eq("上海"));
    builder.or(QMtCity.mtCity.name.eq("广州"));

    query.where(builder);

    query.limit(5).fetch().stream().forEach(mtCity -> {
      System.out.println(mtCity);
    });
  }
```

- Querydsl生成的JPQL:

```sql
select
        mtCity 
    from
        MtCity mtCity 
    where
        mtCity.name = ?1 
        or mtCity.name = ?2 
        or mtCity.name = ?3
```

- JPA通过HPQL生成的Native SQL:

```sql
select
            mtcity0_.id as id1_35_,
            mtcity0_.acronym as acronym2_35_,
            mtcity0_.firstchar as firstcha3_35_,
            mtcity0_.name as name4_35_,
            mtcity0_.pinyin as pinyin5_35_,
            mtcity0_.rank as rank6_35_,
            '一个URL链接,会被DataProxy的afterFetch来赋值'  as formula1_ 
        from
            mt_city mtcity0_ 
        where
            mtcity0_.name=? 
            or mtcity0_.name=? 
            or mtcity0_.name=? limit ?
```


## CASE 表达式

要构造 case-when-then-else 表达式，使用`CaseBuilder`类，如下所示：

```java
  /*
   * 要构造 case-when-then-else 表达式，请使用`CaseBuilder`类
   */
  @Test
  public void testCaseBuilder2() {
    QDistrict district = QDistrict.district;
    
    StringExpression casex = new CaseBuilder()
        .when(district.type.eq(0)).then("国家")
        .when(district.type.eq(1)).then("省份")
        .when(district.type.eq(2)).then("市")
        .otherwise("区县");
    
    jpaQueryFactory.select(district.districtName,district.type,casex)
    .from(district)
    .orderBy(casex.asc())
    .limit(5)
    .fetch()
    .stream()
    .forEach(it -> {
      System.out.println(it);
    });
  }
```

- Querydsl生成的JPQL:

```sql
select
        district.districtName,
        district.type,
        case 
            when (district.type = ?1) then ?2 
            when (district.type = ?3) then ?4 
            when (district.type = ?5) then ?6 
            else '区县' 
        end 
    from
        District district 
    order by
        case 
            when (district.type = ?1) then ?2 
            when (district.type = ?3) then ?4 
            when (district.type = ?5) then ?6 
            else '区县' 
        end asc
```

- JPA通过JPQL生成的Native SQL:

```sql
select
            district0_.district_name as col_0_0_,
            district0_.type as col_1_0_,
            case 
                when district0_.type=? then ? 
                when district0_.type=? then ? 
                when district0_.type=? then ? 
                else '区县' 
            end as col_2_0_ 
        from
            test_district district0_ 
        order by
            case 
                when district0_.type=? then ? 
                when district0_.type=? then ? 
                when district0_.type=? then ? 
                else '区县' 
            end asc limit ?
```


## 转换成JPA的Query

如果你需要在执行查询之前调整原始查询(javax.persistence.Query)，你可以像这样暴露它:

```java
  /*
   * 暴露JPA的Query.如果你需要在执行查询之前调整原始JPA Query，你可以像这样暴露它:
   */
  @Test
  public void testJavaxPersistenceQuery() {
    javax.persistence.Query jpaQuery = jpaQueryFactory.selectFrom(QDistrict.district).limit(5).createQuery();
    @SuppressWarnings("unchecked")
    List<District> ll = (List<District>) jpaQuery.getResultList();
    
    ll.stream()
    .forEach(it -> {
      System.out.println(it);
    });
  }
```


## SQL里常用的`ALL` `ANY` 表达式

想要使用ALL,ANY运算符,使用`ExpressionUtils`工具类里的方法才行!

```java
  @Test
  public void testAllExpression() {
    QDistrict district = new QDistrict("e");
    
    QDistrict d = new QDistrict("d");
    
    List<District> list = jpaQueryFactory.selectFrom(district).where(district.hierarchy.lt(
        ExpressionUtils.all(
            JPAExpressions.select(d.hierarchy).from(d).groupBy(d.hierarchy).having(d.hierarchy.gt(2))
            )
        )).fetch();
    
    for (District p : list) {
      printResult(p);
    }
  }
```

- Querydsl生成的JPQL:

```sql
   select
        e 
    from
        District e 
    where
        e.hierarchy < all (
            select
                d.hierarchy 
            from
                District d 
            group by
                d.hierarchy 
            having
                d.hierarchy > ?1
        )
```

- JPA通过JPQL生成的Native SQL:

```sql
select
            district0_.id as id1_43_,
            district0_.district_name as district2_43_,
            district0_.district_sqe as district3_43_,
            district0_.hierarchy as hierarch4_43_,
            district0_.pid as pid6_43_,
            district0_.type as type5_43_ 
        from
            test_district district0_ 
        where
            district0_.hierarchy<all (
                select
                    district1_.hierarchy 
                from
                    test_district district1_ 
                group by
                    district1_.hierarchy 
                having
                    district1_.hierarchy>?
            )
```


## SQL里常用的转换函数

使用`Expressions.stringTemplate`方法来创建`StringExpression` .字符串里的变量用`{0},{1},...{n}`占位符.

`com.querydsl.core.types.dsl.Expressions` 类是一个用于动态表达式构造的静态工厂类。 工厂方法由返回的类型命名，并且大多是自文档的。

一般来说，`Expressions` 类应该只在不能使用流畅的 DSL 形式的情况下使用，例如动态路径、自定义语法或自定义操作。

```java
@Test
  public void testStringTemplate() {
    QEruptOperateLog eruptOperateLog = QEruptOperateLog.eruptOperateLog;

    final StringExpression createdMonthYear = Expressions.stringTemplate("DATE_FORMAT({0},'%Y-%m-%d %H')",eruptOperateLog.createTime);
    
    jpaQueryFactory.select(eruptOperateLog.apiName,eruptOperateLog.createTime,createdMonthYear,eruptOperateLog.reqAddr)
    .from(eruptOperateLog)
    .limit(5)
    .fetch()
    .stream()
    .forEach((Tuple district) -> {
      System.out.println(district);
    });
  }
```

- Querydsl生成的JPQL:

```sql
select
        eruptOperateLog.apiName,
        eruptOperateLog.createTime,
        DATE_FORMAT(eruptOperateLog.createTime,'%Y-%m-%d %H'),
        eruptOperateLog.reqAddr 
    from
        EruptOperateLog eruptOperateLog
```

- JPA通过JPQL生成的Native SQL:

```sql
select
            eruptopera0_.api_name as col_0_0_,
            eruptopera0_.create_time as col_1_0_,
            date_format(eruptopera0_.create_time,'%Y-%m-%d %H') as col_2_0_,
            eruptopera0_.req_addr as col_3_0_ 
        from
            e_upms_operate_log eruptopera0_ limit ?
```


> 原文: <https://www.yuque.com/erupt/bfqb5g>