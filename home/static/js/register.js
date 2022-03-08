//会員登録 js

//ユーザー登録の判定、初期値設定
if(!sessionStorage.getItem("registerFlg")){
    sessionStorage.setItem("registerFlg",1);
}

//ユーザー登録の判定、ログイン画面かユーザー登録なのか判定
document.getElementById('registerIcon').onclick = function(){
    if(sessionStorage.getItem("registerFlg")%2==1){
        $('.login-form').hide();
        $('.login-form-errors').hide();
        $('.register-form').show();
        const registerScreen = document.querySelector('.register-form');
        registerScreen.animate([{opacity: '0'}, {opacity: '1'}], 1000);
        sessionStorage.setItem("registerFlg",Number(sessionStorage.getItem("registerFlg"))+1);
    }
};


document.getElementById('returnIcon').onclick = function(){
    if(sessionStorage.getItem("registerFlg")%2==0){
        $('.register-form').hide();
        $('.register-form-errors').hide();
        $('.login-form').show();
        const loginScreen = document.querySelector('.login-form');
        loginScreen.animate([{opacity: '0'}, {opacity: '1'}], 1000);
        sessionStorage.setItem("loginFlg", "check");
        sessionStorage.setItem("registerFlg",Number(sessionStorage.getItem("registerFlg"))+1);
    }
};