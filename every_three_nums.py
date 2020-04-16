# Create a function that returns a list of every third number between start and 100 (inclusive).
# codecademy.com

def every_three_nums(start):
  nums = []
  counter = start
  
  while counter <= 100:
    nums.append(counter)
    counter+=3
  return nums

# example outputs
print(every_three_nums(1))
print(every_three_nums(91))
