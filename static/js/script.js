$(document).ready(function () {
    $('.sidenav').sidenav({ edge: "right" });
    $('input#term_name, textarea#term_description').characterCounter();
    $('.parallax').parallax();
    $('.modal').modal();
    $('.fixed-action-btn').floatingActionButton({ hoverEnabled: false });
});

