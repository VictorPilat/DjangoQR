
let rangeInput = document.querySelector('#input-range');
let rangeLabel = document.querySelector('#range-label');




function colorChanging(){

  let colorPicker = document.querySelector("#color-picker");
  colorPicker.value = '#000000'
  let colorText = document.querySelector('#color-text');
  colorText.value = '#000000'

  let colorPicker1 = document.querySelector("#color-picker1");
  colorPicker1.value = '#ffffff'
  let colorText1 = document.querySelector('#color-text1');
  colorText1.value = '#ffffff'


  colorPicker.addEventListener(type = 'input', listener = () => {
    colorText.value = colorPicker.value;
  });
  
  colorText.addEventListener(type = 'input', listener = () => {
    colorPicker.value = colorText.value;
  });


  colorPicker1.addEventListener(type = 'input', listener = () => {
    colorText1.value = colorPicker1.value;
  });
  
  colorText1.addEventListener(type = 'input', listener = () => {
    colorPicker1.value = colorText1.value;
  });



}


  // Функція для оновлення тексту в label
  function updateLabel() {
    rangeLabel.textContent = `Ширина: ${rangeInput.value}px`;
  }

  // Оновлюємо значення при зміні повзунка range
  rangeInput.addEventListener('input', listener = updateLabel);

 



// Викликаємо функції після завантаження сторінки
document.addEventListener('DOMContentLoaded', () => {
  colorChanging(); 
  updateLabel();
});


