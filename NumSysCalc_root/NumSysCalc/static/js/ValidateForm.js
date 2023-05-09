const DigitToAlphas = new Map();
let value = 10;
for (w of "ABCDEFGHIJKLMNOPQRSTUVWXYZ") {
	DigitToAlphas.set(value++, w);
}
const CustomInput = document.getElementById("id_ss_5");
const CustomInput1 = document.getElementById("id_ss1_5");
const CheckBoxes = document.getElementById("line-checkbox");

function findNumInCheckbox(fst, snd) {
	let num = document.forms["CalcForm"].elements[fst].value;
	if (num == "-") {
		num = parseInt(document.forms["CalcForm"].elements[snd].value);
	} else {
		num = parseInt(num);
	}
	return num;
}

function ValidateCalcForm(event) {
	// to validate input#calc-input
	let strFilter, text;
	let ss = findNumInCheckbox("ss", "other_ss");
	let ss1 = findNumInCheckbox("ss1", "other_ss1");

	if (ss < 11) {
		strFilter = new RegExp(`^[0-${ss - 1},.-]*$`);
		text = `Число в ${ss}-ой системе счисления может содержать цифры от 0 до ${
			ss - 1
		}, а также точку для дробных чисел `;
	} else {
		strFilter = new RegExp(`^[\\dA-${DigitToAlphas.get(ss - 1)},.-]*$`);
		text = `Число в ${ss}-ой системе счисления может содержать цифры от 0 до 9, буквы от A до ${DigitToAlphas.get(
			ss - 1
		)}, а также точку для дробных чисел `;
	}
	const chkVal =
		document.forms["CalcForm"].elements["calc_input"].value.toUpperCase();
	if (ss == ss1) {
		alert(
			"В этом нет смысла! Зачем переводить число в его же систему счисления?"
		);
		document.forms["CalcForm"].elements["isRight"].value = '0';
	} else if (!strFilter.test(chkVal)) {
		alert(text);
		document.forms["CalcForm"].elements["isRight"].value = '0';
	} else if (chkVal == 0) {
		alert("Введите какое-нибудь число");
		document.forms["CalcForm"].elements["isRight"].value = '0';
	} else {
		document.forms["CalcForm"].elements["isRight"].value = '1';
	}

	if (document.forms["CalcForm"].elements["isRight"].value === '0') {
		event.preventDefault();
		if (navigator.userAgent.indexOf("YaBrowser") === -1) {
			window.history.back();
		}
	}
	//document.forms["CalcForm"].elements["calc-input"].focus();
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

function manageCustomOnput() {
	if (CustomInput.checked) {
		onOtherLeft();
	} else {
		offOtherLeft();
	}
	if (CustomInput1.checked) {
		onOtherRight();
	} else {
		offOtherRight();
	}
}

CheckBoxes.addEventListener("change", manageCustomOnput, false);
document.addEventListener("DOMContentLoaded", manageCustomOnput, false);
document.forms["CalcForm"].addEventListener('submit', ValidateCalcForm)

//function vievrezult() {
//  document.getElementById("vievrezult").style.display = "block";
//  document.getElementById("vievrezult").focus();
//}
