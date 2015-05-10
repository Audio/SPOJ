process.stdin.on('data', chew);

var remainingLines;
function chew(data) {
    var lines = data.toString().trim().split("\n");
    for (var i = 0; i < lines.length; ++i) {
        if (typeof remainingLines === 'undefined') {
            remainingLines = Number(lines[i]);
        } else {
            on(lines[i]);
            if (--remainingLines < 1) process.exit(0);
        }
    }
}

function on(line) {
    var n = Number(line);
    console.log(solve(n));
}

var cache = {};
function solve(n) {
    var min = 0,
        max = Math.floor(Math.sqrt(n)),
        squares = cache[max];

    if (!squares) {
        squares = [];
        for (var i = min; i <= max; ++i) {
            squares.push(i * i);
        };
        cache[max] = squares;
    }

    for (var s = 0, l = squares.length; s < l; ++s) {
        for (var t = s; t < l; ++t) {
            if (squares[s] + squares[t] == n) return 'Yes';
        }
    }

    return 'No';
}

