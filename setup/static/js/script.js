function user_menu() {
    var user_menu = document.getElementById("user-menu");
    user_menu.style.display = "block";

    var user_profile = document.getElementById("user-profile-link");
    user_profile.style.borderRadius = "19px";
    user_profile.style.borderBottomRightRadius = "0px";
    user_profile.style.borderBottomLeftRadius = "0px";
}

function hide_user_menu() {
    var user_menu = document.getElementById("user-menu");
    user_menu.style.display = "none";

    var user_profile = document.getElementById("user-profile-link");
    user_profile.style.borderRadius = "65px";
}

function delete_account_confirmation() {
    var confirmation = document.getElementById("delete-account-confirmation-container");
    confirmation.style.display = "flex";
}

function dont_delete_account() {
    var confirmation = document.getElementById("delete-account-confirmation-container");
    confirmation.style.display = "none";
}

function hide_message() {
    var message = document.getElementById("message");
    message.style.display = "none";
}