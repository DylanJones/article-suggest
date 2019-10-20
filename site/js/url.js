function submitURL() {
  let urlText = document.getElementById("urlinput").value;
   document.getElementById("urlinput").value  ="";
   document.getElementById("links").innerHTML = "";
  $.ajax({
         url: "urlupload",                 // goes to https://user.tjhsst.edu/pckosek/submit_userpass
         type: "GET",                            // specify that this is going to be a get request
         data: {"data":urlText},      // this line uses jQuery to extract from the form a string like: username=1423&password=foobar
         success: function(response) {
             // the function we are in is called when the server responds with data
             //response should be the urls to display
             var result = JSON.parse(response);
             var div = document.getElementById("links");
            for(var hyperlink of result)
            {
              var a = document.createElement('a');
              a.setAttribute('href',hyperlink);
              a.innerHTML = "Suggested Article";
              // apend the anchor to the body
              // of course you can append it almost to any other dom element
              div.appendChild(a);
              div.appendChild(document.createElement('br'));

            }//console.log(result);
         }
     });
   }
