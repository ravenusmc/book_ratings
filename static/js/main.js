//This file will contain all of the Javascript for the book ratings project. 

//Ajax call for book look up form
$(document).ready(function(){
  $('#book_look_up_form').bind('submit', function(event){
    event.preventDefault();
    $.ajax({
      data: {
        title: $('#title').val()
      },
      type: 'POST',
      url: '/book_look_up',
      success: function(data){
        $('#result').text(data.result).show();
      }
    });
  });
});