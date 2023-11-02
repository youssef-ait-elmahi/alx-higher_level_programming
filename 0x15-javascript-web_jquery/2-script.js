/* global $ */
// Use jQuery to add a click event to the div with id 'red_header'
$('#red_header').click(function () {
  // When the div is clicked, change the color of the header
  $('header').css('color', '#FF0000');
});
