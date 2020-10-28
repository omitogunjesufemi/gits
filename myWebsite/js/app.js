function changeImage() {
  document.getElementById("image1").src = "images/img2.png";
}
function changeText() {
  document.getElementById("demo").innerHTML = "Hello JavaScript";
}

const num1_input = document.getElementById("num1");
const num2_input = document.getElementById("num2");
const result_field = document.getElementById("result");

function add(num1, num2) {
  let result;
  result = num1 + num2;
  return result;
}

function subtract(num1, num2) {
  let result;
  result = num1 - num2;
  return result;
}

function multiply(num1, num2) {
  let result;
  result = num1 * num2;
  return result;
}

function divide(num1, num2) {
  let result;
  result = num1 / num2;
  return result;
}

function modulus(num1, num2) {
  let result;
  result = num1 % num2;
  return result;
}

function getNum1() {
  let x = num1_input;
  return parseFloat(x.value);
}

function getNum2() {
  let y = num2_input;
  return parseFloat(y.value);
}

function addClick() {
  let x = getNum1();
  let y = getNum2();

  let result = add(x, y);
  result_field.value = result;
}

function subClick() {
  let x = getNum1();
  let y = getNum2();

  let result = subtract(x, y);
  result_field.value = result;
}

function mulClick() {
  let x = getNum1();
  let y = getNum2();

  let result = multiply(x, y);
  result_field.value = result;
}

function modClick() {
  let x = getNum1();
  let y = getNum2();

  let result = modulus(x, y);
  result_field.value = result;
}

function divClick() {
  let x = getNum1();
  let y = getNum2();

  let result = divide(x, y);
  result_field.value = result;
}
