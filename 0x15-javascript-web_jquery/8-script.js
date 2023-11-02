/* global $ */
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    data.results.forEach(function (film) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  });
});
