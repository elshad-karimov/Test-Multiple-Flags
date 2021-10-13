# Different ways to test multiple flags at 
# once in Python
a, b, c = 0, 1, 0

if a == 1 or b == 1 or c == 1:
  print('passed')

if 1 in (a, b, c):
  print('passed')

# These only test for truthiness:
if a or b or c:
  print('passed')

if any((a, b, c)):
  print('passed')

  


