#1.새로운 게임은 크기가 N*N체스판에서 실행되고 사용하는 말의개수는 K이다
#/1-1.N*N형태의 map이나 2중 리스트를 만들어준다.
#/1-2.변수 K를 리스트형태로(행,열,이동방향) 선언해준다
#말은 원판모양이고 하나의 말 위에 다른말을 올릴수있다.
#2.체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠되어있다.
#2.N*N형태의 체스판 각칸에 0.흰색, 1.빨간색, 2.파란색을 넣어준다
#3.말 K를 놓고 시작하는데 말은 1~K번까지 번호가 매겨져 있고 이동방향도 미리 정해져있다.
#3.이동방향은 오른쪽,왼쪽, 위, 아래 (0,1,2,3)순으로 의미를 같는다.
#/3-1.말의 번호와 방향을 저장해 두는 변수를 만들어준다.
#/3-2.방향에 따른 이동시 변하는 값을 x와 y축변수로 만들어준다.
#/3-3.말의 방향이동때 변하는 값을 계산하여 함수로 만들어준다.
#/3-4.말의 방향을 반대로 해주는 함수를 만든다.
#4.턴한번은 1~K번 말까지 순서대로 이동시키는 것으로 한말이 이동할때 위에 올려져 있는 말도
#4.함께 이동한다. 말의 이동방향에 있는 칸에 따라서 이동이 다르며 아래와 같다.
#4.턴이 진행되던중에 말이 4개이상 쌓이는 순간 게임이 종효된다.
#/4-1. 1~K까지 순서대로 이동하지만 예시로 1~9번이있으나 1번에 말위에 8번이 올려져있을경우
#/4-1. 8번도 1번 다음으로 이동을 시작한다.1번 아래에 3번이 있고 1번위에 4번이있을경우
#/4-1. 1번은 이동시 4번만 데리고 이동한다.
#/4-2. 앞이 벽이거나 파란색이라면 방향을 반대로 바꾸어 한칸 이동한다.
#5. 흰색인 경우 이동하려는 칸에 말이 있다면 가장위에 A번 말을 올려놓는다
#5. A,B,C로 쌓여있는경우 이동하려는 칸에 D,E가 있다면 D,E,A,B,C가 된다
#5-1. 이동칸이 흰색일 경우 스택형태로 병합한다.
#6.빨간색인 경우 A번 말과 그 위에 쌓여있는 말의 순서를 반대로 바꾼다.
#6. A,B,C가 이동하려는 칸에 E,C,B가 있다면 E,C,B,C,B,A가된다
#6-1.스택을 이용하여 넣고 꺼내준뒤 리스트에 넣어 반환해준다.
#7.다음칸이 파란색인 경우 A번말의 이동방향을 반대로 하고 한칸 이동한다. 밯양을 반대로
#7.바꾼후에 이동하려는 칸이 파란색일 경우 이동하지 않고 가만히 있는다.
#8.체스판을 벗어나는경우에는 파란색과 같은 경우이다.

k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]

# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def get_d_index_when_rotate_to_back(d):
    if d %2 == 1:
        return d-1
    else :
        return d+1

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    current_stacked_horse_map = [[[] for _ in range(0,n)]for _ in range(0,n)]
    stack = [[]for _ in range(0, horse_count)]
    for i in range(horse_count):
        r, y, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][y].append(i)

    count =1;
    while count < 1000:
        #말의 숫자만큼 반복해주는 말 이동 반복문
        for horse_index in range(horse_count):
            r, y, d = horse_location_and_directions[horse_index]
            new_r, new_y = r+dr[d], y+dy[d]
            #다음칸이 파란색이거나 범위를 벗어날경우 방향을 반대로 바꿔서 한칸전진
            #new_r > n or 0 >= new_r이런 형태를 0 <= new_r < n이런 형태로 좋게사용하기위해서
            #if not을 이용하여 0 <= new_r < n이범위 밖이라면 false라면 실행하게 된다.
            if not 0 <= new_r < n or not 0 <= new_y < n or game_map[new_r][new_y] == 2 :
                #바꾼 방향을 변수 temp_d에 넣어줌
                new_d = get_d_index_when_rotate_to_back(d)
                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_y = y + dy[new_d]
                #방향을 반대로 바꿨는데도 파란색이면 방향만 바꾸고 그자리에서 정지후 다음 말이동
                if not 0 <= new_r < n or not 0 <= new_y < n or game_map[new_r][new_y] == 2:
                    continue

            moving_horse_index_array = []

            for i in range(len(current_stacked_horse_map[r][y])):
                current_stacked_horse_index = current_stacked_horse_map[r][y][i]
                # 여기서 이동해야 하는 애들은 현재 옮기는 말 위의 말들이다.
                if horse_index == current_stacked_horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][y][i:]
                    current_stacked_horse_map[r][y] = current_stacked_horse_map[r][y][:i]
                    break

            # 2) 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
            if game_map[new_r][new_y] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)

            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_y].append(moving_horse_index)
                # horse_location_and_directions 에 이동한 말들의 위치를 업데이트한다.
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][
                    1] = new_r, new_y
                #4개가 한칸이상 쌓였다면 끝났으니 count를 반환해주고 종료해준다.
            if len(current_stacked_horse_map[new_r][new_y]) > 3:
                return count

        count += 1
    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))
