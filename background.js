//http://boilerpipe-web.appspot.com/extract?url=https://www.nytimes.com/2019/10/19/world/europe/boris-johnson-brexit.html&extractor=ArticleExtractor&output=text&extractImages=&token=
//http://boilerpipe-web.appspot.com/extract?url=[url]&extractor=ArticleExtractor&output=text&extractImages=&token=


chrome.runtime.onInstalled.addListener(function() {
  chrome.storage.sync.set({color: '#3aa757'}, function() {
    //const proxyurl = "https://cors.io/?";
    async function do_stuff(){
      var request = 'http://boilerpipe-web.appspot.com/extract?url=https://www.nytimes.com/2019/10/19/world/europe/boris-johnson-brexit.html&extractor=ArticleExtractor&output=text&extractImages=&token='
      //  const response = await fetch(request, {mode: 'no-cors'});
      //  var output = response;
      fetch(request, {mode: 'no-cors'})
      .then((resp) => resp.text())
      .then(function(data) {
        download(data, "test.txt");
        console.log(data);
        console.log('test');
        })
      }
      do_stuff();
    })
  });

function download(data, filename) {
  var file = new Blob([data]);
  if (window.navigator.msSaveOrOpenBlob) // IE10+
  window.navigator.msSaveOrOpenBlob(file, filename);
  else { // Others
    var a = document.createElement("a"),
    url = URL.createObjectURL(file);
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    setTimeout(function() {
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
    }, 0);
  }
}
