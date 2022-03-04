//会員登録 js

document.getElementById('registerIcon').onclick = function(){
    $('.login-form').hide();
    $('.register-form').show();
    const registerScreen = document.querySelector('.register-form');
    registerScreen.animate([{opacity: '0'}, {opacity: '1'}], 1000);
};

document.getElementById('returnIcon').onclick = function(){
    $('.register-form').hide();
    $('.login-form').show();
    const loginScreen = document.querySelector('.login-form');
    loginScreen.animate([{opacity: '0'}, {opacity: '1'}], 1000);
};