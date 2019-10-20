function submitText() {
  let articleText = document.getElementById("textinput").value;
  document.getElementById("textinput").value="";

  $.ajax({
         url: "textupload",                 // goes to https://user.tjhsst.edu/pckosek/submit_userpass
         type: "GET",                            // specify that this is going to be a get request
         data: {"data":articleText},      // this line uses jQuery to extract from the form a string like: username=1423&password=foobar
         success: function(response) {
             // the function we are in is called when the server responds with data
             //response should be the urls to display
             console.log(response);
         }
     });
   }
function submitURL() {
  let urlText = document.getElementById("urlinput").value;
   document.getElementById("urlinput").value  ="";
  $.ajax({
         url: "urlupload",                 // goes to https://user.tjhsst.edu/pckosek/submit_userpass
         type: "GET",                            // specify that this is going to be a get request
         data: {"data":urlText},      // this line uses jQuery to extract from the form a string like: username=1423&password=foobar
         success: function(response) {
             // the function we are in is called when the server responds with data
             //response should be the urls to display
             console.log(response);
         }
     });
   }
