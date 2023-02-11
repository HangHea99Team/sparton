const signPopup = document.querySelector("#user-card-popup");
const cardUserId = document.getElementById('userInfo-id');
const cardUserName = document.getElementById('userInfo-name');
const cardUserJob = document.getElementById('userInfo-job');
const cardUserEmail = document.getElementById('userInfo-email');
const cardUserGit = document.getElementById('userInfo-git');
const cardUserAbout = document.getElementById('userInfo-about');
const cardUserImg = document.getElementById('userInfo-image');

const cardPopLike = document.getElementById('cardPop_like');

function viewCardPopup(user) {
    $.ajax({
        type: 'GET',
        url: '/card/detail',
        data: {
            search_id: user,
        },
        success: function (response) {
            let userInfo = JSON.parse(response['userInfo']);

            let userId = userInfo.userId
            let userName = userInfo.userName;
            let userJob = userInfo.job;
            let userEmail = userInfo.email;
            let userGit = userInfo.github;
            let userAbout = userInfo.info;
            let userImg = userInfo.userImg;
            let userLike = userInfo.like;

            if (isNull(userImg)) {
                userImg = 'https://avatars.githubusercontent.com/u/51357635?s=400&u=36fd01b69ccd7729620c086927f9c0847ffdb0e1&v=4';
            }

            if (isNull(userLike)) {
                userLike = 0;
            }

            cardUserId.innerText = userId;
            cardUserName.innerText = userName;
            cardUserJob.innerText = userJob;
            cardUserEmail.href = 'mailto:'+userEmail;
            cardUserGit.href = userGit;
            cardUserAbout.innerText = userAbout;
            cardUserImg.src = userImg;
            cardPopLike.innerText = userLike;

            signPopup.style.display = "block";
        }
    })
}

function hideCardPopup() {
    signPopup.style.display = "none";
}

function isNull(str){
    if(str == '' || str == 'undefined' || str == null){
        return true
    }else{
        return false;
    }
}

function likeThisUser(){
    $.ajax({
        type: 'GET',
        url: '/card/likeUser',
        data: {
            search_id: cardUserId.innerText,
        },
        success: function (response) {
            let userInfo = JSON.parse(response['userInfo']);
            cardPopLike.innerText = userInfo['like'];
        }
    })
}