$(document).ready(function(){
    $('#menu').on('click', function(){
        $('nav').parent().toggleClass('mobile');
        $('.menu-icon').toggleClass('fa-times');
        return false;
    });

	var scroll = new SmoothScroll('a[href*="#"]', {
        offset: 70
    });
});
function requestFormOnSubmit(token) {
    document.getElementById("requestForm").submit();
  }