$(document).ready(function(){
    var sim = 0;
    $("input[type='radio']").click(function(){
    sim = $("input[type='radio']:checked").val();
    //alert(sim);
    if (sim<3) { $('.myratings').css('color','red'); $(".myratings").text(sim); }else{ $('.myratings').css('color','green'); $(".myratings").text(sim); } }); 
    var token = "{{csrf_token}}";
    console.log(sim);
$.ajax({
    type: "POST",
    headers: { "X-CSRFToken": token },
    url: "rate",
    data: { rate: sim },

    success: function (data) {
        $("#rating-result").html(
        '<p style="color:green">Rating Successfully Submitted</p>'
        );
        console.log(data);
        // $('#comments').append(data)
    },
    error: function (data) {
        $("#rating-result").html(
        '<p style="color:red">error occured</p>'
        );
        console.log(data);
    },
    });
});