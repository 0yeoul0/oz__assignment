// 시계 기능을 추가합니다.
function updateClock() {
  const now = new Date();
  const hours = now.getHours().toString().padStart(2, "0");
  const minutes = now.getMinutes().toString().padStart(2, "0");
  const seconds = now.getSeconds().toString().padStart(2, "0");
  const date = now.toLocaleDateString("ko-KR");
  // 템플릿 리터럴을 사용하여 문자열을 구성합니다.
  document.getElementById(
    "clock"
  ).textContent = `${date} ${hours}:${minutes}:${seconds}`;
}

// 시계를 1초마다 업데이트합니다.
setInterval(updateClock, 1000);
updateClock(); // 페이지 로드 시 바로 시간 업데이트
