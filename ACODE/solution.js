var rl = require('readline').createInterface({input: process.stdin, terminal: false});
rl.on('line', function(n) {
    if (n === "0") process.exit(0);
    console.log(count(n));
});

function count(n) {
    var sum = 1; // a case where all numbers are separated (e.g. all digits and 10, 20)

    var doubles = findDoubles(n);
    if (!doubles.length) return sum;

    var cache = {}, l, r, ret;

    for (l = doubles.length, d = l - 1; d >= 0; d--) {
        ret = 1;
        for (r = d + 1; r < l; r++) { // all doubles to the right
            if (doubles[d] + 1 === doubles[r]) continue; // intersection
            ret += cache[r];
        }
        sum += cache[d] = ret;
    }

    return sum;
}

// return [0, 2, 3] for n equals "25114"
function findDoubles(n) {
    var doubles = [], i, nexti;

    for (i = 0; i < n.length - 1; ++i) {
        nexti = n.charCodeAt(i+1);
        if (
            (
                n[i] === "1" &&
                nexti >= 49 && // "1"
                nexti <= 57 && // "9"
                n[i+2] !== "0"
            ) || (
                n[i] === "2" &&
                nexti >= 49 && // "1"
                nexti <= 54 && // "6"
                n[i+2] !== "0"
            )
        ) doubles.push(i);
    }

    return doubles;
}

