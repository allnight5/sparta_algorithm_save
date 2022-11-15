seat_count = 9
vip_seat_array = [4, 7]

# 5번이라면 +1 -1 의 좌석에 앉을수 있으나 +2 -2자리에는 앉을수없다.
# 바꿔질수 있는 자리시에 앉아야 한다.
# 3번 좌석이 1번좌석으로 이동이 안된다 외냐? -2이기 때문이다.
# [1,2] = [1,2] [2,1] / [1,2,3] = [1,2,3] [1,3,2], [2,1,3]
# [1,2,3,4] = [1,2,3,4], [1,2,4,3] [1,3,2,4],[2,1,3,4] [2,1,4,3]
# 2자리라면 2, 3자리라면 3, 4자리라면 5개
# #
memo = {
    1:1,
    2:2
}

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    count =1
    index =0

    # while문을 이용하여 해보려고 했는데
    # 빠져나오는 조건문이 길어지고
    # if문을 넣어주니 시간복잡도가 증가하여
    # for문으로 다시 바꾸어 줬다.
    for i in fixed_seat_array:
        seat_index = i - 1
        result = fibo_dynamic_programming(seat_index-index, memo)
        count *= result
        index = seat_index+1

    result = fibo_dynamic_programming(total_count-index, memo)
    count *= result
    return count


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))