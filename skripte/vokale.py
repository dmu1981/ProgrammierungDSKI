def count_vokale(text):
  vokale = ['a', 'e', 'i', 'o', 'u']
  text = text.lower()
  count = 0
  
  for vokal in vokale:
    count += text.count(vokal)
  
  return count

for x in map(count_vokale, ['apple', 'banana', 'cherry']):
  print(x)