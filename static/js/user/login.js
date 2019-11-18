function add() {

    var $captcha = $('#recaptcha'),
        response = grecaptcha.getResponse();

    if (response.length === 0) {
        $('.msg-error').text("reCAPTCHA is mandatory");
        if (!$captcha.hasClass("error")) {
            $captcha.addClass("error");
            return false;
        }
    } else {
        $('.msg-error').text('');
        $captcha.removeClass("error");
    }

    let flag = true

    if ($('#login-username').val()==""){
        document.getElementById("login-username").style.borderColor = "red";
        flag = false
    }


    if ($('#login-password').val()==""){
        document.getElementById("login-password").style.borderColor = "red";
        flag = false
    }

    if(flag){

        $.ajax({
            data : {
                username: $('#login-username').val(),
                password: $('#login-password').val()
            },
            type: "POST",
            url: "softflix/api/login"
        }).done(function (data) {
            if (data == "1"){
                $("#correct").toggle(750, function () {
                    setTimeout(function () {
                        $("#correct").toggle(750);
                        }, 2500);
                });
                // document.getElementById("loginform").submit()
            }
            else{
                $("#invalid-pass").toggle(750, function () {
                    setTimeout(function () {
                        $("#invalid-pass").toggle(750);
                        }, 2500);
                });
            }

        })

        // document.getElementById("loginform").submit()
    }
    else{
        $(".message-box-danger").toggle(750, function () {
            setTimeout(function () {
                $(".message-box-danger").toggle(750);
            }, 2500);
        });
        return false
    }

}



$('#login-username').on('change keyup paste delete', function () {

    document.getElementById("login-username").style.borderColor = "";

});

$('#login-password').on('change keyup paste delete', function () {

    document.getElementById("login-password").style.borderColor = "";

});

$('#recaptcha').on('change keyup paste delete', function () {

    document.getElementById("recaptcha").style.borderColor = "";

});

