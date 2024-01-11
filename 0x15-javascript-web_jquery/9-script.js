const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function (data, status) {
  $('div#hello').append(data.hello);
});
