const path = require('path');

module.exports = {
    entry: '../src/cytoscape-config.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js',
    },
};
