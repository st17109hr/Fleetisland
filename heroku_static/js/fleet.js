var date = 1;
var name = 1;
var text = 1;
$(function() {
    $(".date_tag").click(function() {
            if (date == 0) {
                date = 1;
                $(".date").fadeIn();
            } else if (date == 1) {
                date = 0;
                $(".date").fadeOut();
            }
        }),
        $(".name_tag").click(function() {
            if (name == 0) {
                name = 1;
                $(".name").fadeIn();
            } else if (name == 1) {
                name = 0;
                $(".name").fadeOut();
            }
        }),
        $(".text_tag").click(function() {
            if (text == 0) {
                text = 1;
                $(".text").fadeIn();
            } else if (text == 1) {
                text = 0;
                $(".text").fadeOut();
            }
        })
})