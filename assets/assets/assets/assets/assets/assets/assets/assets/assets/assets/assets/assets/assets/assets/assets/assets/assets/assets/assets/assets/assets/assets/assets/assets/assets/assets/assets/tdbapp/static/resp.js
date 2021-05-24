burger = document.querySelector('.burger');
navbar = document.querySelector('.navbar');
navList = document.querySelector('.nav-list');
Slogo = document.querySelector('.Slogo');


burger.addEventListener('click', ()=>{
    burger.classList.toggle('Iburger');
    navList.classList.toggle('v-class-resp');
    navbar.classList.toggle('h-nav-resp');
    Slogo.classList.toggle('Ilogo');
});

//paste this code under the head tag or in a separate js file.
	// Wait for window load
	$(window).load(function() {
		// Animate loader off screen
		$(".se-pre-con").fadeOut("slow");;
	});