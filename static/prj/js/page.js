const joinProject = (isLogin) => {
  console.log(isLogin)
  // ログインしていない人だった場合、ログインしてくださいポップアップを表示する
  if(!isLogin){
    $('#modal-login-for-join-project').addClass('is-active')
    return
  }

  // ログインしていたら、プロジェクト参加処理を実行する。
  joinProjectForLoggedInUser()
}

const joinProjectForLoggedInUser = () => {
  location.href = "/prj/joinProject";
}

const fbLoginForJoinProject = () => {
  $('#modal-login-for-join-project').removeClass('is-active')
  fbLogin(joinProjectForLoggedInUser)
}

$('#photo-input').on('change', event => {
  $('#thumbnail')[0].innerHTML = ""

  var file = event.target.files[0];

  var reader = new FileReader;
  reader.readAsDataURL(file);

  reader.onload = (function(theFile) {
    return function (e) {
      var div = document.createElement('div');
      div.className = 'reader_file';
      div.innerHTML += '<img class="reader_image" src="' + e.target.result + '" />';
      $('#thumbnail')[0].insertBefore(div, null);
      $('#file-name').text(theFile.name)
    }
  })(file);
})
