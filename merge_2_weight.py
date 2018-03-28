'''Merging 2 Packages

Given a package with a weight limit and an array arr of item weights,
how can you most efficiently find two items with sum of weights that equals the weight limit?

Your function should return 2 such indices of item weights or -1 if such pair doesn't exist.
What is the runtime and space complexity of your solution?
'''

def mergePackages(arr, limit):
    weights = set()
    for i in range(0, len(arr)):
        weight = arr[i]
        comp = limit - weights
        if(comp in weights):
            return [weights[comp], i]
        else:
            weights.add(i)
    return []
