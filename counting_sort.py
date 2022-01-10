list = []
count_list = [0 for i in range(max(list) + 1)]
out = []

for i in list:
  count_list[i] += 1
for i in range(len(count_list)):
  if count_list[i] != 0:
    out += [i for j in range(count_list[i])]
    
    
# алгоритм осуществляет две итерации по n элементов для списков и итерацию k элементов словаря, 
# поэтому сложность равна О(n + n + k) = O(2n + k) = О(n + k)