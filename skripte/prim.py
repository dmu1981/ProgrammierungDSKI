def isPrim(zahl):
  for teiler in range(2, zahl):
    if zahl % teiler == 0:
      return False
    
  return True

for primzahlen in filter(isPrim, range(100)):
  print(primzahlen)