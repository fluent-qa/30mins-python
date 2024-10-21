<!doctype html>
<html data-kumuhana="default">
  <head>
    <meta charset="utf-8">
    <meta name="robots" content="noindex">
    <meta name="robots" content="nofollow">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
    <link rel="apple-touch-icon" href="https://mdn.alipayobjects.com/huamei_0prmtq/afts/img/A*sRUdR543RjcAAAAAAAAAAAAADvuFAQ/original" />
    <meta http-equiv="X-UA-Compatible" content="edge">
    
    <meta name="pagetype" content="new_session">
    <meta name="pagename" content="new_session">
    <meta name="description" content="十万阿里人都在用的笔记与文档知识库，面向企业、组织或个人，提供全新的体系化知识管理，打造轻松流畅的工作协同。金融级数据安全、丰富的应用场景、强大的知识创作与管理，助力企业、个人轻松拥有云端知识库">
    <meta property="og:type" content="webpage">
    <meta property="og:url" content="https://www.yuque.com/login?goto=https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fsql%2F117735%2F1646758293092-643ef5b5-9e65-485e-a9f8-4054d52b3589.sql%3F_lake_card%3D%257B%2522src%2522%253A%2522https%253A%252F%252Fwww.yuque.com%252Fattachments%252Fyuque%252F0%252F2022%252Fsql%252F117735%252F1646758293092-643ef5b5-9e65-485e-a9f8-4054d52b3589.sql%2522%252C%2522name%2522%253A%2522district.sql%2522%252C%2522size%2522%253A301034%252C%2522ext%2522%253A%2522sql%2522%252C%2522source%2522%253A%2522transfer%2522%252C%2522status%2522%253A%2522done%2522%252C%2522download%2522%253Atrue%252C%2522type%2522%253A%2522%2522%252C%2522mode%2522%253A%2522title%2522%252C%2522id%2522%253A%2522Niql7%2522%252C%2522card%2522%253A%2522file%2522%257D">
    <meta property="og:title" content="登录 · 语雀">
    <meta property="og:description" content="十万阿里人都在用的笔记与文档知识库，面向企业、组织或个人，提供全新的体系化知识管理，打造轻松流畅的工作协同。金融级数据安全、丰富的应用场景、强大的知识创作与管理，助力企业、个人轻松拥有云端知识库">
    <meta property="og:image" content="https://mdn.alipayobjects.com/huamei_0prmtq/afts/img/A*sRUdR543RjcAAAAAAAAAAAAADvuFAQ/original">
    <title>登录 · 语雀</title>
    <link type="image/png" href="https://mdn.alipayobjects.com/huamei_0prmtq/afts/img/A*vMxOQIh4KBMAAAAAAAAAAAAADvuFAQ/original" rel="shortcut icon" />
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="语雀" />
    <link rel="manifest" href="/manifest.json" />
    <meta name="theme-color" media="(prefers-color-scheme: dark)"  content="black">
    <meta name="theme-color" media="(prefers-color-scheme: light)" content="#E7E9E8">

    <link href="https://gw.alipayobjects.com" rel="dns-prefetch" />
<link href="https://mdap.alipay.com" rel="dns-prefetch" />
<link href="https://cdn.nlark.com" rel="dns-prefetch" />
<link href="https://cdn.yuque.com" rel="dns-prefetch" />
<link href="https://kcart.alipay.com" rel="dns-prefetch" />
<link href="https://cdn-pri.nlark.com" rel="dns-prefetch" />
<link href="https://g.yuque.com" rel="dns-prefetch" />
<link href="https://mdap.yuque.com" rel="dns-prefetch" />



    
    
