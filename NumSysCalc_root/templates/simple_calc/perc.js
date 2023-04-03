import { digits } from "./simple_calc";

/**
 *  find numbers after symbol and before symbol
 * if sym == '%', s == '927+837*320%28+86-73' => {before_num:'320', after_num:'28', bef_i:8, aft_i:13}
 * @param ind {number} index of char, which is splitting two nums
 * @param s {string} string, where looking for '{num}{char}{num}'
 */
export function findBeforeAfterSym(ind, s) {
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

// let { before_num, after_num } = findBeforeAfterSym(
// 	15,
// 	"1000-839+332234%9237*98+93*2*98+93*2"
// );
// console.log(before_num, after_num);

/**
 * convert math expression like this "50%+100%" -> "0.5+0.5"
 * removes all "%" and translate to func eval
 *@param s {string} - math expression
 */
export function percToEval(s) {
	if (s.includes("%%")) return "";
	let perc_ind;
	while ((perc_ind = s.indexOf("%")) != -1) {
		if (perc_ind == 0) return "";
		let { before_num, after_num, bef_i, aft_i } = findBeforeAfterSym(
			perc_ind,
			s
		);

		// console.log(s);
		// console.log(before_num);
		// console.log(after_num);
		// console.log(bef_i);
		// console.log(aft_i);

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

// console.log(eval(percToEval("1000-839+332234%9237*98+93*2*98+93*2"))); // 3007487123.84
// console.log(percToEval("50%50")); // 25
// console.log(percToEval("300%200")); // 600
// console.log(percToEval("8+1%+9*5+78%")); // 53.08+41.4024
// console.log(percToEval("50%+100%")); // 0.5+0.5 == 1
// console.log(percToEval("8*50%4+2")); // 18
// console.log(percToEval("10+16%*10")); // 10+0.16*10 == 11.6
// console.log(percToEval("100%-100%")) // 1-1
// console.log(percToEval("-100%+827+87%/67*90+67*2-1000")) // -1+827+0.87/67*90+67*2-1000 == -38.83134328358
// console.log(percToEval('%451*46')) // ''
// console.log(percToEval("85%56+926%94")) // 47.6+870.44 == 918.04
// console.log(percToEval("65%624%6458%34%2%199")); // 354.452444736


// console.log(percToEval('830-839+332234%9237*98+93**90'))
// console.log(percToEval("100%987+69-59*23%100+89**3-50%")); // 704668-352334
// console.log(eval(percToEval("100%987+69-59*23%100+89**3-50%*100%"))); // 704667.5
// console.log(eval(percToEval("2**10+86-540+35%-56%+3000-50%*8"))); // 3334,58
// console.log(percToEval("8*50%4**2")); // 64
// console.log(percToEval('8*9+8%10**2**2'))
// console.log(percToEval('9*(5+1)%'))  // 0.54
// console.log(eval(percToEval('100%987+69-59*23%100+89**3-(50*100)%'))) // 704618
// console.log(eval(percToEval('100%987+69-59*23%100+(89**3-50%)*100%'))) // 352183,5
