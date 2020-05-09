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
}