<link rel="stylesheet" href="https://gw.alipayobjects.com/os/chair-script/skylark/deps.19acf475.chunk.css" />
<link rel="stylesheet" href="https://gw.alipayobjects.com/os/chair-script/skylark/larkui.2ec1e1a7.chunk.css" />


    <link rel="stylesheet" href="https://gw.alipayobjects.com/os/chair-script/skylark/pc.c12a2c9f.css" />
    
    
    <meta name="renderer" content="webkit">
    <script nonce=c6Yu0EtCZPsQ1pGtauRD>
  window._macaca_runtime_collector = [];
  var MaxErrorReportLimit = 100;
  var initialPageHref = window.location.href;

  // 简单的将错误采集上报到 /api/logs/error
  window.onerror = function(message, source, lineno, colno, error) {
    // 同一个页面最多上报100次错误，防止某个循环错误页面一直打开，不断的报错
    if (MaxErrorReportLimit-- < 0) return;
    if (!message) return; // 没有 message 不上报
    if (message === 'ResizeObserver loop limit exceeded' || message === 'ResizeObserver loop completed with undelivered notifications.') return; // 无意义的 message 不上报
    if (source && source.indexOf('chrome-extension://') === 0) return; // chrome 插件注入的不上报
    try {
      var data = {
        message: message,
        source: source,
        lineno: lineno,
        colno: colno,
        stack: error && error.stack,
        traceId: window.appData && window.appData.traceId,
        href: window.location.href
      };
      // Macaca 回归使用
      window._macaca_runtime_collector.push({
        type: 'onerror',
        data: data
      });
      var content = JSON.stringify(data);
      var req = new XMLHttpRequest();
      req.open('post', '/api/logs/error', true);
      req.setRequestHeader('Content-Type', 'application/json');
      req.send(content);

      // yuyanMonitor 记录错误堆栈
      if (window.yuyanMonitor) {
        yuyanMonitor.logError(error, {
          code: 1,
          msg: message
        });
      }

      if (window.appData
        && window.appData.isYuqueMobileApp
        && initialPageHref.indexOf('/r/mobile_app/skeleton_v2') > 0
        && message !== 'Script error.'
        && message.indexOf('lakex_editor_assert_error') < 0) {

        // App 骨架屏错误埋点
        data.instanceId = window.AlipayJSBridge
          && window.AlipayJSBridge.startupParams
          && window.AlipayJSBridge.startupParams.rctInstanceId;

        NativeBridges.monitorEvent({
          eventId: 'skeleton_onerror',
          extParams: data
        });
      }
    } catch (err) {
      console.log('report error', err);
    }
  };
  window.addEventListener('unhandledrejection', function(e) {
    var data = {
      message: e.reason && e.reason.message,
      stack: e.reason && e.reason.stack,
      href: window.location.href,
      traceId: window.appData && window.appData.traceId
    };
    // Macaca 回归使用
    window._macaca_runtime_collector.push({
      type: 'unhandledrejection',
      data: data
    });
  });
</script>

  </head>
  <body>
    
    
