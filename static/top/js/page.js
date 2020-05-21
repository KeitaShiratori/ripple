const receiveData = data => {
  return data
}

const filter = () => {
  // 検索ボックスに入力された文字列を使って、プロジェクトの絞り込みを行う
  const searchWord = $('#search-box').val()
  if(!searchWord) return false // 検索文字列が入力されていなかったら何もしない

  const cards = $($('#projects-list > div.columns')[0]).children()
  for(var i=0; i < cards.length; i++){
    $(cards[i]).addClass('is-hidden')
  }
  for(let dat of data){
    for(let key in dat){
      const str = String(dat[key])
      if(str.indexOf(searchWord) > 0){
        // 検索文字列が含まれないプロジェクトは非表示にする
        $(`#${dat['prj_id']}`).removeClass('is-hidden')
      }
    }
  }
}