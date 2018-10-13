$(document).ready(function () {

    // hover over landing page
    $('.landing').hover(function () {
        // over
        $('.landing-abs-fade').addClass('dark-fade');
        $('.landing-abs-fade').removeClass('light-fade');
    }, function () {
        // out
        $('.landing-abs-fade').addClass('light-fade');
        $('.landing-abs-fade').removeClass('dark-fade');
    });

    // hover over individual website box
});

function getid(fadeId) {
    // over
    let fade = '#fade' + fadeId
    $(fade).addClass('site-fade-in');
    $(fade).removeClass('site-fade-out');
}

function outmouse(fadeId) {
    // out
    let fade = '#fade' + fadeId
    $(fade).removeClass('site-fade-in');
    $(fade).addClass('site-fade-out');
};