const buttonOpenPopupStandart = document.querySelector('#openPopupStandart');
const buttonOpenPopupPro = document.querySelector('#ProButton');
const popupBg = document.querySelector('#popupBg');
const popup = document.querySelector('#popup');
const popup1 = document.querySelector('#popup1');
const popupBg1 = document.querySelector('#popupBg1');
const closePopup = document.querySelector('#closePopup');
const closePopup1 = document.querySelector('#closePopup1');

const add = document.querySelector('#add');
const popupBg3 = document.querySelector('#popupBg3');
const popup3 = document.querySelector('#popup3');
const closePopup3 = document.querySelector('#closePopup3');

// Проверяем, что кнопки существуют перед добавлением обработчиков
if (buttonOpenPopupStandart) {
    buttonOpenPopupStandart.addEventListener('click', () => {
        popup.style.display = 'flex';
        popupBg.style.display = 'flex';
        popupBg.style.position = 'fixed';
        popupBg.style.justifyContent = 'center';
        popupBg.style.alignItems = 'center';
    });
}

if (buttonOpenPopupPro) {
    buttonOpenPopupPro.addEventListener('click', () => {
        popup1.style.display = 'flex';
        popupBg1.style.display = 'flex';
        popupBg1.style.position = 'fixed';
        popupBg1.style.justifyContent = 'center';
        popupBg1.style.alignItems = 'center';
    });
}

if (add) {
    add.addEventListener('click', () => {
        popup3.style.display = 'flex';
        popupBg3.style.display = 'flex';
        popupBg3.style.position = 'fixed';
        popupBg3.style.justifyContent = 'center';
        popupBg3.style.alignItems = 'center';
    });
}

if (closePopup) {
    closePopup.addEventListener('click', () => {
        popup.style.display = 'none';
        popupBg.style.display = 'none';
    });
}

if (closePopup1) {
    closePopup1.addEventListener('click', () => {
        popup1.style.display = 'none';
        popupBg1.style.display = 'none';
    });
}

if (closePopup3) {
    closePopup3.addEventListener('click', () => {
        popup3.style.display = 'none';
        popupBg3.style.display = 'none';
    });
}