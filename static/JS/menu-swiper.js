document.addEventListener('DOMContentLoaded', function() {
    if (document.querySelector('.swiper')) {
        new Swiper('.swiper', {
            effect: 'coverflow',
            loop: true,
            grabCursor: true,
            centeredSlides: true,
            slidesPerView: 3,
            initialSlide: 0,
            spaceBetween: 30,
            speed: 400,
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },

            coverflowEffect: {
            rotate: 15,
            stretch: -15,
            depth: 180,
            modifier: 1.5,
            slideShadows: false,
	},

            pagination: {
            el: '.swiper-pagination',
            type: 'bullets',
            dynamicBullets: true,
            dinamicmainBullets: 1,
            clickable: true,
            },

        });

    }

});