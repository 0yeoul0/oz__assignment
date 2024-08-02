let monsterHP = 100;
container = document.getElementById("container");
const h1 = document.createElement("h1");
h1.textContent = "몬스터 잡기 게임을 시작합니다!";
container.appendChild(h1);

let attackDamage = parseInt(prompt("1회 공격시 데미지는? (양의 정수)"));
let attackCount = 0;

if (attackDamage > 0) {
  while (monsterHP > 0) {
    monsterHP -= attackDamage;
    if (monsterHP < 0) {
      monsterHP = 0;
    }
    attackCount += 1;

    const p = document.createElement("p");
    p.textContent = `몬스터를 ${attackCount}회 공격했다! `;
    container.append(p);

    const strong = document.createElement("strong");
    strong.textContent = `몬스터의 남은 HP 는 ${monsterHP} 입니다!`;
    container.append(strong);
  }

  const h2 = document.createElement("h2");

  h2.textContent = "몬스터 잡기 완료!";
  h2.style.color = "orange";
  h2.title = "게임을 다시 시작하고 싶다면 새로고침!!";
  container.appendChild(h2);
} else {
  alert("데미지를 잘못입력하여 게임을 취소합니다.");
}
