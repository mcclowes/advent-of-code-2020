text_file = open("input.txt", "r")
lines = text_file.read().split('\n')
text_file.close()

def counterpart(n):
  return [ int(n), 2000 - int(n) ]

def isInArr(n):
  if str(n[1]) in lines:
    return True

  return False

linesWithCounterparts = map(counterpart, lines)

target = next(filter(lambda x: isInArr(x) == True, linesWithCounterparts), None)

print("We found:")
print(target)
print("Sum:")
print("2000")
print("Product:")
print(str(target[0] * target[1]))