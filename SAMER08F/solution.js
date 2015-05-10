var rl = require('readline').createInterface({input: process.stdin, terminal: false});
rl.on('line', function(n) {
    n = Number(n);
    if (!n) process.exit(0);
    console.log(solve(n));
});

var cache = {}, sum;

function solve(n) {
    if (cache[n]) return cache[n];

    sum = 0;
    do {
        sum += n * n;
    } while (--n > 0);

    return cache[n] = sum;
}

