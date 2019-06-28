let menu = document.querySelector('#top_profile_menu');
let button = document.querySelector('#top_profile_link');
button.onclick = function() {
        let classList = menu.classList;
        if (classList.contains('shown')) {
            menu.classList.remove("shown");
        } else {
            menu.classList.add("shown");
        }
};
let show_button = document.querySelector('.profile_more_info_link');
let information_div = document.querySelector('#profile_full');
show_button.onclick = function () {
    if(information_div.style.display === "block") {
        information_div.style.display = "none";
    }
    else {
        information_div.style.display = "block";
    }
};