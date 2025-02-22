const buttonOpenPopupStandart = document.querySelector('#openPopup');
const buttonOpenPopupPro = document.querySelector('#ProButton')
const popupBg = document.querySelector('#popupBg');
const popup = document.querySelector('#popup');
const popup1 = document.querySelector('#popup1');
const popupBg1 = document.querySelector('#popupBg1');
const closePopup = document.querySelector('#closePopup');
const closePopup1 = document.querySelector('#closePopup1');




buttonOpenPopupStandart.addEventListener('click', () => {
    popup.style.display = 'flex';
            
    popupBg.style.display = 'flex';
    popupBg.style.position = 'fixed'
    popupBg.style.justifyContent = 'center';
    popupBg.style.alignItems = 'center';
                
});

buttonOpenPopupPro.addEventListener('click', () => {
    popup1.style.display = 'flex';
            
    popupBg1.style.display = 'flex';
    popupBg1.style.position = 'fixed'
    popupBg1.style.justifyContent = 'center';
    popupBg1.style.alignItems = 'center';
});


// const listOpenElement = [buttonOpenPopupStandart, buttonOpenPopupPro];

// listOpenElement.forEach(
//     (elem) => {
//         elem.addEventListener('click', () => {
//             popup.style.display = 'flex';
        
//             popupBg.style.display = 'flex';
//             popupBg.style.position = 'fixed'
//             popupBg.style.justifyContent = 'center';
//             popupBg.style.alignItems = 'center';
            
//         });

//     }
// );



closePopup.addEventListener('click', () => {
    popup.style.display = 'none';
    popupBg.style.display = 'none';
    }
);

closePopup1.addEventListener('click', () => {
    popup1.style.display = 'none';
    popupBg1.style.display = 'none';
    }
);