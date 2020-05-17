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