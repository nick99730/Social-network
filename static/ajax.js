$(document).ready(function () {
    $("#form1").on('submit', (function (e) {
        e.preventDefault();
        let formData = new FormData($('#form1')[0]);
        let fst_name = $("#pedit_first_name").val();
        let lst_name = $("#pedit_last_name").val();
        let error_msg = "";
        if (/[0-9]/.test(fst_name)) error_msg = "The value of the field \"First name\" must not contain numbers.";
        if (/[0-9]/.test(lst_name)) error_msg += "The value of the field \"Last name\" must not contain numbers.";
        if (error_msg === "") {
            $("#error_message").removeClass('d-flex');
            $.ajax({
                type: "POST",
                url: "",
                data: formData,
                cache: false,
                contentType: false,
                processData: false,
            }).done(function () {
                $("#pedit_result").show();
            });
        }
        else {
            $("#pedit_result").hide();
            $("#error_message").html("<div>" + error_msg +  "</div>");
            $("#error_message").addClass("d-flex");
        }
    }))
});