def sum_to(a):
  sum = 0
  for num in range(1, a + 1):
    sum += num
  return sum

# print(sum_to(5))

def largest (nums):
  nums.sort()
  return nums[-1]

# print(largest([1, 2, 3, 7, 4, 3, 6, 0]))

def occurrences (str1, ltr):
  return str1.count(ltr)

# print(occurrences('toodle-hoo', 'o'))

