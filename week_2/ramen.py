import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

#우선은 stock과 k를 비교한다 stock이 k와 같거나 크다면 1을 반환한다
#stock이 작다면 순서대로 stock의 갯수보다 지급일수가 많이 남았다면 지급일수
#만큼 들어가서 비교해본 후 지급일에 따른 공급수 k와 비교하고 지급일만큼 들어갔는데
#마지막까지 비교해도 안된다면 들어간만큼 모든 지급일을 넣어둔뒤
#최댓값을 stock에 더해준다.
#

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    count =0
    cut_date=0
    heap = []

    while stock <= k :
        while cut_date < len(dates) and stock >= dates[cut_date]:
            heapq.heappush(heap, -supplies[cut_date])
            cut_date += 1

        count += 1
        heapop = heapq.heappop(heap)
        stock += -heapop

    return count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 5 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 30, 60, 65, 70], [20, 7, 40, 5, 20, 50], 140))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))