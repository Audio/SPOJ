var rl = require('readline').createInterface({input: process.stdin, terminal: false});
rl.on('line', function(n) {
    if (n === "0") process.exit(0);
    console.log(count(n));
});

function count(n) {
    // console.log(n)
    var ret = 1; // a case where all numbers are separated (e.g. all digits and 10, 20)

    var doubles = findDoubles(n);
    if (!doubles.length) return ret;

    for (var right, d = 0, l = doubles.length; d < l; d++) {
        right = n.substring(doubles[d] + 2);
        ret += right.length ? count(right) : 1;
    }

    return ret;
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

