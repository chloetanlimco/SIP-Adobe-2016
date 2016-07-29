var slideIndex = 1;

window.onload = function(){
    showSlides(slideIndex);
}
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = $(".mySlides");
    var dots = $(".dot");
    if (n > slides.length) {slideIndex = 1} 
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; 
    }

    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }

    slides[slideIndex-1].style.display = "block"; 
    dots[slideIndex-1].className += " active";
}




// var i = 0;

// var myPhotos = ["images/GroupPhoto.jpg", "images/Pinterest.jpg", "images/BrickWall.jpg", "images/Mariette.jpg"];

// window.onload = function(){
//     $(".TopScroller").on('click', changePhoto);
//     console.log("clicked");
// }
// function changePhoto(element, newPath){
//     var image = $(".TopScroller").children()[0];
//     var path = myPhotos[i];
//     image.src = path;
//     i++;
//     if (i == 4){
//         i = 0;
// }
