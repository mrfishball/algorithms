'''
Array Index & Element Equality

Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i.
Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

Examples:

input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i]
'''

def index_equals_value_search(arr):
  start = 0;
  end = len(arr) - 1

  while (start <= end):
    mid = (start + end) / 2
    if (arr[mid] == mid):
      return mid
    elif (mid > arr[mid]):
      start = mid + 1
    else:
      end = mid - 1
  return -1
