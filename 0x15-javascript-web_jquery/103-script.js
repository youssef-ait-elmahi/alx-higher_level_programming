$(document).ready(function(){
    function translate() {
      let lang = $('#language_code').val();
      $.get('https://www.fourtonfish.com/hellosalut/hello/' + lang, function(data){
        $('#hello').text(data.hello);
      });
    }
    $('#btn_translate').click(translate);
    $('#language_code').keypress(function(e){
      if(e.which == 13) {
        translate();
      }
    });
  });
  