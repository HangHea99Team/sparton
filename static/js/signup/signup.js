function signup() {
    $.ajax({
        type: 'post',
        url: "/signUp",
        data: {
            userId: $('#signUp_userId').val(),
            userName: $('#signUp_username').val(),
            pass1: $('#signUp_password').val(),
            pass2: $('#signUp_password_check').val(),
            email: $('#signUp_email').val()
        },
        success: function (response) {
            console.log(response)
            alert(response['msg'], response['result'])
            if (response['result'] == 'success') {
                window.location.href = '/login'
            }

        }
    })
}
function login() {
    $.ajax({
        type: 'post',
        url: "/login",
        data: {
            userId: $('#login_userId').val(),
            password: $('#login_password').val(),
        },
        success: function (response) {
            console.log(response)
            alert(response['msg'], response['result'])
            if (response['result'] == 'success') {
                
                window.location.href = '/'
                
            }

        }
    })
}