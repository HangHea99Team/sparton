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
                let userImg = rows[i]['userImg']
                let userName = rows[i]['userName']
                let info = rows[i]['info']
                let job = rows[i]['job']
                let stack = rows[i]['stack']

                let temp_html = `<div class="col">
                                    <div class="card h-100">
                                        <img src="${userImg}"
                                             class="userImg">
                                        <div class="card-body">
                                            <h5 class="userName">${userName}</h5>
                                            <p class="info">${info}</p>
                                            <p class="job">${job}</p>
                                            <p class="stack">${stack}</p>
                                        </div>
                                    </div>
                                </div>`

                $('#cards-box').append(temp_html)
            }
        }
    })
}

function open_login() {
  alert("로그인 버튼 클릭!")
}

function open_signUP() {
  alert("로그인 버튼 클릭!")
}