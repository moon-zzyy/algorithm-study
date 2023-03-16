from collections import deque
import sys
input = sys.stdin.readline


def boj10845():
    queue = deque()

    for _ in range(int(input())):
        command = input().split()

        if command[0]=='push':
            queue.append(command[1])
        elif command[0] == 'pop':
            if queue: print(queue.popleft())
            else: print(-1)
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            if queue: print(0)
            else: print(1)
        elif command[0] == 'front':
            print(queue[0] if queue else -1)
        else: # 'back'
            print(queue[-1] if queue else -1)


def boj18258():
    queue = deque()

    for _ in range(int(input())):
        command = input().split()

        if command[0]=='push':
            queue.append(command[1])
        elif command[0] == 'pop':
            if queue: print(queue.popleft())
            else: print(-1)
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            print(0 if queue else 1)
        elif command[0] == 'front':
            print(queue[0] if queue else -1)
        else: # 'back'
            print(queue[-1] if queue else -1)


def boj2164():
    N = int(input())
    queue = deque([i for i in range(1,N+1)])

    while len(queue)>1:
        queue.popleft()
        queue.append(queue.popleft())
    print(queue[0])


if __name__ == '__main__':
    boj2164()