<script nonce=c6Yu0EtCZPsQ1pGtauRD>
(function() {
  window.appData = JSON.parse(decodeURIComponent("%7B%22me%22%3A%7B%22avatar_url%22%3A%22https%3A%2F%2Fgw.alipayobjects.com%2Fzos%2Frmsportal%2FApEnVmpRbThmwJJukDlb.jpeg%22%2C%22avatar%22%3A%22https%3A%2F%2Fgw.alipayobjects.com%2Fzos%2Frmsportal%2FApEnVmpRbThmwJJukDlb.jpeg%22%2C%22language%22%3A%22zh-cn%22%2C%22is_admin%22%3Afalse%2C%22is_uirobot%22%3Afalse%7D%2C%22notification%22%3A%7B%7D%2C%22settings%22%3A%7B%22allowed_link_schema%22%3A%5B%22dingtalk%3A%22%5D%2C%22enable_link_interception%22%3Atrue%2C%22enable_new_user_public_ability_forbid%22%3Atrue%2C%22user_registry_forbidden_level%22%3A%22%22%2C%22watermark_enable%22%3A%22%22%2C%22public_space_doc_search_enable%22%3Atrue%2C%22lake_enabled_groups%22%3A%22*%22%2C%22image_proxy_root%22%3A%22%22%2C%22max_import_task_count%22%3A1%2C%22enable_search%22%3Atrue%2C%22enable_serviceworker%22%3Atrue%2C%22enable_lazyload_card%22%3A%22codeblock%22%2C%22editor_canary%22%3A%7B%22card_lazy_init%22%3A100%2C%22retryOriginImage%22%3A100%7D%2C%22enable_attachment_multipart%22%3Atrue%2C%22enable_custom_video_player%22%3Atrue%2C%22conference_gift_num%22%3A0%2C%22intranet_safe_tip%22%3A%5B%22open%22%5D%2C%22publication_enable_whitelist%22%3A%5B%5D%2C%22foreign_phone_registry_enabled_organization_whitelist%22%3A%5B%2216014876%22%2C%2216022684%22%2C%2216052442%22%2C%2218041640%22%2C%221437%22%2C%221565%22%2C%221796%22%2C%222838%22%2C%2216052442%22%2C%22309%22%2C%2222614%22%2C%221780%22%2C%226001397%22%2C%2214481%22%2C%2214040138%22%2C%2216052442%22%2C%2214043106%22%2C%2214006688%22%2C%2216033469%22%2C%2218044074%22%2C%2211321%22%2C%222008%22%2C%2235721%22%2C%226001216%22%2C%22806%22%2C%2218041640%22%2C%2218100055%22%2C%2216014876%22%2C%2216022684%22%2C%2220013926%22%2C%2221004993%22%2C%2216014876%22%2C%221780%22%2C%2216040901%22%2C%2221008258%22%2C%2222004689%22%2C%2222007115%22%2C%2216019689%22%2C%2223010%22%2C%2222614%22%2C%2214051630%22%2C%2222490268%22%5D%2C%22disable_comment_socket%22%3Atrue%2C%22disabled_login_modal_pop_default%22%3Atrue%2C%22enable_open_in_mobile_app%22%3Atrue%2C%22enable_wechat_guide_qrcode%22%3Atrue%2C%22enable_issue%22%3Atrue%2C%22enable_blank_page_detect%22%3Atrue%2C%22zone_ant_auth_keepalive_enabled_domains%22%3A%5B%5D%2C%22enable_new_group_page_whitelist%22%3A%5B%5D%2C%22enable_web_ocr%22%3A%7B%22enable%22%3Atrue%2C%22enableBrowsers%22%3A%5B%22chrome%22%5D%2C%22_users%22%3A%5B106822%5D%2C%22percent%22%3A100%7D%2C%22customer_staff_dingtalk_id%22%3A%22%22%2C%22enable_desktop_force_local%22%3Atrue%2C%22side_third_app_config%22%3A%7B%7D%2C%22desktop_check_network_status_interval%22%3A30%2C%22review_assistant_provider_url%22%3A%22%22%2C%22debug_assistant_provider_url%22%3A%22%22%2C%22codefuse_assistant_provider_url%22%3A%22%22%2C%22opsgpt_assistant_provider_url%22%3A%22%22%2C%22user_certifications_share_whitelist%22%3A%5B%22352135%22%2C%2239191355%22%2C%2295294%22%2C%2213012852%22%2C%2239187844%22%2C%2239195365%22%2C%2222303185%22%2C%2239199571%22%2C%2239200198%22%5D%2C%22user_certifications_share_scale%22%3A10%2C%22app_trusted_url_patterns%22%3A%5B%22%5Ehttps%3F%3A%5C%5C%2F%5C%5C%2F%5Ba-zA-Z0-9.-%5D%2B%5C%5C.yuque%5C%5C.com%22%2C%22%5Ehttps%3F%3A%5C%5C%2F%5C%5C%2F%5Ba-zA-Z0-9.-%5D%2B%5C%5C.nlark%5C%5C.com%22%2C%22%5Ealipays%3F%3A%5C%5C%2F%5C%5C%2F%22%5D%2C%22enable_mobile_appeal%22%3Atrue%2C%22member_buy_ad%22%3A%7B%7D%2C%22success_buy_ad%22%3A%7B%7D%2C%22doc_generator_type_blacklist%22%3A%5B%5D%2C%22all_default_captcha_enable%22%3Atrue%2C%22support_extension_download_url%22%3Atrue%2C%22support_extension_download_assembly%22%3Atrue%2C%22user_communication_group_qrcode%22%3A%22https%3A%2F%2Fmdn.alipayobjects.com%2Fhuamei_0prmtq%2Fafts%2Fimg%2FA*5CiSRraBRL0AAAAAAAAAAAAADvuFAQ%2Foriginal%22%7D%2C%22env%22%3A%22prod%22%2C%22space%22%3A%7B%22id%22%3A0%2C%22login%22%3A%22%22%2C%22name%22%3A%22%E8%AF%AD%E9%9B%80%22%2C%22short_name%22%3Anull%2C%22status%22%3A0%2C%22account_id%22%3A0%2C%22logo%22%3Anull%2C%22description%22%3A%22%22%2C%22created_at%22%3Anull%2C%22updated_at%22%3Anull%2C%22host%22%3A%22https%3A%2F%2Fwww.yuque.com%22%2C%22displayName%22%3A%22%E8%AF%AD%E9%9B%80%22%2C%22logo_url%22%3A%22https%3A%2F%2Fcdn.nlark.com%2Fyuque%2F0%2F2022%2Fpng%2F303152%2F1665994257081-avatar%2Fdcb74862-1409-4691-b9ce-8173b4f6e037.png%22%2C%22enable_password%22%3Atrue%2C%22enable_watermark%22%3Afalse%2C%22_serializer%22%3A%22web.space%22%7D%2C%22isYuque%22%3Atrue%2C%22isPublicCloud%22%3Atrue%2C%22isEnterprise%22%3Afalse%2C%22isUseAntLogin%22%3Afalse%2C%22defaultSpaceHost%22%3A%22https%3A%2F%2Fwww.yuque.com%22%2C%22timestamp%22%3A1719812598924%2C%22traceId%22%3A%220a222c7f17198125989145475155%22%2C%22siteName%22%3A%22%E8%AF%AD%E9%9B%80%22%2C%22siteTip%22%3Anull%2C%22activityTip%22%3Anull%2C%22topTip%22%3Anull%2C%22readTip%22%3A%7B%7D%2C%22questionRecommend%22%3Anull%2C%22dashboardBannerRecommend%22%3Anull%2C%22imageServiceDomains%22%3A%5B%22cdn.yuque.com%22%2C%22cdn.nlark.com%22%2C%22img.shields.io%22%2C%22travis-ci.org%22%2C%22api.travis-ci.org%22%2C%22npm.packagequality.com%22%2C%22snyk.io%22%2C%22coveralls.io%22%2C%22badgen.now.sh%22%2C%22badgen.net%22%2C%22packagephobia.now.sh%22%2C%22duing.alibaba-inc.com%22%2C%22npm.alibaba-inc.com%22%2C%22web.npm.alibaba-inc.com%22%2C%22npmjs.com%22%2C%22npmjs.org%22%2C%22npg.dockerlab.alipay.net%22%2C%22private-alipayobjects.alipay.com%22%2C%22googleusercontent.com%22%2C%22blogspot.com%22%2C%22cdn.hk01.com%22%2C%22camo.githubusercontent.com%22%2C%22gw.daily.taobaocdn.net%22%2C%22cdn-images-1.medium.com%22%2C%22medium.com%22%2C%22i.stack.imgur.com%22%2C%22imgur.com%22%2C%22doc.ucweb.local%22%2C%22lh6.googleusercontent.com%22%2C%224.bp.blogspot.com%22%2C%22bp.blogspot.com%22%2C%22blogspot.com%22%2C%221.bp.blogspot.com%22%2C%222.bp.blogspot.com%22%2C%223.bp.blogspot.com%22%2C%22aliwork-files.oss-accelerate.aliyuncs.com%22%2C%22oss-accelerate.aliyuncs.com%22%2C%22work.alibaba.net%22%2C%22work.alibaba-inc.com%22%2C%22work-file.alibaba.net%22%2C%22work-file.alibaba-inc.com%22%2C%22pre-work-file.alibaba-inc.com%22%2C%22yuque.antfin.com%22%2C%22yuque.antfin-inc.com%22%2C%22intranetproxy.alipay.com%22%2C%22lark-assets-prod-aliyun.oss-accelerate.aliyuncs.com%22%2C%22lh1.googleusercontent.com%22%2C%22lh2.googleusercontent.com%22%2C%22lh3.googleusercontent.com%22%2C%22lh4.googleusercontent.com%22%2C%22lh5.googleusercontent.com%22%2C%22lh6.googleusercontent.com%22%2C%22lh7.googleusercontent.com%22%2C%22lh8.googleusercontent.com%22%2C%22lh9.googleusercontent.com%22%2C%22raw.githubusercontent.com%22%2C%22github.com%22%2C%22en.wikipedia.org%22%2C%22rawcdn.githack.com%22%2C%22pre-work-file.alibaba-inc.com%22%2C%22alipay-rmsdeploy-image.cn-hangzhou.alipay.aliyun-inc.com%22%2C%22antsys-align-files-management.cn-hangzhou.alipay.aliyun-inc.com%22%2C%22baiyan-pre.antfin.com%22%2C%22baiyan.antfin.com%22%2C%22baiyan.dev.alipay.net%22%2C%22marketing.aliyun-inc.com%22%2C%22lark-temp.oss-cn-hangzhou.aliyuncs.com%22%2C%22www.yuque.com%22%2C%22yuque.com%22%2C%22cdn.nlark.com%22%5D%2C%22sharePlatforms%22%3A%5B%22wechat%22%2C%22dingtalk%22%5D%2C%22locale%22%3A%22zh-cn%22%2C%22customTracertConfig%22%3A%7B%22spmBPos%22%3Anull%7D%2C%22login%22%3A%7B%22loginType%22%3A%22normal%22%2C%22enablePlatforms%22%3A%5B%22dingtalk%22%2C%22alipay%22%2C%22wechat%22%2C%22teambition%22%2C%22apple%22%5D%2C%22isWechatMobileApp%22%3Afalse%2C%22platform%22%3Anull%2C%22oauthURL%22%3A%22https%3A%2F%2Foapi.dingtalk.com%2Fconnect%2Fqrconnect%3Fscope%3Dsnsapi_login%26response_type%3Dcode%26appid%3Ddingoakbgng92btxiwpydr%26redirect_uri%3Dhttps%253A%252F%252Fwww.yuque.com%252Flogin%252Foauth%252Fnull%252Fcallback%26state%3D94ce2b61-dfe0-468d-a58c-5f1f63881683%22%2C%22oauthParams%22%3A%7B%22scope%22%3A%22snsapi_login%22%2C%22response_type%22%3A%22code%22%2C%22appid%22%3A%22dingoakbgng92btxiwpydr%22%2C%22redirect_uri%22%3A%22https%3A%2F%2Fwww.yuque.com%2Flogin%2Foauth%2Fnull%2Fcallback%22%2C%22state%22%3A%2294ce2b61-dfe0-468d-a58c-5f1f63881683%22%7D%2C%22twoFAContext%22%3Anull%7D%2C%22isDesktopInValidVersion%22%3Afalse%2C%22qrCodeUrl%22%3A%22%22%2C%22paymentInfo%22%3A%7B%22paymentBizInstId%22%3A%22Z69%22%7D%2C%22interest%22%3A%7B%22interests%22%3A%7B%7D%7D%2C%22captchaAppKey%22%3A%22FFFF000000000179A3AD%22%2C%22enableCoverageDeploy%22%3Afalse%2C%22isDesktopApp%22%3Afalse%2C%22isAssistant%22%3Afalse%2C%22isAlipayApp%22%3Afalse%2C%22isDingTalkApp%22%3Afalse%2C%22isDingTalkMiniApp%22%3Afalse%2C%22isDingTalkDesktopApp%22%3Afalse%2C%22isYuqueMobileApp%22%3Afalse%2C%22tracertConfig%22%3A%7B%22spmAPos%22%3A%22a385%22%2C%22spmBPos%22%3Anull%7D%7D"));
})();
</script>


    <div id="ReactApp"></div>

    

    
    <script nonce=c6Yu0EtCZPsQ1pGtauRD>window.__webpack_nonce__ = 'c6Yu0EtCZPsQ1pGtauRD';</script>
    <script nonce=c6Yu0EtCZPsQ1pGtauRD>
      performance && performance.mark && performance.mark("start-js-render");
    </script>
    
    
    
    
    
    <style type="text/css">
  .yq-blank-detection.module-error {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 20px;
    flex-direction: column;
    text-align: center;
  }

  .yq-blank-detection.module-error h3 {
    font-size: 28px;
    font-weight: normal;
    color: #262626;
    margin-bottom: 16px;
  }

  .yq-blank-detection.module-error .error-message {
    color: #8c8c8c;
    font-size: 14px;
  }

  .yq-blank-detection.module-error .error-icon-1 {
    max-width: 45px;
    position: relative;
    left: 80px;
    top: -60px;
  }

  .yq-blank-detection.module-error .error-icon-2 {
    max-width: 54px;
    object-fit: contain;
    position: relative;
    left: -300px;
    top: 50px;
  }

  .yq-blank-detection.module-error .unknown-error {
    width: 100%;
    max-width: 1080px;
    margin-top: 50px;
  }

  .yq-blank-detection.module-error button {
    margin-top: 24px;
    color: white;
    background-color: rgb(83, 182, 114);
  }

  @media screen and (max-width: 768px) {
    .yq-blank-detection.module-error .unknown-error {
      max-width: 100%;
    }
    .yq-blank-detection.module-error .error-icon-2 {
      display: none;
    }
  }
