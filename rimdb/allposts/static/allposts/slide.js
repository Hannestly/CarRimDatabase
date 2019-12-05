//<div class="downloads">
  //  <h2> Past Deliverables </h2>
  //  <a id="p1doc" href="Phase1.pdf" download> Phase One </a>
    //<a id="p2doc" href="Phase2.pdf" download> Phase Two </a>
//</div>

var i = 0;
var imgs = [];
var time = 3000;

imgs[0] = 'slide2.jpg';
imgs[1] = 'slide3.jpg';


function change() {
  document.slides.src = imgs[i];


  if( i < imgs.length -1){
    i++;
  } else {
    i = 0;
  }

  setTimeout("change()",time)
}

window.onload = change;
