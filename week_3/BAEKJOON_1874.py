
def stack_sequence(n, sequence):
    stack = []
    num = 1
    sequence_idx = 0
    result = []
    for i in range(n*2):
        #밖에서 0일때 선언하고 하는것도 가능하지만
        #stack에서 다빼고 아무것도 없을때
        #sequence에서 내용을 확인할때 오류가 남으로
        if len(stack) == 0:
            stack.append(num)
            result.append("+")
            num += 1

        elif sequence[sequence_idx] == stack[-1]:
            stack.pop()
            result.append("-")
            sequence_idx += 1
            if sequence_idx == n:
                break
        else :
            if n < num:
                print("NO")
                break
            stack.append(num)
            result.append("+")
            num += 1

    if len(stack) == 0:
        for i in result:
            print(i)

sequence = list()

n = int(input())
for _ in range(n):
    sequence.append(int(input()))

stack_sequence(n, sequence)