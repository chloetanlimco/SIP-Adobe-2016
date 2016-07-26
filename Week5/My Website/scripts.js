var myPhotos = ["images/GroupPhoto.jpg", "images/Pinterest.jpg"]
// , "images/BrickWall.jpg", "images/Mariette.jpg"

window.onload = function(){
    $(".TopScroller").on('click', changePhoto);
    console.log("clicked")
}

function changePhoto(element, newPath){
    // var image = $(".TopScroller").children()[0];
    // var path = "images/Pinterest.jpg"
    // image.src = path;

    if (image.src == myPhotos[0]){
        var path = myPhotos[1];
        image.src = path;
    }
    // if (image.src == myPhotos[1]){
    //     var path = myPhotos[2];
    //     image.src = path;
    // }
    // if (image.src == myPhotos[2]){
    //     var path = myPhotos[3];
    //     image.src = path;
    // }
    // if (image.src == myPhotos[3]){
    //     var path = myPhotos[0];
    //     image.src = path;
    // }
}
