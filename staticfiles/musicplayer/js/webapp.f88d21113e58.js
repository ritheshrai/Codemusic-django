
var len=0,cursong=0;
var isPlaying = false;
let songarray=["none"]
var x= document.getElementById("audio");
//getsong funtion
function loadXMLDoc() {
	var x = document.getElementById("searching").value;
  var xhttp = new XMLHttpRequest();
  var good=" ",god="";
 // xhttp.open("GET", "https://codemusic-django.herokuapp.com/dashboard/song?search="+x, true);
 
 if(Boolean(x)){
  //xhttp.open("GET", "https://codemusic-django.herokuapp.com/dashboard/song?search="+x, true);
  xhttp.open("GET", "http://127.0.0.1:8000/dashboard/song?search="+x, true);
  xhttp.send();
  xhttp.onload = () => {
  	if(xhttp.status==200){
  		var k = JSON.parse(xhttp.response)
      console.log(k);
      if(k.Result=='false'){
      god ="<h1>No Results Found For now </h1>";}
      else
      { god="<div class='grid'>"
        len=k.length;
for (i = 0; i < len; i++) 
    {
  		good =`<button type='button' class='btn btn-light full' onclick='djangosong(\"${k[i].id}\")'><div><img src='${k[i].image}' alt='${k[i].title}' width=141 height=141><h1>${k[i].title}</h1><p>${k[i].description}</p></div></button>`;
  	  god=god+good;
      songarray[i]=k[i].id
  	}
  }
  	document.getElementById("demo").innerHTML=god+"</div>";
  }
}}}
console.log(songarray)
function playSong(kid){
 var xhttp2 = new XMLHttpRequest();
 xhttp2.open("GET", "https://codemusic.vercel.app/song?id="+kid, true);
 xhttp2.send();
 xhttp2.onload = () => {
  	if(xhttp2.status==200){
  		var s = JSON.parse(xhttp2.response)
       console.log(s)
  		
       x.src=s.media_url;
  		//document.getElementById("player").innerHTML =`<audio id='myAudio' controls ' hidden="hidden"><source src='${s.media_url}' type='audio/mpeg'>  Your browser does not support the audio tag.</audio>`;
      playss();
      
      // document.getElementById("plybtn").style.display = "none";
      // document.getElementById("psbtn").style.display = "initial" ;
    }
}}


 function playss(){
// x = document.getElementById("myAudio");
   x.play();
   isPlaying=true;
  // document.getElementById("plybtn").style.display = "none";
  // document.getElementById("psbtn").style.display = "initial" ;
 }
  function pauseSong(){
    x = document.getElementById("myAudio");
   x.pause();
   isPlaying=false;
   // document.getElementById("plybtn").style.display = "initial" ;
   // document.getElementById("psbtn").style.display = "none";

   }
var h;
function djangosong(id)
{ 
  cursong=songarray.indexOf(id);
  var xhttp3 = new XMLHttpRequest();
   //xhttp3.open("GET", "https://codemusic-django.herokuapp.com/dashboard/api?id="+id, true);
   xhttp3.open("GET", "http://127.0.0.1:8000/dashboard/api?id="+id, true);
 xhttp3.send();
  xhttp3.onload = () => {
  	if(xhttp3.status==200){
  		 h= JSON.parse(xhttp3.response)
      console.log(h);
      x.src=h[0].fields.musicUrl;

     // document.getElementById("posterimg").crossOrigin = 'Anonymous';
      document.getElementById("posterimg").src=h[0].fields.musicIMG;
      document.getElementById("songinfo").innerHTML="<h1>"+h[0].fields.musicTitle+"</h1><p>"+h[0].fields.musicDESC+"</p>";
      //<audio id='myAudio'  ' hidden="hidden"><source src='${h[0].fields.musicUrl}' type='audio/mpeg'>  Your browser does not support the audio tag.</audio>`;
      playss();
      //document.querySelector(".codeplay").style.backgroundImage = 'url("https://source.unsplash.com/1600x900/?music,peace")';
      //document.querySelector(".codeplay").style.backgroundImage = "url('"+ h[0].fields.musicIMG+"') ";
      document.querySelector(".body").style.backgroundImage = "url('"+ h[0].fields.musicIMG+"') ";
     // document.getElementById("plybtn").style.display = "none";
      //document.getElementById("psbtn").style.display = "initial" ;




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
//fressing enter calls search
document.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    loadXMLDoc();
  }
});
//player
