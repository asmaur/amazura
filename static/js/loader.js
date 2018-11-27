

$(document).ready(function() {
    //Preloader
    $(window).on("load", function() {
    preloaderFadeOutTime = 500;
    function hidePreloader() {
    var preloader = $('#page-loader');
    preloader.fadeOut(preloaderFadeOutTime);
    }
    hidePreloader();
    });
});

