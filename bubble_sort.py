lst = []

for j in range(len(lst) - 1):
  for i in range(len(lst) -1):
    if lst[i] > lst[i + 1]:
       lst[i], lst[i + 1]=lst[i + 1], lst[i]
     
# т.к. алгоритм выполняет итерацию n элементов внутри итерации n элементов, то сложность алгоритма равна О(n^2)