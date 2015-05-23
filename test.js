var assert = require('assert');
var cwd = process.cwd();
var fs = require('fs');
var exec = require('child_process').exec;

function getTestFiles() {
    var files = [];

    if (fs.existsSync(cwd + '/solution.go')) {
        files.push({
            solution: 'solution.go',
            command: 'go run'
        });
    }

    if (fs.existsSync(cwd + '/solution.py')) {
        files.push({
            solution: 'solution.py',
            command: 'python3'
        });
    }

    if (fs.existsSync(cwd + '/solution.js')) {
        files.push({
            solution: 'solution.js',
            command: 'node'
        });
    }

    if (fs.existsSync(cwd + '/solution.rb')) {
        files.push({
            solution: 'solution.rb',
            command: 'ruby'
        });
    }

    return files;
}

var validators = {
    equal: function(input, output) {
        if (input.length !== output.length) {
            throw Error('Input/output length mismatch (' + input.length +
                        ' vs ' + output.length + ')');
        }
    },
    prefix: function(input, output) {
        if (input.length - 1 !== output.length) {
            throw Error('Input/output length mismatch (' + input.length +
                        ' vs ' + output.length + ')');
        }
        if (input.length - 1 !== Number(input[0])) {
            throw Error('Input length mismatch (expected ' + input[0] +
                        ' test cases, but found ' + (input.length - 1) + ')');
        }
        input.shift(); // remove the first input line
    },
    suffix: function(input, output) {
        if (input.length - 1 !== output.length) {
            throw Error('Input/output length mismatch (' + input.length +
                        ' vs ' + output.length + ')');
        }
        if (input[input.length - 1] !== '0') {
            throw Error('The last input line must be zero (0)');
        }
        input.pop(); // remove the last input line
    }
};

module.exports = function(opts) {

    // default values
    opts = opts || {};
    opts.validator = opts.validator || 'equal';
    opts.separator = opts.separator || "\n";

    // load and parse io files
    function separate(lines) {
        return lines.trim().split(opts.separator);
    }
    var input  = separate( fs.readFileSync(cwd + '/input.txt',  {encoding: 'utf8'}) );
    var output = separate( fs.readFileSync(cwd + '/output.txt', {encoding: 'utf8'}) );

    // validate io files
    if (typeof opts.validator === 'function') {
        opts.validator(input, output);
    } else {
        validators[opts.validator](input, output);
    }

    var files = getTestFiles();
    if (!files.length) throw Error('No solutions found');

    for (var f = 0; f < files.length; ++f) {
        var suiteTitle = cwd.split('/').reverse()[0] + ' - ' + files[f].solution;
        describe(suiteTitle, function() {

            // run solution app
            var results,
                command = files[f].command + ' ' + files[f].solution + ' < input.txt';

            before(function(done) {
                exec(command, function(e, out, err) {
                    if (e) return done(e);
                    if (err) return done(err);
                    results = separate(out);
                    done();
                });
            });

            // register tests
            for (var i = 0, max = input.length; i < max; ++i) {

                (function(i) {
                    it(input[i], function() {
                        var msg = 'Expected "' + output[i] + '", but got "' + results[i] + '" instead.';
                        assert.equal(results[i], output[i], msg);
                    });
                })(i);

            }
        });
    }

};
