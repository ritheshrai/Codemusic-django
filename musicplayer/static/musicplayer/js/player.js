$('audio').mediaelementplayer({
	features: ['playpause','progress','current','tracks','fullscreen']
});
var voluume = document.getElementById("myRange");
 voluume.oninput = function() {
  var audio=document.getElementById("audio");
 //audio.volume=1.0;
}

