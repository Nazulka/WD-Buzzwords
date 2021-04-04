$(document).ready(function () {
    $('.sidenav').sidenav({ edge: "right" });
    $('input#term_name, textarea#term_description').characterCounter();
});

// Slide
const slider = document.querySelector('.slider');
M.Slider.init(slider, {
    full_width: true,
    indicators: false,
    height: 400,
    transition: 500,
    interval: 6000
});


// Autocomplete
const ac = document.querySelector('.autocomplete');
M.Autocomplete.init(ac, {
    data: {
        "API": null,
        "Bootstrap": null,
        "Cache": null,
    }
});

// ScrollSpy
const ss = document.querySelectorAll('.scrollspy');
M.ScrollSpy.init(ss, {});