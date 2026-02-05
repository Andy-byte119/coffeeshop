const swiper = new Swiper('.swiper', {
	effect: 'coverflow',
	grabCursor: true,
	centeredSlides: true,
	slidesPerView: 4,
	spaceBetween: 30,
	speed: 400,

	coverflowEffect: {
		rotate: 30,
		stretch: -30,
		depth: 150,
		modifier: 1,
		slideShadows: true,
	},

	loop: false,

	keyboard: {
		enabled: true,
	},

	pagination: {
		el: '.swiper-pagination',
		type: 'fraction',
		dynamicBullets: false,
		clickable: true,
	},
});