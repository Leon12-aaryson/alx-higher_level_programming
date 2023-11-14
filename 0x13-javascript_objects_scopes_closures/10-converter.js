exports.converter = function (base) {
  return function convertNumber (number) {
    if (number < base) {
      return number.toString(base);
    }
    return convertNumber(Math.floor(number / base)) + (number % base).toString(base);
  };
};
