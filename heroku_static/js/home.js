$(function() {
    $('#explain').hover(
        function() {
            $('#explain_c').fadeIn();
        },
        function() {
            $('#explain_c').hide();
        }
    );
});
var menu1 = 0;
var menu2 = 0;
$(function() {
    $(".menu1").click(function() {
            if (menu1 == 0) {
                menu1 = 1;
                $(".menu1_c").fadeIn();
            } else if (menu1 == 1) {
                menu1 = 0;
                $(".menu1_c").fadeOut();
            }
        }),
        $(".menu2").click(function() {
            if (menu2 == 0) {
                menu2 = 1;
                $(".menu2_c").fadeIn();
            } else if (menu2 == 1) {
                menu2 = 0;
                $(".menu2_c").fadeOut();
            }
        })
})

$(function() {
    setTimeout(function() {
        $('.start p').fadeIn(1600);
        $('.start h1').fadeIn(1600);
    }, 500);
    setTimeout(function() {
        $('.start').fadeOut(500);
    }, 2500);
});