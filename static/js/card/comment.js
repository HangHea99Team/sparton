const cardComment = document.getElementById('comment-input');

function writeComment(){
    let comment = cardComment.value;
    let sendUser = document.getElementById('login-userId').value;
    let targetUser = document.getElementById('userInfo-id').innerText;

    if(chkNull(sendUser)){
        alert("로그인 후 사용가능합니다.")
        return;
    }

    $.ajax({
        type: 'POST',
        url: '/card/sendReply',
        data: {
            send_user: sendUser,
            target_user: targetUser,
            send_comment: comment,
        },
        success: function (response) {
            let comments = JSON.parse(response['comments']);
            $("#reply-box").empty();

            for(let i = 0 ; i < comments.length ; i++){
                let sendComment = comments[i]['sendComment'];
                let sendUserImg = comments[i]['sendUserImg'];
                let sendUserName = comments[i]['sendUserName'];
                let sendTime = comments[i]['dateTime'];

                let temp_html = `<li class="comment-item">
                                    <div class="comment-user">
                                        <img src="${sendUserImg}"
                                             id="comment-user-img"/>
                                    </div>
                                    <div class="comment-content">
                                        <div class="content-box">
                                            <p id="comment-user-name">
                                                ${sendUserName}
                                            </p>
                                            <p id="comment-user-content">
                                                ${sendComment}
                                            </p>
                                        </div>
                                        <div class="comment">
                                            <p id="comment-time">
                                                ${sendTime}
                                            </p>
                                        </div>
                                    </div>
                                </li>`
                $("#reply-box").append(temp_html);
            }
            cardComment.value = '';
        }
    })
}

function loadComment(){
    let targetUser = document.getElementById('userInfo-id').innerText;

    $.ajax({
        type: 'GET',
        url: '/card/getReply',
        data: {
            target_id: targetUser,
        },
        success: function (response) {
            let comments = JSON.parse(response['comments']);

            for(let i = 0 ; i < comments.length ; i++){
                let sendComment = comments[i]['sendComment'];
                let sendUserImg = comments[i]['sendUserImg'];
                let sendUserName = comments[i]['sendUserName'];
                let sendTime = comments[i]['dateTime'];

                let temp_html = `<li class="comment-item">
                                    <div class="comment-user">
                                        <img src="${sendUserImg}"
                                             id="comment-user-img"/>
                                    </div>
                                    <div class="comment-content">
                                        <div class="content-box">
                                            <p id="comment-user-name">
                                                ${sendUserName}
                                            </p>
                                            <p id="comment-user-content">
                                                ${sendComment}
                                            </p>
                                        </div>
                                        <div class="comment">
                                            <p id="comment-time">
                                                ${sendTime}
                                            </p>
                                        </div>
                                    </div>
                                </li>`
                $("#reply-box").append(temp_html);
            }
            cardComment.value = '';
        }
    })
}

function chkNull(str){
    if(str == '' || str == 'undefined' || str == null){
        return true
    }else{
        return false;
    }
}