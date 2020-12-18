var bkg= document.getElementById('good');

//getsong funtion
function loadXMLDoc() {
	var x = document.getElementById("searching").value;
  var xhttp = new XMLHttpRequest();
  var good=" ",god="";
  xhttp.open("GET", "https://rithesh.pythonanywhere.com/dashboard/song?search="+x, true);
  xhttp.send();
  xhttp.onload = () => {
  	if(xhttp.status==200){
  		var k = JSON.parse(xhttp.response)
      console.log(k);
      if(k.Result=='false'){
      god ="<h1>No Results Found For now </h1>";}
      else
      {
for (i = 0; i < k.length; i++) 
    {
  		good =`<button type='button' class='btn btn-light full' onclick='djangosong(\"${k[i].id}\")'><div class='center'><img src='${k[i].image}' alt='${k[i].title}' width=141 height=141><h1>${k[i].title}</h1><p>${k[i].description}</p></button></div><hr>`;
  	    god=god+good;
  	}
  }
  	document.getElementById("demo").innerHTML=god;
  }
}}
function playSong(kid){
 var xhttp2 = new XMLHttpRequest();
 xhttp2.open("GET", "https://codemusic.vercel.app/song?id="+kid, true);
  xhttp2.send();
  xhttp2.onload = () => {
  	if(xhttp2.status==200){
  		var s = JSON.parse(xhttp2.response)
       console.log(s)
  		document.getElementById("player").innerHTML ="";
  		document.getElementById("player").innerHTML =`<audio id='myAudio' controls ' hidden="hidden"><source src='${s.media_url}' type='audio/mpeg'>  Your browser does not support the audio tag.</audio>`;
      playss();
      bkg.style.backgroundImage = "url('"+s.image+"') !importent";
      document.getElementById("plybtn").style.display = "none";
      document.getElementById("psbtn").style.display = "initial" ;
    }
}
}
var x ; 
 function playss(){
 x = document.getElementById("myAudio");
   x.play();
  document.getElementById("plybtn").style.display = "none";
  document.getElementById("psbtn").style.display = "initial" ;
 }
  function pauseSong(){
    x = document.getElementById("myAudio");
   x.pause();
   document.getElementById("plybtn").style.display = "initial" ;
   document.getElementById("psbtn").style.display = "none";

   }

function djangosong(id)
{
  var xhttp3 = new XMLHttpRequest();
  xhttp3.open("GET", "https://rithesh.pythonanywhere.com/dashboard/api?id="+id, true);
  xhttp3.send();
  xhttp3.onload = () => {
  	if(xhttp3.status==200){
  		var h= JSON.parse(xhttp3.response)
      console.log(h);
     
      document.getElementById("player").innerHTML =`<audio id='myAudio' controls ' hidden="hidden"><source src='${h[0].fields.musicUrl}' type='audio/mpeg'>  Your browser does not support the audio tag.</audio>`;
      playss();
      bkg.style.backgroundImage = "url('"+ h[0].fields.musicIMG+"') !importent";
      document.getElementById("plybtn").style.display = "none";
      document.getElementById("psbtn").style.display = "initial" ;
      
if ("mediaSession" in navigator) {
  navigator.mediaSession.metadata = new MediaMetadata({
    title: h[0].fields.musicTitle,
    artist: h[0].fields.musicDESC,
    album: h[0].fields.musicTitle,
    artwork: [
      { src: h[0].fields.musicIMG, sizes: '500x500', type: 'image/jpg' },
    ]
  });
}}}}  // TODO: Update playback state.

//SVG colour chnging coder
