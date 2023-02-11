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
            gitUrl_give: gitUrl
        },
        success: function (response) {
            alert(response['msg'])
            profileForm.elements[name = 'userId'].value = null;
            profileForm.elements[name = 'image'].value = null;
            profileForm.elements[name = 'nick'].value = null;
            profileForm.elements[name = 'about'].value = null;
            profileForm.elements[name = 'job'].value = null;
            profileForm.elements[name = 'techStack'].value = null;
            profileForm.elements[name = 'email'].value = null;
            profileForm.elements[name = 'gitUrl'].value = null;
        }
    })
});