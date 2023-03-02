$(document).ready(function () {
    $("#collapse").on("click", function () {
        $("#sidebar").toggleClass("active");
        $(".fa-align-justify").toggleClass("fa-align-right");
    });
});
