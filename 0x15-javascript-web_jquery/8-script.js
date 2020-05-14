$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (key, val) {
    $.getJSON(val, function (data) {
      $.each(data, function (key, val) {
        if (key === 'title') {
          $('UL#list_movies').append('<LI>' + val + '</LI');
        }
      });
    });
  });
});
