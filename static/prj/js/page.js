const chkform = () => {
  if(!_fbProfile || !_fbProfile.id || !_fbProfile.name){
    return false
  }
  const form = $('form')[0]
  
  const fbid = document.createElement('input');
  fbid.type = "hidden";
  fbid.value = _fbProfile.id;
  fbid.name = 'fbid';

  const fbnm = document.createElement('input');
  fbnm.type = "hidden";
  fbnm.value = _fbProfile.name;
  fbnm.name = 'fbnm';

  form.appendChild(fbid);
  form.appendChild(fbnm);

  form.action = "/prj/create"
  form.method = "post"
}

const joinProject = (isLogin) => {
  console.log(isLogin)
  // ログインしていない人だった場合、ログインしてくださいポップアップを表示する
  if(!isLogin){
    if(confirm("プロジェクトに参加するためにログインしてください")){
      // OKをクリックした場合
      // TODO facebookログイン処理を呼び出す。
    }
    return
  }

  // TODO ログインしていたら、プロジェクト参加処理を実行する。
}
