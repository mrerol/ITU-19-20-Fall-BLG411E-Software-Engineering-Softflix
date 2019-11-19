function email_checker(){
    let email = $('#email').val();
    let splitted = email.split('@')
    if (splitted.length === 1){
        document.getElementById("email").style.borderColor = "red";
        $("#invalid-email-format").css('display','block');
        $("#invalid-email").css('display','none');
        return false
    }

    let left = email.split('@')[0];
    let remaining = email.split('@')[1];
    if (remaining.length === 1){
        document.getElementById("email").style.borderColor = "red";
        $("#invalid-email-format").css('display','block');
        $("#invalid-email").css('display','none');
        return false;
    }

    let middle = remaining.split('.')[0];
    let right = remaining.split('.')[1];
    if (left.length === 0 || middle.length === 0 || right.length === 0){
        document.getElementById("email").style.borderColor = "red";
        $("#invalid-email-format").css('display','block');
        $("#invalid-email").css('display','none');
        return false;
    }
    else{
        $("#invalid-email-format").css('display','none');
        $.ajax({
            data : {
                email: email
            },
            type: "POST",
            url: "softflix.api.validate_email"
        }).done(function (data) {
            if (data === "1"){
                document.getElementById("email").style.borderColor = "green";
                $("#invalid-email").css('display','none');
                $("#invalid-email-format").css('display','none');
                return true;
            }
            else if (data === "-1"){
                document.getElementById("email").style.borderColor = "red";
                $("#invalid-email-format").css('display','block');
                $("#invalid-email").css('display','none');
                return false;
            }
            else{
                document.getElementById("email").style.borderColor = "red";
                $("#invalid-email").css('display','block');
                $("#invalid-email-format").css('display','none');
                return false;
            }

        })
    }
}


function username_checker() {

    let username = $('#username').val()
    if (username.length < 8 || username.length > 25){
        document.getElementById("username").style.borderColor = "red";
        $("#invalid-username-length").css('display','block');
        return false;
    }
    else{
        $("#invalid-username-length").css('display','none');
        $.ajax({
            data : {
                username: username
            },
            type: "POST",
            url: "softflix.api.validate_username"
        }).done(function (data) {
            if (data == "1"){
                document.getElementById("username").style.borderColor = "green";
                $("#invalid-username").css('display','none');
                return true;
            }
            else{
                document.getElementById("username").style.borderColor = "red";
                $("#invalid-username").css('display','block');
                return false;

            }

        })
    }
}

function password_checker() {

    let password = $('#password').val()
    if (password.length < 8 || password.length > 25){
        document.getElementById("password").style.borderColor = "red";
        $("#invalid-password-length").css('display','block');
        return false;
    }
    else{
        document.getElementById("password").style.borderColor = "green";
        $("#invalid-password-length").css('display','none');
        return true;
    }
}

function register() {
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

    let flag = true;

    if ($('#invalid-username-length').css('display') === "block" || $('#invalid-username').css('display') === "block")
        flag = false;

    if ($('#invalid-email-format').css('display') === "block" || $('#invalid-email').css('display') === "block")
        flag = false;

    if ($('#invalid-password-length').css('display') === "block")
        flag = false;





    if ($('#fullname').val()==""){
        document.getElementById("fullname").style.borderColor = "red";
        flag = false
    }

    if(flag){
        let form = $('#fileUploadForm')[0];

        let data = new FormData(form);

        $.ajax({
            data : {
                username: $('#username').val(),
                password: $('#password').val(),
                email: $('#email').val(),
                fullname: $('#fullname').val(),
                gender: $('input[name=gender]:checked').val(),
                address: $('#address').val(),
            },
            type: "POST",
            url: "softflix.api.register",
            enctype: 'multipart/form-data',
            beforeSend: function () {
                $('#btn-signup').attr("disabled","disabled");
                $('#signupform').css("opacity",".5");
            }
        }).done(function (data) {
            console.log("data", data)
            if (data == "1"){
                $("#correct").toggle(750, function () {
                    setTimeout(function () {
                        $("#correct").toggle(750);
                        }, 2500);
                    window.alert("Successfully registered! Check your email to activate your account")
                    window.location = "/login"
                });

                // document.getElementById("loginform").submit()
            }
            else{
                 $("#back-error").css('display','block');
            }

        })

        // document.getElementById("loginform").submit()
    }
    else{
        $("#register-error").css('display','block');
        return false
    }

}



$('#username').on('change keyup paste delete', function () {


    username_checker();



});

$('#password').on('change keyup paste delete', function () {

    password_checker();

});



$('#email').on('change keyup paste delete', function () {


    email_checker();



});

$('#fullname').on('change keyup paste delete', function () {

    document.getElementById("fullname").style.borderColor = "";

});

$('#recaptcha').on('change keyup paste delete', function () {

    document.getElementById("recaptcha").style.borderColor = "";

});

