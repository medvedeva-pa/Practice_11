lst1 = []
lst2 = []
out = []
i = j = 0

while i < len(lst1) and j < len(lst2):
  if lst1[i] < lst2[j]:
    out.append(lst1[i])
    i += 1
  else:
    out.append(lst2[j])
    j += 1
while i < len(lst1):
  out.append(lst1[i])
  i += 1
while j < len(lst2):
  out.append(lst2[j])
  j += 1
  
out