function submitText() {
  let articleText = document.getElementById("textinput").value;
  document.getElementById("textinput").value="";
  document.getElementById("links").innerHTML = "";
  $.ajax({
         url: "textupload",                 // goes to https://user.tjhsst.edu/pckosek/submit_userpass
         type: "GET",                            // specify that this is going to be a get request
         data: {"data":articleText},      // this line uses jQuery to extract from the form a string like: username=1423&password=foobar
         success: function(response) {
             // the function we are in is called when the server responds with data
             //response should be the urls to display
             var result = JSON.parse(response);
             var div = document.getElementById("links");
             var i;
             for(var i = 0; i < result.length; i++)
             {
               var a = document.createElement('a');

                 a.setAttribute('href','https://google.com?q='+result[i])
               a.innerHTML = result[i];

               div.appendChild(a);
               div.appendChild(document.createElement('br'));
             }


             //console.log(result);
         }
     });
   }
