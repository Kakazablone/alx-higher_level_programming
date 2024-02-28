$(document).ready(function() {
  $('#btn_translate').click(function() {
      var languageCode = $('#language_code').val();
      $.ajax({
          url: 'https://www.fourtonfish.com/hellosalut/hello/',
          type: 'GET',
          dataType: 'json',
          data: { lang: languageCode },
          success: function(response) {
              $('#hello').text(response.hello);
          },
      });
  });
});
//CORS seems to be preventing data retrieval