</style>
<script nonce=c6Yu0EtCZPsQ1pGtauRD>
  (function() {
    var rootNode = document.querySelector('#ReactApp');
    var appData = window.appData || {};
    var errorMessage = '';
    var BLANK_DETECTION_RELOAD = 'blankDetectionReload';

    var isSupportLocalStorage = (function() {
      var key = '__bd_check_storage';
      try {
        if (!window.localStorage) return false;

        window.localStorage.setItem(key, '1');
        window.localStorage.removeItem(key);
      } catch (e) {
        return false;
      }
      return true;
    })();

    function renderFeedBackTips() {
      // 反馈链接
      var feedBackUrl = window.location.origin + '/feedbacks/new';
      if (appData.traceId) {
        feedBackUrl += '?body=反馈信息：' + appData.traceId;
      }
      var isDesktopApp = window.appData.isDesktopApp;
      var feedback = window.appData.traceId ? '反馈信息：' + window.appData.traceId : '';
      var htmlList;
      if (isDesktopApp) {
        htmlList = [
          '<div id="yq-blank-detection" class="module-error yq-blank-detection">',
          '<div class="error-message">',
          '<h3>页面出错了</h3>',
          '<p>',
          '遇到一些未知错误，请尝试刷新页面、清除浏览器缓存或截图<a target="_blank" href="' + feedBackUrl + '">反馈</a>给我们',
          '</p>',
          '<p>' + feedback + '</p>',
          '<button class="ant-btn" id="yq-blank-detection-reload-button">重启客户端</button>'
        ];
      } else {
        htmlList = [
          '<div id="yq-blank-detection" class="module-error yq-blank-detection">',
          '<img class="error-icon-1" src="https://gw.alipayobjects.com/mdn/prod_resou/afts/img/A*lACSTZ9k73wAAAAAAAAAAAAAARQnAQ" />',
          '<img class="error-icon-2" src="https://gw.alipayobjects.com/mdn/prod_resou/afts/img/A*gVB8RJQlsQsAAAAAAAAAAAAAARQnAQ" />',
          '<div class="error-message">',
          '<h3>页面出错了</h3>',
          '<p>',
          '遇到一些未知错误，请尝试刷新页面、清除浏览器缓存或截图<a target="_blank" href="' + feedBackUrl + '">反馈</a>给我们',
          '</p>',
          '<p>' + feedback + '</p>',
          '</div>',
          '<div>',
          '<img class="unknown-error" src="https://gw.alipayobjects.com/mdn/prod_resou/afts/img/A*au01Tr2-h8oAAAAAAAAAAAAAARQnAQ" />',
          '</div>',
          '</div>'
        ];
      }
      rootNode.innerHTML = htmlList.join('');
      var reloadBtn = document.getElementById('yq-blank-detection-reload-button');
      if (reloadBtn) {
        reloadBtn.onclick = function() {
          if (window.YuqueDesktopJSBridge) {
            window.YuqueDesktopJSBridge.postMessage('app.relaunch');
          } else {
            window.location.reload();
          }
        };
      }
    }

    function reportToYuYan() {
      if (!window.yuyanMonitor) return;
      var fromClient = window.appData.isYuqueMobileApp ? 'yuqueMobileApp' : 'default';
      var traceId = window.appData.traceId || '';
      window.yuyanMonitor.logError(new Error('Page is blank!'), {
        code: 45,
        msg: 'web_page_blank_error',
        d1: fromClient,
        d2: traceId,
        d3: errorMessage
      });
    }

    function unregisterServiceWorker() {
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker
          .getRegistrations()
          .then(function(registrations) {
            registrations.forEach(function(sw) {
              sw.unregister();
            });
        });
      }
    }

    function report() {
      try {
        // 清理掉 localStorage
        if (isSupportLocalStorage) {
          window.localStorage.removeItem(BLANK_DETECTION_RELOAD);
        }

        // 清理掉 serviceWorker
        unregisterServiceWorker();
        // 展示反馈
        renderFeedBackTips();
        // 上报雨燕
        reportToYuYan();
      } catch (e) {
        console.error(e);
      }
    }

    function checkRootNode() {
      if (rootNode && rootNode.innerHTML && rootNode.innerHTML !== '<div></div>') {
        return true;
      }
      return false;
    }

    function reload() {
      // 清理掉 serviceWorker
      unregisterServiceWorker();
      // 主动刷新一次
      window.localStorage.setItem(BLANK_DETECTION_RELOAD, true);
      if (window.localStorage.getItem(BLANK_DETECTION_RELOAD)) {
        window.location.reload(true);
      } else {
        report();
      }
    }

    function checkAndReport() {
      // 插入节点前再次检查是否白屏
      if (checkRootNode()) {
        if (isSupportLocalStorage) {
          window.localStorage.removeItem(BLANK_DETECTION_RELOAD);
        }
        return;
      }
      // 是否重新加载
      if (isSupportLocalStorage && !window.localStorage.getItem(BLANK_DETECTION_RELOAD)) {
        reload();
      } else {
        report();
      }
    }

    function onloadHandler() {
      if (checkRootNode()) {
        if (isSupportLocalStorage) {
          window.localStorage.removeItem(BLANK_DETECTION_RELOAD);
        }
        return;
      } else {
        // 10s 后检测白屏
        setTimeout(function() {
          errorMessage = 'INNERHTML_NOT_EXIST';
          checkAndReport();
        }, 10 * 1000);
      }
    }

    window.addEventListener('error', function(event) {
      if (event) {
        // 5s 后检测白屏
        setTimeout(function() {
          errorMessage = event.message;
          checkAndReport();
        }, 5 * 1000);
      }
    }, false);

    window.addEventListener('load', onloadHandler, false);
  })();
