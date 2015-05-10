var ttl, rl = require('readline').createInterface({input: process.stdin, terminal: false});
rl.on('line', function(n) {
    n = Number(n);
    if (!ttl) return ttl = n;
    console.log(solve(n));
    if (--ttl < 1) process.exit(0);
});

var cache = {}, max;

function solve(n) {
    if (cache[n]) return cache[n];

    max = Math.floor(Math.sqrt(n));

    for (var i = 0; i <= max; ++i) {
        var isInt = Math.sqrt(n - i * i) % 1 == 0;
        if (isInt) return cache[n] = 'Yes';
    }

    return cache[n] = 'No';
}

