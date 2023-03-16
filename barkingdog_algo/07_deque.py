from collections import deque
import sys
input = sys.stdin.readline


def boj10866():
    queue = deque()

    for _ in range(int(input())):
        command = input().split()

        if command[0]=='push_front':
            queue.appendleft(command[1])
        elif command[0]=='push_back':
            queue.append(command[1])
        elif command[0] == 'pop_front':
            if queue: print(queue.popleft())
            else: print(-1)
        elif command[0] == 'pop_back':
            if queue: print(queue.pop())
            else: print(-1)
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            print(0 if queue else 1)
        elif command[0] == 'front':
            print(queue[0] if queue else -1)
        else: # 'back'
            print(queue[-1] if queue else -1)

# *
def boj1021():
    N, M = map(int, input().split())
    queue = deque([0]*N)
    for i, n in enumerate(map(int, input().split())): # 뽑을순서저장
        queue[n-1] = i+1

    answer=0 # 정답
    for i in range(1, M+1):
        idx = queue.index(i) # 뽑을 수의 위치

        if idx <= len(queue)-idx: # left
            for _ in range(idx):
                queue.append(queue.popleft())
                answer+=1
        else: # right
            for _ in range(len(queue)-idx):
                queue.appendleft(queue.pop())
                answer+=1

        queue.popleft() # 뽑기

    print(answer)


# *
def boj5430():
    for _ in range(int(input())):
        p = input() # 수행할 함수
        n = int(input())
        arr = input().strip()[1:-1].split(',')
        queue = deque(arr) # 배열
        if n>0: # 배열의 길이가 0
            queue = deque()

        count = 0 # 뒤집기 횟수
        error = False # error인지
        for s in p:
            if s=='R':
                count+=1
            elif s=='D':
                if queue: # 뒤집기가 짝수면 왼쪽에서 버리기
                    if count%2==0: queue.popleft()
                    else: queue.pop()
                else: # 빈 queued이면 탈출
                    error = True
                    break

        if not error:
            if count%2!=0: queue.reverse() # 뒤집기가 홀수면 뒤집기
            print('[' + ",".join(queue) + ']')
        else:
            print('error')


if __name__ == '__main__':
    boj5430()