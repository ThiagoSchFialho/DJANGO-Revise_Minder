function user_menu() {
    var user_menu = document.getElementById("user-menu");
    user_menu.style.display = "block";

    var user_profile = document.getElementById("user-profile");
    user_profile.style.borderRadius = "18px";
    user_profile.style.borderBottomRightRadius = "0px";
    user_profile.style.borderBottomLeftRadius = "0px";
}

function hide_user_menu() {
    var user_menu = document.getElementById("user-menu");
    user_menu.style.display = "none";

    var user_profile = document.getElementById("user-profile");
    user_profile.style.borderRadius = "65px";
}