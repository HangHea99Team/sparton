const profileForm = document.getElementById("profileForm");

profileForm.addEventListener("submit", function (event) {
    event.preventDefault();

    let id = this.elements[name = 'userId'].value;
    let image = this.elements[name = 'image'].value;
    let nick = this.elements[name = 'nick'].value;
    let about = this.elements[name = 'about'].value;
    let job = this.elements[name = 'job'].value;
    let techStack = this.elements[name = 'techStack'].value;
    let email = this.elements[name = 'email'].value;
    let gitUrl = this.elements[name = 'gitUrl'].value;

    $.ajax({
        type: 'POST',
        url: '/profile/save',
        data: {
            id_give: id,
            image_give: image,
            nick_give: nick,
            about_give: about,
            job_give: job,
            techStack_give: techStack,
            email_give: email,
            gitUrl_give: gitUrl,
            like_give: '0'
        },
        success: function (response) {
            alert(response['msg'])
            location.href = document.location.href.split('/')[0]+'//'+document.location.href.split('/')[2]+'/'
        }
    })
});

function checkProfileCard(){

    let userId = document.getElementById('login-userId').value;
    let profileHeader = document.getElementById('profile_mod_header')

    $.ajax({
        type: 'GET',
        url: '/card/chkWrite',
        data: {
            search_id: userId,
        },
        success: function (response) {
            let writeChk = JSON.parse(response['userInfo']).writeCard;

            if(!writeChk){
                profileHeader.innerText = '프로필 입력하기'
            }else{
                profileHeader.innerText = '프로필 수정하기'
            }
        }
    })
}

function profileMod(){
    let userId = document.getElementById('login-userId').value;

    $.ajax({
        type: 'GET',
        url: '/card/detail',
        data: {
            search_id: userId,
        },
        success: function (response) {
            let userInfo = JSON.parse(response['userInfo']);

            if(userInfo == null){
                return;
            }

            console.log(userInfo);
            profileForm.elements[name = 'image'].value = userInfo.userImg;
            profileForm.elements[name = 'nick'].value = userInfo.userName;
            profileForm.elements[name = 'about'].value = userInfo.info;
            profileForm.elements[name = 'job'].value = userInfo.job;
            profileForm.elements[name = 'techStack'].value = userInfo.stack;
            profileForm.elements[name = 'email'].value = userInfo.email;
            profileForm.elements[name = 'gitUrl'].value = userInfo.github;
        }
    })
}

window.onload = () => {
    checkProfileCard();
    profileMod();
}