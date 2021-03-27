 $(document).ready(function(){
    $('.sidenav').sidenav({ edge: "right" });
    $('.fixed-action-btn').floatingActionButton();
    $('input#term_name, textarea#term_description').characterCounter();
  });

  
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {
      direction: 'left'
    });
  });
    