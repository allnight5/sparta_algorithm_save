#1.도시를 NxN담을도시 행렬을 만들고 (r,c)는 1부터 시작한다.
#2.도시의 치킨거리는 모든집의 치킨거리의 합이다
#3.임의의 두칸 (r1,c1)과 (r2,c2)의 거리는 |r1-r2|+|c1-c2|로구한다.
#4.0은 빈칸, 1은 집, 2는 치킨집이다.
#5.최대치킨집 M개를 구해라
#5-1.BFS를 이용하여 각 치킨집마다의 배열에 거리를 입력하고
#5-1.M의 개수를 1씩 증가시키며 어느 지점까지 있을때 거리가 적은지를 더하면 될것같다.
from itertools import combinations
import itertools, sys

n = 5
m = 2

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = []
    home_location_list = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i, j])
            if city_map[i][j] == 2:
                chicken_location_list.append([i, j])
    #combinations조합이라는 의미를 지닌다
    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    min_distance_of_m_combinations = sys.maxsize

    for chicken_location_m_combination in chicken_location_m_combinations:
        distance =0
        for home_r, home_c in home_location_list:
            min_home_chicken_distance = sys.maxsize
            for chicken_location in chicken_location_m_combination:
                min_home_chicken_distance = min(
                    min_home_chicken_distance, abs(home_r -chicken_location[0])+abs(home_c-chicken_location[1])
                )
            distance += min_home_chicken_distance
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, distance)
    return min_distance_of_m_combinations



# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!합니다!