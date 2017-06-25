/**
 * This is some basic JS code to work with my bunting CSS to create bunting :D
 * Created by ryan on 25/06/17.
 */
jQuery(document).ready(function() {
    var resizeBunting = function() {
    console.log("Resize");
    var windowWidth = $('.bunting').width();
    $('.bunting').empty();

    // first, let's draw the string that we fasten flags to
    var string = $('<div>');
    string.addClass('string');
    $('.bunting').append(string);
    // now go through rendering flags
    var sliding = 0;
    var odd = true;
    for(sliding = -5; sliding < windowWidth - 10; sliding += 200) {
      // add another flag, with alternative colour
      var newFlag = $('<div>');
      newFlag.addClass('arrow-down');
      // alternate colours
      if(odd) {
        newFlag.addClass('red');
        odd = false;
      } else {
        //even
        newFlag.addClass('green');
        odd = true;
      }

      // now add the flag
      $('.bunting').append(newFlag);
  }
    };

  $(window).on('resize', function() {
    resizeBunting();
  });
  resizeBunting();
});