#!/usr/bin/node

const fs = require('fs');

/**
 * Check if correct number of command-line arguments are provided
 */
if (process.argv.length !== 5) {
  process.exit(1);
}

const concatfiles = fs.readFileSync(process.argv[2], 'utf8') + fs.readFileSync(process.argv[3], 'utf8');

// Write to the third file (arg)
fs.writeFileSync(process.argv[4], concatfiles);
