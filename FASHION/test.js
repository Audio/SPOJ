require('../test.js')({
    validator: function(input, output) {
        // remove the first input line
        input.shift();

        // also remove the first of every three following lines
        // and reindex the input array
        if (input.length % 3 !== 0) throw Error('Invalid input');
        var freeIndex = 0;
        for (var toDelete = 0; toDelete < input.length; toDelete += 3) {
            delete input[toDelete];
            input[freeIndex++] = input[toDelete+1] + " \\n " + input[toDelete+2];
        }
        input.length = freeIndex;
    }
});

