var express = require('express');
var path = require('path');
var request = require('request');
var child_process = require('child_process');
var fs = require('fs');
let {PythonShell} = require('python-shell');

var app = express();



app.set('port',process.env.PORT||8080);
app.use('/views',express.static(path.join(__dirname,"views")));
app.use('/css',express.static(path.join(__dirname,"css")));
app.use('/js',express.static(path.join(__dirname,"js")));

app.set('view engine', 'hbs');
app.get('/', function (req, res) {
  res.render('index');
})
app.get('/file', function (req, res) {
  res.render('file');
})
app.get('/text', function (req, res) {
  res.render('text');
})
app.get('/url', function (req, res) {
  res.render('url');
})
app.get('/fileupload',function(req,res){
  var file = req.query.fileupload;
  fs.readFile(file, function(err, buf) {
  console.log(buf.toString());
});
  console.log(file);
  // const filecontents = fs.readFileSync(fileupload).toString();
  // console.log(filecontents);



//  res.render('index')
})
app.get('/textupload',function(req,res){
  console.log(req.query.data)
  var articletext = req.query.data;
  let options = {
    mode: 'text',
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: path.join(__dirname, 'python'),
    args: [articletext]
  };
  PythonShell.run('py_script_01.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    //console.log('results: %j', results);
    var result_json = JSON.stringify(results);
    console.log(result_json);
    res.send(result_json); //sends output of python to client side to display urls on site
  });
})

app.get('/urlupload',function(req,res){
  var url = req.query.data;
  //console.log(req.query.data)
     request("http://boilerpipe-web.appspot.com/extract?extractor=ArticleExtractor&output=text&url="+url, function (error, response, body) {
       if (!error && response.statusCode == 200) {
         //console.log(body) // Print the google web page.
         var articletext = body;
         let options = {
           mode: 'text',
           pythonOptions: ['-u'], // get print results in real-time
           scriptPath: path.join(__dirname, 'python'),
           args: [articletext]
         };
         PythonShell.run('py_script_01.py', options, function (err, results) {
           if (err) throw err;
           // results is an array consisting of messages collected during execution
           var result_json = JSON.stringify(results);
           console.log(result_json);
           res.send(result_json); //sends output of python to client side to display urls on site
         });
       }
     })

})
var listener = app.listen(app.get('port'), function(){
  console.log('Express server started on port:'+ listener.address().port)
})
