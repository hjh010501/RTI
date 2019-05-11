let pagestatus = "Dashboard";

let widthsize = parseInt($('body').css('width').replace("px",""))

$(document).ready(function() {
    $('.Status').css('transform', 'translateX(' + widthsize + 'px)');
    $('.Logs').css('transform', 'translateX(' + widthsize + 'px)');
});

var toDashboard = () => {

    let widthsize = parseInt($('body').css('width').replace("px",""))
    $('.Logsbutton').css('pointer-events','none');
    $('.Dashboardbutton').css('pointer-events','none');
    $('.Statusbutton').css('pointer-events','none');
    
    anime({
        targets: '.'+pagestatus,
        translateX: widthsize,
        duration: 1500,
        easing: 'easeInOutCubic',
        autoplay: true,
        complete: function(anim) {
            $('.'+pagestatus).css('display', 'none');
            $('.Dashboard').css('position', 'block');
            $('.Statusbutton').css('pointer-events','all');
            $('.Logsbutton').css('pointer-events','all');
            pagestatus = "Dashboard";
        }
    });
    
    anime({
        targets: '.Dashboard',
        translateX: 0,
        duration: 1500,
        easing: 'easeInOutCubic',
        autoplay: true,
        begin: function(anim) {
            $('.'+pagestatus).css('position', 'absolute');
            $('.Dashboard').css({'display': 'block', 'position': 'absolute'});
        },
    })

}

var toStatus = () => {

    let widthsize = parseInt($('body').css('width').replace("px",""))
    $('.Logsbutton').css('pointer-events','none');
    $('.Dashboardbutton').css('pointer-events','none');
    $('.Statusbutton').css('pointer-events','none');

    anime({
        targets: '.'+pagestatus,
        translateX: pagestatus=="Dashboard" ? -widthsize : widthsize,
        duration: 1500,
        easing: 'easeInOutCubic',
        autoplay: true,
        complete: function(anim) {
            $('.'+pagestatus).css('display', 'none');
            $('.Status').css('position', 'block');
            $('.Dashboardbutton').css('pointer-events','all');
            $('.Logsbutton').css('pointer-events','all');
            pagestatus = "Status";
        }
    });

    anime({
        targets: '.Status',
        translateX: 0,
        duration: 1500,
        easing: 'easeInOutCubic',
        autoplay: true,
        begin: function(anim) {
            $('.'+pagestatus).css('position', 'absolute');
            $('.Status').css({'display': 'block', 'position': 'absolute'});
          },
    });

}


var toLogs = () => {

    let widthsize = parseInt($('body').css('width').replace("px",""))

    $('.Logsbutton').css('pointer-events','none');
    $('.Dashboardbutton').css('pointer-events','none');
    $('.Statusbutton').css('pointer-events','none');
    anime({
        targets: '.'+pagestatus,
        translateX: -widthsize,
        duration: 1500,
        easing: 'easeInOutCubic',
        autoplay: true,
        complete: function(anim) {
            $('.'+pagestatus).css('display', 'none');
            $('.Logs').css('position', 'block');
            $('.Dashboardbutton').css('pointer-events','all');
            $('.Statusbutton').css('pointer-events','all');
            pagestatus = "Logs";
        }
    });

    anime({
        targets: '.Logs',
        translateX: 0,
        duration: 1500,
        easing: 'easeInOutCubic',
        autoplay: true,
        begin: function(anim) {
            $('.'+pagestatus).css('position', 'absolute');
            $('.Logs').css({'display': 'block', 'position': 'absolute'});
          },
    });

}

