// Scroll Button
window.onscroll = function() { scrollFunction() };

function scrollFunction() {
    let button = document.getElementById("topBtn");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
}

// Scroll to the top when the button is clicked
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: "smooth" });
}

// Testimonial slider
let index = 0;
const wrapper = document.querySelector('.testimonial-wrapper');
const dots = document.querySelectorAll('.dot');

function showSlide(n) {
    index = n;
    wrapper.style.transform = `translateX(-${index * 100}%)`;
    dots.forEach(dot => dot.classList.remove('active'));
    dots[n].classList.add('active');
}

function nextSlide() {
    index++;
    if (index > 4) { index = 0; }
    showSlide(index);
}

function currentSlide(n) {
    index = n;
    showSlide(index);
}

setInterval(nextSlide, 3000); // Move every 3 seconds

// Maps picture
function initMap() {
    var location = { lat: 31.5204, lng: 74.3587 }; // Example (Lahore, Pakistan)
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: location
    });
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
}
// Show and hide sidebar
const bar = document.getElementById('bar');
const close = document.getElementById('close');
const  nav = document.querySelector('.navbar');

if (bar){
    bar.addEventListener('click',()=>{
        nav.classList.add('active');
    })
}
if (close){
    close.addEventListener('click',()=>{
        nav.classList.remove('active');
    })
}
// hero section animate text

const smart = document.querySelector('.smart');

function Smart(){
    smart.style.animation = 'typing 3s steps(20)'; //it run only one time
    setTimeout( ()=>{
        smart.style.animation = 'none';
        setTimeout( ()=>{ // it reapeated time of animation again and again
            Smart();

        },3000);

    },5000); //it will pause the animation for some seconds
}
setTimeout(Smart,500);// it is the starting time of animation on reload page


