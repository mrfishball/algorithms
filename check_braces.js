/*
An algorithm to check if the brackets/parentheses are in balance.
*/

function check_braces (expr) {
  if (expr.length % 2 != 0) {
    return false;
  }

  const exprSet = new Set();
}
