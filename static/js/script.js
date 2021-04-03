$(document).ready(function () {
    $('.sidenav').sidenav({ edge: "right" });
    $('input#term_name, textarea#term_description').characterCounter();
});

// Slider
const slider = document.querySelector('.slider');
MSAssertion.Slider.init(slider, {
    indicators: false,
    height: 500,
    transition: 500,
    interval: 600
});

// Autocomplete
