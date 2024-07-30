function validateLogin(event) {
  // <-- 수정: 폼 검증 함수 정의
  event.preventDefault(); // <-- 수정: 폼의 기본 제출 동작 방지

  // 입력 필드 값 가져오기
  var username = document.querySelector('input[type="text"]').value;
  var password = document.querySelector('input[type="password"]').value;

  // 아이디와 비밀번호 형식 검증
  var usernamePattern = /^[A-Za-z0-9]{8,}$/; // 아이디: 최소 8글자, 문자와 숫자만
  var passwordPattern =
    /^(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/; // 비밀번호: 최소 8자, 숫자, 문자, 특수문자

  if (!usernamePattern.test(username)) {
    // <-- 수정: 아이디 형식 검증
    alert("아이디는 최소 8글자와 숫자만 입력할 수 있습니다.");
    return false; // <-- 수정: 검증 실패 시 폼 제출 중지
  }

  if (!passwordPattern.test(password)) {
    // <-- 수정: 비밀번호 형식 검증
    alert(
      "비밀번호는 최소 8자 이상, 최소 하나의 숫자, 문자, 특수문자를 포함해야 합니다."
    );
    return false; // <-- 수정: 검증 실패 시 폼 제출 중지
  }

  // 입력 검증이 통과하면 로그인 성공 알림 및 페이지 이동
  alert("로그인 성공!");
  window.location.href = "index.html"; // <-- 수정: 로그인 성공 시 페이지 이동
  return true;
}
