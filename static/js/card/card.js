const signPopup = document.querySelector("#user-card-popup");
const cardUserId = document.getElementById('userInfo-id');
const cardUserName = document.getElementById('userInfo-name');
const cardUserJob = document.getElementById('userInfo-job');
const cardUserEmail = document.getElementById('userInfo-email');
const cardUserGit = document.getElementById('userInfo-git');
const cardUserAbout = document.getElementById('userInfo-about');
const cardUserImg = document.getElementById('userInfo-image');
const cardUserComment = document.getElementById('comment-input');

function viewCardPopup(user) {
    $.ajax({
        type: 'GET',
        url: '/card/detail',
        data: {
            search_id: user,
        },
        success: function (response) {
            let userInfo = JSON.parse(response['userInfo']);
            console.log(userInfo)
            let userId = userInfo.userId
            let userName = userInfo.userName;
            let userJob = userInfo.job;
            let userEmail = userInfo.email;
            let userGit = userInfo.github;
            let userAbout = userInfo.info;
            let userImg = userInfo.userImg;

            if(userImg == '' || userImg == 'undefined' || userImg == null){
                userImg = 'https://avatars.githubusercontent.com/u/51357635?s=400&u=36fd01b69ccd7729620c086927f9c0847ffdb0e1&v=4';
            }

            cardUserId.innerText = userId;
            cardUserName.innerText = userName;
            cardUserJob.innerText = userJob;
            cardUserEmail.innerText = userEmail;
            cardUserGit.innerText = userGit;
            cardUserAbout.innerText = userAbout;
            cardUserImg.src = userImg;
        }
    })
    signPopup.style.display = "block";
}

function saveReple() {
    let writerId = 'hhhhh'
    let comment = $('#comment-input').val()
    let today = new Date().toISOString().substring(0, 10)
    let reple = cardUserId.innerText
    $.ajax({
        type: 'POST',
        url: '/reple/save',
        data: {
            'writer_give': writerId, 'comment_give': comment, 'date_give': today, 'reple_give': reple
        },
        success: function (response) {
            alert(response["msg"])
            JSON.stringify(response["reple_list"])
            alert(JSON.stringify(response["reple_list"]))
        }
    })
}

function viewReple() {

}

function hideCardPopup() {
    signPopup.style.display = "none";
}