const receiveData = data => {
  return data
}

const filter = () => {
  // 検索ボックスに入力された文字列を使って、プロジェクトの絞り込みを行う
  const searchWord = $('#search-box').val()
  const cards = $($('#projects-list > div.columns')[0]).children()

  if (!searchWord) {
    // 検索文字列が入力されていなかったら、すべてのカードを表示する。
    for (var i = 0; i < cards.length; i++) {
      $(cards[i]).removeClass('is-hidden')
    }
  } else {
    // 検索文字列が入力されていたら、その文字列を含むカードを表示する
    for (var i = 0; i < cards.length; i++) {
      $(cards[i]).addClass('is-hidden')
    }
    for (let dat of data) {
      for (let key in dat) {
        const str = String(dat[key])
        if (str.indexOf(searchWord) > 0) {
          // 検索文字列が含まれないプロジェクトは非表示にする
          $(`#${dat['prj_id']}`).removeClass('is-hidden')
          break
        }
      }
    }
  }

  return false
}