</script>

    
    <script nonce=c6Yu0EtCZPsQ1pGtauRD>
  if ('serviceWorker' in navigator && navigator.serviceWorker) {
    if (!/[?&]enable_sw=false/.test(location.search)
      && window.appData
      && !window.appData.isYuqueMobileApp
      && window.appData.settings
      && window.appData.settings.enable_serviceworker
      && window.appData.me
      && window.appData.me.id) {
      if (typeof navigator.serviceWorker.register === 'function') {
        window.addEventListener('load', function() {
          navigator.serviceWorker.register('/serviceworker.js').catch(function(err) {
            console.error("service worker register error " + err.message);
          });
        });
      }
    } else {
      if (typeof navigator.serviceWorker.getRegistrations === 'function') {
        navigator.serviceWorker.getRegistrations().then(function (registrations) {
          registrations.forEach(function (sw) {
            sw.unregister();
          });
        });
      }
    }
  }
</script>

    <script crossorigin
  src="https://gw.alipayobjects.com/render/p/yuyan_npm/@alipay_yuyan-monitor-web/4.1.14/dist/index.umd.min.js"></script>
<script nonce=c6Yu0EtCZPsQ1pGtauRD>
  if (window.YuyanMonitor) {
    window.yuyanMonitor = new YuyanMonitor({
      _appId: '589c123e2b89c03d127000da',
    
  env: '外网',
    
  
  userId: '',
    plugins: ['performance']
  });
}
</script>

    <!-- 雨燕前置错误捕获逻辑 -->
    <script nonce=c6Yu0EtCZPsQ1pGtauRD>
      !function(){var e=window;function n(n){if(e.g_monitor&&e.g_monitor.events){var t=e.g_monitor.events;t.length<20&&t.push(n)}}e.g_monitor=e.g_monitor||{listener:{},events:[]};
      var r=e.g_monitor.listener;function t(t,n){try{e.addEventListener?e.addEventListener(t,n,!0):e.attachEvent?e.attachEvent("on"+t,n):e[t]=n,r[t]=n}catch(n){console.warn("Tracert 监控事件注册失败："+t,n)}}r.error||t("error",n),r.unhandledrejection||t("unhandledrejection",n)}();
    </script>
    <script crossorigin src="https://b.alicdn.com/s/polyfill.min.js?features=default,es2015,es2016,es2017,fetch,IntersectionObserver,NodeList.prototype.forEach,NodeList.prototype.@@iterator,EventSource,MutationObserver,ResizeObserver,HTMLCanvasElement.prototype.toBlob,Promise.prototype.finally,Object.values|always"></script>
