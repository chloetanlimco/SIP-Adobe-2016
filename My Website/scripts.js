
var i = 0;

var myPhotos = ["images/GroupPhoto.jpg", "images/Pinterest.jpg", "images/BrickWall.jpg", "images/Mariette.jpg"];

window.onload = function(){
    $(".TopScroller").on('click', changePhoto);
    console.log("clicked");
    $(".TitleText").style.visibility = "hidden";
}

function changePhoto(element, newPath){
    var image = $(".TopScroller").children()[0];
 
    var path = myPhotos[i];
    image.src = path;
    i++;
    if (i == 4){
        i = 0;
    }
}
