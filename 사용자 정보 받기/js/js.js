const nameElmenet = document.querySelector("#name");
let name = prompt("당신의 이름은?");
nameElmenet.textContent = name;

const hobbyElement = document.querySelector("#hobby");
let hobby = prompt("당신의 취미는?");
hobbyElement.textContent = `취미는 ${hobby}입니다!`;

document.querySelector("#song").textContent = `좋아하는 곡은 ${prompt(
  "좋아하는곡은?"
)}입니다!`;
