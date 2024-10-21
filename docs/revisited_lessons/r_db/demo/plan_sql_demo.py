from sqlalchemy import text, insert
from sqlmodel import Session, SQLModel, select

from revisited_lessons.r_db.setup import engine, DemoHero, User


def exec_sql(sql_text: text):
    with engine.connect() as conn:
        print("execute sql:", str(sql_text))
        result = conn.execute(sql_text)
        conn.commit()
        return result


def select_plain_sql():
    conn = engine.connect()
    sql = text("select * from demo_hero")
    result = conn.execute(
        sql
    )
    print(result.fetchall())
    conn.commit()
    conn.close()


def insert_statement():
    statement = insert(User)
    print(statement.compile(compile_kwargs={"literal_binds": True}))
    with engine.begin() as conn:
        conn.execute(
            insert(User),
            [
                {"name": "sandy", "fullname": "Sandy Cheeks"},
                {"name": "gary", "fullname": "Gary the Snail"},
            ],
        )


def with_sql_model_session(statement):
    with Session(engine) as session:
        return session.execute(statement).fetchall()


def with_sql_model_session_save(o: SQLModel):
    with Session(engine) as session:
        session.add(o)
        session.commit()
        return result


if __name__ == '__main__':
    sql_text = text("""
    insert into demo_hero (name, age) values ('test',18);
    """)
    exec_sql(sql_text)
    select_plain_sql()
    result = with_sql_model_session(select(DemoHero).where(DemoHero.name == 'test'))
    hero = result[0]
    print(hero)
    with_sql_model_session_save(DemoHero(name='save-it', age=120))
    insert_statement()
