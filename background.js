var partNum = 30;

var canvas = document.getElementById('c');
var ctx = canvas.getContext('2d');

var w = window.innerWidth; var h = window.innerHeight;
var x = 100; var y = 100;

var particles = [];
for(i = 0; i < partNum; i++) {
  particles.push(new newParticle);
}

function newParticle() {
  this.x = w / 2;
  this.y = h / 2;
  
  this.vx = Math.random() * 20-10;
  this.vy = Math.random() * 20-10;
  
  this.r = Math.random() * 15;
  
  var r = '#c0392b';
  var o = '#e67e22';
  var y = '#f1c40f';
  var array = [r, o, y];
	this.color = array[Math.floor(Math.random() * 3)];
  
  this.g = 0.3; 
}

var draw = function() {
  
  c.width = w;
  c.height = h;
  
  for(t = 0; t < particles.length; t++) {
    var p = particles[t];
    
    ctx.beginPath();
  	ctx.fillStyle = p.color;
  	ctx.arc(p.x, p.y, p.r, Math.PI * 2, false);
  	ctx.fill();
    
    p.x+=p.vx;
    p.y+=p.vy+=p.g;
    
    if(p.y < 0)
      p.vy *= -1;
    if(p.y > h)
      p.vy *= -1;
    if(p.y > h + 1)
      p.y = h;
    if(p.x < 0)
      p.vx *= -1;
    if(p.x > w)
      p.vx *= -1;
    if(p.r < 3) {
      p.color = 'white';
    };
  }
};

setInterval(draw, 33);
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

$("p").each(function() {
  var text = $(this).html();
  var words = text.split(" ");
  var spanSentence = "";
  for (var i = 0; i < words.length; i++) {
    spanSentence += "<span>" + words[i] + "</span> ";
  }
  $(this).html(spanSentence);
})

$("p span").each(function() {
  $(this)
    .css({
      "transform": "translate(" + getRandomInt(-100, 100) + "px, " + getRandomInt(-100, 100) + "px)"
    })
});
setTimeout(function() {

  $("p:nth-child(1) span").css({
    "transform": "translate(0, 0)",
    "opacity": 1
  });
}, 50);

setTimeout(function() {

  $("p:nth-child(2) span").css({
    "transform": "translate(0, 0)",
    "opacity": 1
  });
}, 1000+50);

setTimeout(function() {

  $("p:nth-child(3) span").css({
    "transform": "translate(0, 0)",
    "opacity": 1
  });
}, 2000+50);

setTimeout(function() {

  $("p:nth-child(4) span").css({
    "transform": "translate(0, 0)",
    "opacity": 1
  });
}, 3000+50);

setTimeout(function() {

  $("p:nth-child(5) span").css({
    "transform": "translate(0, 0)",
    "opacity": 1
  });
}, 4000+50);
setTimeout(function() {

  $("p:nth-child(6) span").css({
    "transform": "translate(0, 0)",
    "opacity": 1
  });
}, 5000+50);
setTimeout(function() {

  $("p:nth-child(7) span").css({
    "transform": "translate(0, 0)",
    "opacity": 1
  });
}, 6000+50);
setTimeout(function() {

  $("p:nth-child(8) span").css({
    "transform": "translate(0, 0)",
    "opacity": 1
  });
}, 8000+50);