const swiper = new Swiper('.swiper', {
    loop: true,
    slidesPerView: 3, // نمایش دو اسلاید در کنار هم
    spaceBetween: 20, // فاصله بین اسلایدها به پیکسل
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
});