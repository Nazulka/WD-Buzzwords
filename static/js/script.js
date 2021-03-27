 $(document).ready(function(){
    $('.sidenav').sidenav({ edge: "right" });
    $('.fixed-action-btn').floatingActionButton();
    $('input#input_text, textarea#textarea1').characterCounter();
  });

  
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {
      direction: 'left'
    });
  });
    