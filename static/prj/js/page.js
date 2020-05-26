const joinProject = (isLogin) => {
  console.log(isLogin)
  // ログインしていない人だった場合、ログインしてくださいポップアップを表示する
  if(!isLogin){
    $('#modal-login-for-join-project').addClass('is-active')
    return
  }

  // TODO ログインしていたら、プロジェクト参加処理を実行する。
  joinProjectForLoggedInUser()
}

const joinProjectForLoggedInUser = () => {
  location.href = "/prj/joinProject";
}

const fbLoginForJoinProject = () => {
  $('#modal-login-for-join-project').removeClass('is-active')
  fbLogin(joinProjectForLoggedInUser)
}
