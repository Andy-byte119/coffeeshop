const swiper = new Swiper('.swiper', {
	effect: 'coverflow',
	grabCursor: true,
	centeredSlides: true,
	slidesPerView: 2.5,
	initialSlide: 0,
	spaceBetween: 30,
	speed: 400,
	
	

	coverflowEffect: {
		rotate: 20,
		stretch: -20,
		depth: 150,
		modifier: 1.5,
		slideShadows: false,
	},

	loop: true,

	keyboard: {
		enabled: true,
	},

	pagination: {
		el: '.swiper-pagination',
		type: 'bullets',
		dynamicBullets: true,
		dinamicmainBullets: 1,
		clickable: true,
	},
});