<script crossorigin src="https://gw.alipayobjects.com/os/lib/??react/16.13.1/umd/react.production.min.js,react-dom/16.13.1/umd/react-dom.production.min.js,react-dom/16.13.1/umd/react-dom-server.browser.production.min.js,moment/2.24.0/min/moment.min.js"></script>


<script nonce=c6Yu0EtCZPsQ1pGtauRD>
window.globalThis = window.globalThis || window;
if (!Object.fromEntries) {
  Object.defineProperty(Object, 'fromEntries', {
    value(entries) {
      if (!entries || !entries[Symbol.iterator]) { throw new Error('Object.fromEntries() requires a single iterable argument'); }

      var o = {};

      Object.keys(entries).forEach(function(key){
        var [k, v] = entries[key];

        o[k] = v;
      });

      return o;
    },
  });
}
if (!Object.entries) {
  Object.entries = function( obj ){
    var ownProps = Object.keys( obj ),
        i = ownProps.length,
        resArray = new Array(i); // preallocate the Array
    while (i--)
      resArray[i] = [ownProps[i], obj[ownProps[i]]];
    
    return resArray;
  };
}
</script>



    <!-- 通过开关结合当前请求的 url 对应路由的配置信息，来决定是否发送 preload_appData.js -->
    

    
    
    
    <script nonce=c6Yu0EtCZPsQ1pGtauRD>
      window.routerBase = '/';
      window.resourceBaseUrl = 'https://gw.alipayobjects.com/os/chair-script/skylark/';
    </script>
    
    

    
