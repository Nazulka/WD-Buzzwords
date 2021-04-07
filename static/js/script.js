$(document).ready(function () {
    $('.sidenav').sidenav({ edge: "right" });
    $('input#term_name, textarea#term_description').characterCounter();
     $('.parallax').parallax();
     $('.modal').modal();
});

// Autocomplete
const ac = document.querySelector('.autocomplete');
M.Autocomplete.init(ac, {
    data: {
        "API": null,
        "Bootstrap": null,
        "Cache": null,
    },
    limit: 5
});

