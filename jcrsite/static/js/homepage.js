/**
 * Created by ryan on 05/05/17.
 */

$(function() {

    // use isotope to ensure cards work nicely.
    $('.card-deck').isotope({
        itemSelector: '.card',
        layoutMode: 'fitRows'
    });
});