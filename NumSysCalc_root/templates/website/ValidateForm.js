function ValidateCalcForm(theForm) {
  let strFilter;
  let text;
  let error = 0;

  let i = parseInt(document.forms["CalcForm"].elements["ss"].value);

  if (i == 1) {
    strFilter = /^[0-1,.-]*$/;
    text =
      "Двоичное число может содержать только цифры 0 и 1, а также точку для дробных чисел";
  } else if (i == 2) {
    strFilter = /^[0-2,.-]*$/;
    text =
      "Троичное число может содержать только цифры 0,1 и 2, а также точку для дробных чисел";
  } else if (i == 3) {
    strFilter = /^[0-7,.-]*$/;
    text =
      "Восьмеричное число может содержать только цифры 0 - 7, а также точку для дробных чисел";
  } else if (i == 4) {
    strFilter = /^[0-9,.-]*$/;
    text =
      "Десятичное число может содержать только цифры 0 - 9, а также точку для дробных чисел";
  } else if (i == 5) {
    strFilter = /^[0-9a-fA-F,.-]*$/;
    text =
      "Шестнадцатиричное число может содержать только цифры 0 - 9, буквы A,B,C,D,E,F а также точку для дробных чисел";
  } else if (i == 6) {
    strFilter = /^[0-9a-fA-Z,.-]*$/;
    text =
      "Число может содержать только цифры 0 и 9, буквы A-Z а также точку для дробных чисел";
  }

  if (
    (i <= 6 &&
      i == parseInt(document.forms["CalcForm"].elements["ss1"].value)) ||
    (i == 7 &&
      document.getElementById("left-other").value ==
        document.getElementById("right-other").value)
  ) {
    alert(
      "В этом нет смысла! Зачем переводить число в его же систему счисления?"
    );
    error = 1;
  }

  const chkVal = document.forms["CalcForm"].elements["calc-input"].value;
  if (!strFilter.test(chkVal)) {
    alert(text);
    document.forms["CalcForm"].elements["calc-input"].focus();
    error = 1;
  }
  if (document.forms["CalcForm"].elements["calc-input"].value == 0) {
    document.forms["CalcForm"].elements["calc-input"].focus();
    error = 1;
    alert("Введите какое-нибудь число");
  }
  if (error != 1) document.forms["CalcForm"].submit();
}

// to appear a form of another number of number system
function offOtherLeft() {
  document.getElementById("left-other").style.display = "none";
}

function offOtherRight() {
  document.getElementById("right-other").style.display = "none";
}
function onOtherRight() {
  document.getElementById("right-other").style.display = "block";
}
function onOtherLeft() {
  document.getElementById("left-other").style.display = "block";
}
function vievrezult() {
  document.getElementById("vievrezult").style.display = "block";
  document.getElementById("vievrezult").focus();
}
