function myFunction() {
  $('#url').select();
  document.execCommand("copy");
  alert("Ссылка скопирована в буфер обмена");
}


$(window).scroll(function(){
    if ($(this).scrollTop() > 800) {
        $('.top_button').fadeIn();
    }
    else {
        $('.top_button').fadeOut();
    }
});
$('.top_button').click(function(){
    $("html").animate({ scrollTop: 0 }, 600);
});


$('.galery img').click(function(){
    $('.modal').html("<img src='"+$(this).attr("src")+"'>").css('display','flex');
});
$('.share_but').click(function(){
    $('.modal .share').css('display','flex');
    $('.modal').css('display','flex');
});
$('.modal').click(function(){
    $(this).css('display','none');
});