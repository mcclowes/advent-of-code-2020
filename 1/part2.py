text_file = open("input.txt", "r")
lines = text_file.read().split('\n')
text_file.close()

year = 2020

def isInArr(n):
  print(n)
  if(n == None):
    return False
    
  if str(n[1]) in lines:
    return True

  return False

def getCounterpart(x):
  target = year - int(x)

  counterparts = next(
    filter(
      lambda x: isInArr(x) == True, 
      map(lambda x: getSubCounterparts(target, x), lines)
    ), 
    None
  )
  
  if counterparts == None:
    return None

  return [ int(x), counterparts[0], counterparts[1] ]

def getSubCounterparts(target, y):
  return [ int(y), target - int(y) ]

target = next(
  filter(
    lambda x: isInArr(x) == True, 
    map(getCounterpart, lines)
  ), 
  None
)

print("We found:")
print(target)
print("Sum:")
print(str(target[ 0] + target[1] + target[2]))
print("Product:")
print(str(target[0] * target[1] * target[2]))