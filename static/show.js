console.log('Hello from show.js');

//アップロードボタンを変数に格納
const upload = document.getElementById("uploadFile");
//アップロードされたら
upload.addEventListener("change",function(event){
    //ファイル名を取得
    const fileName = event.target.files[0].name;
},false)