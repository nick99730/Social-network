$(document).ready(function () {
    $("#form1").on('submit', (function (e) {
        e.preventDefault();
        let formData = new FormData($('#form1')[0]);
                $.ajax({
                    type: "POST",
                    url: "",
                    data: formData,
                    cache:false,
                    contentType: false,
                    processData: false,
                }).done(function () {
                    $("#pedit_result").css("display", "block")
                });
    }))
});