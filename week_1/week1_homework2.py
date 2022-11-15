
in_input = 20

def decimal(input):
    prime_list =[]
    for n in range(2, input+1):
        for i in prime_list:
            if n%i == 0 and i*i<=n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = decimal(in_input)
print(result)