<script nonce=c6Yu0EtCZPsQ1pGtauRD>window.__webpack_public_path__ = '/os/chair-script/skylark/';</script><script crossorigin src="https://gw.alipayobjects.com/os/chair-script/skylark/deps.22e8c456.async.js"></script>
<script crossorigin src="https://gw.alipayobjects.com/os/chair-script/skylark/common.8ae1eac9.async.js"></script>
<script crossorigin src="https://gw.alipayobjects.com/os/chair-script/skylark/larkui.6590650d.async.js"></script>



    <script crossorigin src="https://gw.alipayobjects.com/os/chair-script/skylark/pc.74e6a049.js"></script>
    
      
      <script nonce=c6Yu0EtCZPsQ1pGtauRD>
        // 加载九色鹿埋点脚本
        window.addEventListener('load', function() {
          !function(t,e,a,r,c){t.TracertCmdCache=t.TracertCmdCache||[],t[c]=window[c]||
            {_isRenderInit:!0,call:function(){t.TracertCmdCache.push(arguments)},
            start:function(t){this.call('start',t)}},t[c].l=new Date;
            var n=e.createElement(a),s=e.getElementsByTagName(a)[0];
            n.async=!0,n.src=r,s.parentNode.insertBefore(n,s)}

          
          (window,document,'script','https://ur.alipay.com/tracert_a385.js','Tracert');
          Tracert.start({
            spmAPos: 'a385',
            spmBPos: '',
            
            role_id: '',
            mdata: {
              
              
              
              
            },
          });

          
          
        });
      </script>
      
      
    
    

    

    
    
    
  </body>
</html>
