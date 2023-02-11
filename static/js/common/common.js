$(document).ready(function(){
  listing();
});

function listing() {
    $.ajax({
        type: 'GET',
        url: '/card',
        data: {},
        success: function (response) {
            $('#cards-box').empty()
            let rows = response['card']
            for(let i = 0; i < rows.length; i++) {
                let userId = rows[i]['userId']
                let userImg = rows[i]['userImg']
                let userName = rows[i]['userName']
                let job = rows[i]['job']
                let stack = rows[i]['stack']

                let temp_html = `<div class="col" onclick="viewCardPopup('${userId}')">
                                    <div class="card h-100">
                                        <img src="${userImg}"
                                             class="userImg">
                                        <div class="card-body">
                                            <h5 class="userName">${userName}</h5>
                                            <p class="job">${job}</p>
                                            <span class="stack">${stack}</span>
                                        </div>
                                    </div>
                                </div>`

                $('#cards-box').append(temp_html)
            }
        }
    })
}

function out() {
    $.ajax({
        type: 'GET',
        url: '/logout',
        data: {},
        success: function (response) {
            alert(response["msg"])
            window.location.reload()               
        }
    })
}

const user = document.querySelector(".user").innerText;
function open_login(){
    $('.login-btn').show();
}
function close_login(){
    $('.login-btn').hide();
}

if (user != '') {
    close_login();
}
else{
    open_login();
}

function open_mypage(){
    $('.mypage-btn').show();
}
function close_mypage(){
    $('.mypage-btn').hide();
}

if (user != '') {
    open_mypage();
}
else{
    close_mypage();
}

