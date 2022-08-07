import math

def power(a,b):
  global n
  if b == 0:
    return 1
  elif b == 1:
    return a
  elif b == 2:
    n += 1
    return a * a
  elif b % 2 == 0:
    n += 1
    factor = power(a, b/2)
    return factor * factor
  elif b % 2 == 1:
    n += 2
    half = math.floor(b/2)
    factor = power(a, half)
    return factor * factor * a

def original_power(a,b):
  global original_n
  result = 1
  for i in range(b):
    result = result * a
    original_n += 1
  return result

def number_of_multiplications(b):
  result = 0
  if b == 2:
    result += 1
  elif b % 2 == 0:
    result += 1
    result += number_of_multiplications(b//2)
  elif b % 2 == 1:
    result += 2
    result += number_of_multiplications(b//2)
  return result


  

a=2
b=23
original_n = 0
n = 0


original_answer = original_power(a,b)
print(original_answer)
print(original_n)
answer = power(a,b)
print(answer)
print(n)
number = number_of_multiplications(b)
print(number)