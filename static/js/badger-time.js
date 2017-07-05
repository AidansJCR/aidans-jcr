/*
  We link to the image: http://localhost:8000/static/images/dancing-badger.gif

  This script will bless the rains (of badgers).

*/

function startRainingBadgers() {

  setInterval(function() {
    var badger = document.createElement('div');
    badger.className = 'flying-badger';
    var width = Math.floor((Math.random() * 300) + 100);
    var height = Math.floor((Math.random() * 300) + 50);
    var startLeft = Math.floor((Math.random() * screen.width));
    var img = document.createElement('img');
    img.setAttribute('width', width);
    img.setAttribute('height', height);
    img.setAttribute('src', 'localhost:8000/static/images/dancing-badger.gif');
    badger.style.top = "0px";
    badger.style.left = startLeft + "px";
    badger.appendChild(img);
    document.getElementsByTagName("body")[0].appendChild(badger);
    setTimeout(function() {
					var cheight = document.getElementsByTagName("body")[0].clientHeight;
					badger.style.top = Math.floor((Math.random() * cheight) + 200)+"px";
				},100);
  }, 1000);


}
