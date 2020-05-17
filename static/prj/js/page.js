const chkform = () => {
  if(!_fbProfile || !_fbProfile.id || !_fbProfile.name){
    return false
  }
  document.prj_create_form.user_id = _fbProfile.id
  document.prj_create_form.user_name = _fbProfile.name
  document.prj_create_form.action = "/prj/create"
  document.prj_create_form.method = "post"
}