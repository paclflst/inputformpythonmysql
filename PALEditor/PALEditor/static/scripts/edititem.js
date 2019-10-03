$(function () {
    $('#btnSignUp').click(function () {
        $('form').attr("disabled", "disabled");
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
                $("form")[0].reset();
                $("#messageSuccess").show()
            },
            error: function (error) {
                console.log(error);
            }
        });
        $('form').removeAttr("disabled", false);
    });
});