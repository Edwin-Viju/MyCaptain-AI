def positives(numbers):
    list = []
    for num in numbers:
        if num > 0:
            list.append(num)
    return list

list1 = [12, -7, 5, 64, -14]
po1 = positives(list1)
print("Output:", po1)

list2 = [12, 14, -95, 3]
po2 = positives(list2)
print("Output:", po2)
