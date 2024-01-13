#!/usr/bin/node
/**
 * Convert to different bases
 */

exports.converter = function (base) {
  function convert (number) {
    return number.toString(base);
  }
  return convert;
};
