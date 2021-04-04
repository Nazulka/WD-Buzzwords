$(document).ready(function () {
    $('.sidenav').sidenav({ edge: "right" });
    $('input#term_name, textarea#term_description').characterCounter();
    $('.parallax').parallax({ full_width: true });
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