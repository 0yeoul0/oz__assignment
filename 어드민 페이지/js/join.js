function validateForm() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  var confirmPassword = document.getElementById("confirm-password").value;
  var email = document.getElementById("email").value;

  if (!username || !password || !confirmPassword || !email) {
    alert("모든 필드를 입력해 주세요.");
    return false;
  }

  if (password !== confirmPassword) {
    alert("비밀번호와 비밀번호 확인이 일치하지 않습니다.");
    return false;
  }

  alert("가입 성공!");
  return true;
}
