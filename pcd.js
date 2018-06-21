const fs = require('fs');
const rl = require('readline');

const skipMath = ['.git', 'node_modules', 'vendor'];

const choose = path => fs.stat(path, (err, stats) => stats.isDirectory() ? descend(path) : parse(path));

const descend = path => fs.readdir(path, (err, files) => files
    .filter(f => !(f in skipMath))
    .map(part => `${path}/${part}`)
    .forEach(choose)
)

const parse = path => {
    let foundClass = null;

    if (!path.endsWith('.php')) return;

    rl.createInterface({ input: fs.createReadStream(path) }).on('line', l => {
        if (foundClass && l.match(new RegExp(`.*function +?${foundClass}[ ,\\(]+?`))) {
            console.log(path, `Class: ${foundClass}`)
            foundClass = null;
        } else {
            [, found] = l.match(/^[{ ,\t}]*?class +?(\w[^{ ,\\()}]*)/) || [null, null]

            if (found) foundClass = found;
        }
    })
}

choose(process.argv[2]);