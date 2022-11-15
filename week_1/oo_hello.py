input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for i in array:
        for j in array:
            if i < j:
                break
        else:
            return i


result = find_max_num(input)
print(result)
