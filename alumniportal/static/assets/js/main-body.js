function openModal(image){
        var modal = document.getElementById('myModal');

        // Get the image and insert it inside the modal - use its "alt" text as a caption
        var img = document.getElementById('myImg');
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
            modal.style.display = "block";
            modalImg.src = image.src;
            captionText.innerHTML = image.alt;
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function() {
            modal.style.display='none';
        }


}

$(window).load(function(){
        $('.main-nav li a').bind('click',function(event){
            var $anchor = $(this);
            
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top - 102
            }, 1500,'easeInOutExpo');
            /*
            if you don't want to use the easing effects:
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top
            }, 1000);
            */
            event.preventDefault();
        });
  if($(location)[0].pathname == '/'){
    $("#nav-home").addClass("nav-active")
  }else if($(location)[0].pathname.startsWith("/news/Achievement")){
    $("#nav-achievement").addClass("nav-active")
  }
  else if($(location)[0].pathname.startsWith("/activity")){
    $("#nav-activity").addClass("nav-active")
  }
  else if($(location)[0].pathname.startsWith("/community")){
    $("#nav-community").addClass("nav-active")
  }
  else if($(location)[0].pathname.startsWith("/search")){
    $("#nav-search").addClass("nav-active")
  }else if($(location)[0].pathname.startsWith("/profile")){
    $("#nav-profile").addClass("nav-active")
  }else if($(location)[0].pathname.startsWith("/news")){
    $("#nav-news").addClass("nav-active")
  }

  $(document).keypress(function(e) { 
    if (e.keyCode == 27) { 
        document.getElementById('myModal').style.display = 'none';
    } 
});
  $(document).keydown(function(e) { 
    if (e.which == 27) { 
        document.getElementById('myModal').style.display = 'none';
    } 
});

    })

  $( document ).ready(function() {
           $('#topnav').scrollToFixed();
        $('.res-nav_click').click(function(){
            $('.main-nav').slideToggle();
            return false    
            
        });        
});