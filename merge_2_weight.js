/*
Merging 2 Packages

Given a package with a weight limit and an array arr of item weights,
how can you most efficiently find two items with sum of weights that equals the weight limit?

Your function should return 2 such indices of item weights or -1 if such pair doesn't exist.
What is the runtime and space complexity of your solution?
*/

function mergePackages(arr, limit) {
  const weights = {};
  for (let i = 0; i < arr.length; i++) {
    let weight = arr[i], comp = limit - weight;
    if (weights[comp]) {
       return [weights[comp], i];
    } else {
      weights[weight] = i;
    }
  }
  return [];
}
