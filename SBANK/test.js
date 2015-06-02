require('../test.js')({
    validator: function(input, output) {
        var firstTask = input[0].split(" \\n ");
        var tasksCount = Number(firstTask.shift());
        input[0] = firstTask.join(" \\n ");

        if (tasksCount !== input.length) {
            throw Error('Invalid tasks length (should be ' + tasksCount +
                        ', but found ' + input.length + ')');
        }
    },
    separator: "\n\n"
});
