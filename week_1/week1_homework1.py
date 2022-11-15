input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    #변환시 변환 횟수를 저장해두기 위한 1과 0의 변수
    count_to_all_zero = 0
    count_to_all_one = 0
    #처음에 값에대한 변환을 넣어주기 위한것
    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string)-1):
        #첫번째와 두번째가 다르다면 변환해 줘야하니이런 조건문을 준다
        if string[i] != string[i+1]:
            #뒤의 숫자인 1을 다 0으로 바꿔줘야하는 것으로
            #변환을 마칠까지 하니 +1을 더해준다.
            if string[i+1] == '0':
                count_to_all_one += 1
            #뒤의 숫자인 0을 다 1으로 바꿔줘야하는 것으로
            #변환을 마칠까지 하니 +1을 더해준다.
            if string[i+1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)