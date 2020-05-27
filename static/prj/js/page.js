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
  $('#thumbnail').innerHTML = ""

  var file = event.target.file;

  var reader = new FileReader;
  reader.readAsDataURL(file);

  reader.onload = (function(theFile) {
    return function (e) {
      var div = document.createElement('div');
      div.className = 'reader_file';
      div.innerHTML = '<div class="reader_title">' + encodeURIComponent(theFile.name) + '</div>';
      div.innerHTML += '<img class="reader_image" src="' + e.target.result + '" />';
      $('#thumbnail').insertBefore(div, null);
      $('#file-name').innerHTML = encodeURIComponent(theFile.name)
    }
  })(file);
})
