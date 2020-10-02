# Counting Sort

Counting sort is a sorting techniques based on keys between a specific range.

It works by counting the number of objects having distinct key values. Then doing some arithmetic to calculate the position of each object in the output sequence.

For simplicity, consider data in ragne of 0 to 9

```
| 1 | 4 | 1 | 2 | 7 | 5 | 2 |
```

Step 1:
- Create a count array to store the count of each unique object

```
  0   1   2   3   4   5   6   7   8   9
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
```
    initally, the count of all elements is zero

Step 2:
- Count each element in the given array and place the count at the appropriate index

```
Index:
  0   1   2   3   4   5   6   7   8   9
| 0 | 2 | 2 | 0 | 1 | 1 | 0 | 1 | 0 | 0 |
```

Step 3:
- Modify the count array by adding the previous counts

```
Index:
  0   1   2   3   4   5   6   7   8   9
| 0 | 2 | 2 | 0 | 1 | 1 | 0 | 1 | 0 | 0 |
     |____|
      2 + 2


Index:
  0   1   2   3   4   5   6   7   8   9
| 0 | 2 | 4 | 4 | 5 | 6 | 6 | 7 | 7 | 7 |
```

Step 3:
Since we have seven inputs we create an array with seven places

```
  1   2   3   4   5   6   7
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
```

Step 4:
We place the objects in the correct positions and decrease the count by one.

```
| 1 | 4 | 1 | 2 | 7 | 5 | 2 |


Index:

  0 | 1 | 2   3   4   5   6   7   8   9
| 0 | 2 | 4 | 4 | 5 | 6 | 6 | 7 | 7 | 7 |

  1   2   3   4   5   6   7
| 1 | 1 | 2 | 2 | 4 | 5 | 7 |

```

Explaining the code
```
def countSort(arr):
    len(arr)
    
```