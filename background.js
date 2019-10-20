//http://boilerpipe-web.appspot.com/extract?url=https://www.nytimes.com/2019/10/19/world/europe/boris-johnson-brexit.html&extractor=ArticleExtractor&output=text&extractImages=&token=
//http://boilerpipe-web.appspot.com/extract?url=[url]&extractor=ArticleExtractor&output=text&extractImages=&token=


chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({color: '#3aa757'}, function() {
      //const proxyurl = "https://cors.io/?";
      async function do_stuff(){
        var request = 'http://boilerpipe-web.appspot.com/extract?url=https://www.nytimes.com/2019/10/19/world/europe/boris-johnson-brexit.html&extractor=ArticleExtractor&output=text&extractImages=&token='
        const response = await fetch(request, {mode: 'no-cors'});
        var output = await response;
        console.log(output.toString());
        console.log('test');
      }
      do_stuff();

    });
  });
