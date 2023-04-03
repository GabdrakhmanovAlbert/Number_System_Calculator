/**
 *  find numbers after symbol and before symbol
 * if sym == '%', s == '927+837*320%28+86-73' => {before_num:'320', after_num:'28', bef_i:8, aft_i:13}
 * @param ind {number} index of char, which is splitting two nums
 * @param s {string} string, where looking for '{num}{char}{num}'
 */
function findBeforeAfterSym(ind, s) {
	let bef_i = ind;
	let [bef_num, aft_num] = ["", ""];
	while (digits.includes(s[ind + 1]) || s[ind + 1] == ".") {
		aft_num += s[++ind];
	}
	while (digits.includes(s[bef_i - 1]) || s[bef_i - 1] == ".") {
		bef_num = s[--bef_i] + bef_num;
	}
	return {
		before_num: bef_num,
		after_num: aft_num,
		bef_i: bef_i,
		aft_i: ind,
	};
}

/**
 * convert math expression like this "50%+100%" -> "0.5+0.5"
 * removes all "%" and translate to func eval
 *@param s {string} - math expression
 */
function percToEval(s) {
	if (s.includes("%%")) return "";
	let perc_ind;
	while ((perc_ind = s.indexOf("%")) != -1) {
		if (perc_ind == 0) return "";
		let { before_num, after_num, bef_i, aft_i } = findBeforeAfterSym(
			perc_ind,
			s
		);

		if (after_num) {
			let res = (Number(after_num) * Number(before_num)) / 100;
			s = s.slice(0, bef_i) + String(res) + s.slice(aft_i + 1);
		} else if (
			(s[bef_i - 1] == "+" || s[bef_i - 1] == "-") &&
			digits.includes(s[bef_i - 2]) &&
			(s[aft_i + 1] == "+" || s[aft_i + 1] == "-" || s[aft_i + 1] == undefined)
		) {
			let perc100 = eval(s.slice(0, bef_i - 1));
			let res = (perc100 * Number(before_num)) / 100;
			s = String(perc100) + s[bef_i - 1] + String(res) + s.slice(aft_i + 1);
		} else {
			let res = Number(before_num) / 100;
			s = s.slice(0, bef_i) + String(res) + s.slice(aft_i + 1);
		}
	}
	return s;
}

/**
 * evaluate "6^2" from str and inserts into cur_place
 * @param {string} str
 * @returns {string} "87*2^10+34" -> "87*1024+34"
 */

function solveExponantion(str) {
	let ind;
	while ((ind = str.lastIndexOf("^")) != -1) {
		const { before_num, after_num, bef_i, aft_i } = findBeforeAfterSym(
			ind,
			str
		);
		str =
			str.slice(0, bef_i) +
			String(before_num ** after_num) +
			str.slice(aft_i + 1);
	}
	return str;
}

//! tests needed
/**
 * if brackets not valid return ""
 * if user: "6(56-76)" -> "6*(56-76)"
 * @param {string} s
 * @returns {string}
 */
function wokrWithBrackets(s) {
	let brackets = 0;
	const insertMult = [];
	for (let i in s) {
		if (s[i] == "(") {
			brackets++;
			if (digits.includes(s[i - 1])) insertMult.push(i);
		} else if (s[i] == ")") {
			brackets--;
			if (digits.includes(s[i + 1])) insertMult.push(i + 1);
		}
		if (brackets < 0) return "";
	}
	if (brackets != 0) return "";
	for (let i of insertMult) {
		s = s.slice(0, i) + "*" + s.slice(i);
	}
	return s;
}

/**
 * convert userInputStr for Eval of JS
 * @param {string} str
 * @returns string for eval: from "27+10%-67x2+2^10" -> "27+2.7-67*2+1024"
 */
function editToEval(str) {
	// translate string on screen, to the func "eval"
	str = wokrWithBrackets(str);
	// now multiplying works
	str = str.replaceAll("x", "*");
	// now exponantion works
	str = solveExponantion(str);
	// now % works...
	str = percToEval(str);
	return str;
}
