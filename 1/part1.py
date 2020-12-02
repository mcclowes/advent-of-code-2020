text_file = open("input.txt", "r")
lines = text_file.read().split('\n')
text_file.close()

year = 2020

def counterpart(n):
  return [ int(n), year - int(n) ]

def isInArr(n):
  if str(n[1]) in lines:
    return True

  return False

linesWithCounterparts = map(counterpart, lines)

target = next(filter(lambda x: isInArr(x) == True, linesWithCounterparts), None)

print("We found:")
print(target)
print("Sum:")
print(str(target[0] + target[1]))
print("Product:")
print(str(target[0] * target[1]))