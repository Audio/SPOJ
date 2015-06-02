var fs = require('fs');

function includesTestFile(dirname) {
    return fs.existsSync(__dirname + '/' + dirname + '/test.js');
}

var dirs = fs.readdirSync(__dirname).filter(includesTestFile);

console.log('Found ' + dirs.length + ' solutions.');

dirs.forEach(function(dir, i) {
    process.chdir(__dirname + '/' + dir);
    require(__dirname + '/' + dir + '/test.js');
});
