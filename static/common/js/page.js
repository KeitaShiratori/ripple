var _isLogin = false;
var _fbProfile = {};

(function ($) {
  $(function () {
    // facebook認証連携用コード
    window.fbAsyncInit = function() {
      FB.init({
        appId      : '249435286426550',
        cookie     : true,
        xfbml      : true,
        version    : 'v7.0'
      });
        
      FB.AppEvents.logPageView();

      // Facebookログイン状態確認
      FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
      });
    };

    // Facebookログインボタンの準備
    (function(d, s, id){
      var js, fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) {return;}
      js = d.createElement(s); js.id = id;
      js.src = "https://connect.facebook.net/en_US/sdk.js";
      fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
  
    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function() {
      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      $(".navbar-burger").toggleClass("is-active");
      $(".navbar-menu").toggleClass("is-active");
    });
  }); // end of document ready
})(jQuery); // end of jQuery name space

function checkLoginState() {
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });
}

function statusChangeCallback(response, onConnectedCallback = () => {}) {
  console.log(response)
  // handle the response
  if (response.status === 'connected') {
    // Logged into your webpage and Facebook.
    _isLogin = true
    $('.for-unlogged-in').addClass('is-hidden')
    $('.for-logged-in').removeClass('is-hidden')
    FB.api('/me', function(me) {
      $('#fb-username').text(`${me.name}さんとしてログイン中　`)
      const json = Object.assign(response, me)
      // 認証情報をサーバに連携
      $.ajax({
        type: 'POST',
        url: '/oauth',
        data: JSON.stringify(json),
        contentType: 'application/json'
      }).then(
        data => onConnectedCallback(data)
      )
    });
  }
}

function fbLogin(onConnectedCallback) {
  FB.login(function(response){
    statusChangeCallback(response, onConnectedCallback);
  }, {scope: 'public_profile,email'});
}

function fbLogout(){
  FB.logout(function(response) {
    // Person is now logged out
    _isLogin = false
    // 認証情報をサーバに連携
    $.ajax({
      type: 'POST',
      url: '/logout',
    }).then(
      data => {
        $('.for-unlogged-in').removeClass('is-hidden')
        $('.for-logged-in').addClass('is-hidden')
      }
    )
    // TOPに戻る
    window.location.href = '/'
 });
}
