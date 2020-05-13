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

function statusChangeCallback(response) {
  console.log(response)
  // handle the response
  if (response.status === 'connected') {
    // Logged into your webpage and Facebook.
    _isLogin = true
    $('#for-unlogged-in').addClass('is-hidden')
    $('#for-logged-in').removeClass('is-hidden')
    _fbProfile = getFbProfile()
  } else {
    // The person is not logged into your webpage or we are unable to tell. 
    _isLogin = false
    $('#for-unlogged-in').removeClass('is-hidden')
    $('#for-logged-in').addClass('is-hidden')
  }
}

function fbLogin() {
  FB.login(function(response){
    statusChangeCallback(response);
  }, {scope: 'public_profile,email'});
}

function getFbProfile() {                      // Testing Graph API after login.  See statusChangeCallback() for when this call is made.
  console.log('Welcome!  Fetching your information.... ');
  FB.api('/me', function(response) {
    console.log('Successful login for: ' + JSON.stringify(response));
    _fbProfile = response
    $('#fb-username').text(`${response.name}さんとしてログイン中　`)
  });
}

function fbLogout(){
  FB.logout(function(response) {
    // Person is now logged out
    statusChangeCallback(response);
    // TOPに戻る
    window.location.href = '/'
 });
}
