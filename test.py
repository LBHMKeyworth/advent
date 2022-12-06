l1 = [1,2,3,4,4]
l2 = [2,4,7,8,4]

result = list(set(l1) & set(l2))

result_count = {}

for element in result:
    count = l1.count(element) + l2.count(element)
    result_count[element] = count



print (result_count)
