const btnAdd = document.querySelector("#fileSubmit");
btnAdd.addEventListener("click", (event) => {
    console.log("送信が押されました");
    event.preventDefault();

    let uploadFile = document.querySelector('input[name=uploadFile]')


    if (uploadFile== "") {
        document.querySelector("#error-container").innerHTML = "ファイルを選択してください"
        document.querySelector('#error-container').style.display = "block"
        return
    }

    const formData = new FormData();
    formData.append('uploadFile', uploadFile.files[0]);

    fetch("/upload", {
        method: "POST",
        body: formData
    }).then(response => {
        console.log(response);
        response.json().then((data) => {
            console.log(data);  // 取得されたレスポンスデータをデバッグ表示

            document.querySelector('#error-container').style.display = "none"
            document.querySelector('#message-container').style.display = "none"

            if (data.result == "error") {
                document.querySelector("#error-container").innerHTML = "書き込みに失敗しました"
                document.querySelector('#error-container').style.display = "block"
                return
            }
            else if (data.result == "success") {
                document.querySelector("#message-container").innerHTML = "書き込みに成功しました"
                document.querySelector('#message-container').style.display = "block"
            }
        });
    });
})