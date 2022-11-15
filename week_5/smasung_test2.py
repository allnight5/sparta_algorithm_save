#1.N*M의 보드를 만들며 편의상 1x1크기의 칸으로 나누어져있다
#1.가장 바깥행과 열은 모두 막혀져있고 보드에는 구멍이 하나있다.
#1-1.N*M의 행렬을 만들고 가장 마지막행, 열은 1로써서 막아두며
#1-2.보드 한칸에는 구멍을넣고 빨간구슬만 빼고 파란구슬은 들어갈수없게 해준다.
#2. 구슬은 중력을 이용하여 왼쪽 기울이기, 오른쪽 기울기등 위, 아래 , 좌, 우로 기울일수있다.
#2.구슬은 동시에 움직이며 한칸씩 차지하여 같은같에 있을수없다.
#2-1.구슬의 위치 배열을 만들어줘서 중복이 불가능하게 해준다.
#2-2.이동을 위한 변수를 만들어준다.
#3.보드가 이루어졌을때 10번이하고 빨간구슬을 구멍을 통해
#3 빼낼수 있는지 구하는 프로그램을 작성하라
#3-1.while문을 통하여 10까지 카운트하고 성공시 성공count를 실패시 실패했다는 -1을 리턴한다.
#4.보드의 행, 열의 길이는 3이상 10이다.
#4.보드 내에 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다.
#'.'은 빈 칸을 의미하고,
#'#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며,
#'O'는 구멍의 위치를 의미한다.
#'R'은 빨간 구슬의 위치,
#'B'는 파란 구슬의 위치이다.
#위아래옆 이동시 나올수 있는 위치를 다 구해야 하기때문에 BFS를 응용하여 해결해야한다.

from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
#  오른쪽,아래,왼쪽, 위 기울기
#    왼, 위,오른,위쪽 이동
dr = [-1, 0, 1,  0]
dc = [ 0, 1, 0, -1]
def move_hole_or_wall(r, c, diff_r, diff_c, game_map):
    move_count = 0

    while game_map[r+diff_r][c+diff_c] != '#' and game_map[r][c] != 'O':
        r += diff_r
        c += diff_c
        move_count += 1
    return r, c, move_count

#          n사이즈  m사이즈   n사이즈   m사이즈이다
#visited[red_row][red_col][blue_row][blue_col]
#4차원 배열 구상도blue_col이 가장 안쪽이라서 m을 곱해준뒤 for을 n만큼해주는것이다
def is_available_to_take_out_only_red_marble(game_map):
    #map형태의 배열일시 열, 행의 길이를 구하는방법
    n, m= len(game_map),len(game_map[0])
    visited = [[[[False] * m for _ in range(n)]for _ in range(m)]for _ in range(n)]
    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j
    #여러개 넣을때에는 소괄호를 쓰고 입력해줘야한다.
    #뒤에 1을 넣어준 이유는 탐색한 숫자를 넣어줘야하기때문에
    #지금 1회 탐색했으니 1을 넣어주는것이다.
    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()  # FIFO
        if try_count > 10:  # 10 이하여야 한다.
            break

        for i in range(4):
            next_red_row, next_red_col, r_count = move_hole_or_wall(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, b_count = move_hole_or_wall(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[next_blue_row][next_blue_col] == 'O':  # 파란 구슬이 구멍에 떨어지지 않으면(실패 X)
                continue
            if game_map[next_red_row][next_red_col] == 'O':  # 빨간 구슬이 구멍에 떨어진다면(성공)
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col:  # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
                if r_count > b_count:  # 이동 거리가 많은 구슬을 한칸 뒤로
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]
            # BFS 탐색을 마치고, 방문 여부 확인
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다



game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", "R", "#", "B", "#"],
    ["#", ".", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", ".", "#"],
    ["#", "O", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))