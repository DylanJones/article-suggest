var express = require('express');
var path = require('path');
var request = require('request');
var child_process = require('child_process')

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
  console.log(req.query.fileupload);
  res.render('index')
})
app.get('/textupload',function(req,res){
  console.log(req.query.data)
  // var articletext = req.query.data;
  // // the python executable. Can be a path to a venv
  // python_exe = 'python3';
  //
  // // the python file
  // pythonFile = path.join(__dirname, 'python', 'py_script_01.py');
  //
  // //produce json data for python input
  // jsonData = JSON.stringify(articletext);
  // feed_dict = { input: jsonData };
  //
  // // spawn the (python) child process
  // py = child_process.spawnSync(python_exe, [pythonFile], feed_dict );
  //
  // // extract the result of the python operation
  // py_response = py['stdout'].toString();
  // console.log(py_response);
  // // send the result back to the user
  // res.send(py_response);

})
app.get('/urlupload',function(req,res){
  var url = req.query.data;
  var article = "";
  console.log(req.query.data)


     request("http://boilerpipe-web.appspot.com/extract?extractor=ArticleExtractor&output=text&url="+url, function (error, response, body) {
       if (!error && response.statusCode == 200) {
         console.log(body) // Print the google web page.
         article = body
       }
     })



})
var listener = app.listen(app.get('port'), function(){
  console.log('Express server started on port:'+ listener.address().port)
})
