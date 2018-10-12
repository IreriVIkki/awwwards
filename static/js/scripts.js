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
    $('.site-img').hover(function () {
        // over
        $('.site-fade').addClass('site-fade-in');
        $('.site-fade').removeClass('site-fade-out');
    }, function () {
        // out
        $('.site-fade').removeClass('site-fade-in');
        $('.site-fade').addClass('site-fade-out');
    });
});

// function getid(obj) {
//     alert(obj.id)
//     return obj.id
// }

// function outmouse(obj) {
//     alert(obj.id)
//     return obj.id
// }