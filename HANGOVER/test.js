require('../test.js')({
    validator: function(input, output) {
        if (input.length - 1 !== output.length) {
            throw Error('Input/output length mismatch');
        }
        if (input[input.length - 1] !== '0.00') {
            throw Error('The last input line must be zero (0.00)');
        }
        input.pop(); // remove the last input line
    }
});
