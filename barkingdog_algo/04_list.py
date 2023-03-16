# *
def boj1406():
    S = list(' ' + input().strip())
    M = int(input())
    cursor = len(S)-1
    for _ in range(M):
        query = input().strip()

        if query == 'L':
            if cursor>0:
                cursor-=1
        elif query == 'D':
            if cursor<len(S)-1:
                cursor+=1
        elif query == 'B':
            if S:
                if cursor > 0:
                    del S[cursor]
                    cursor -= 1
        else:
            c = query.split()[1]
            cursor+=1
            S.insert(cursor, c)

    print(''.join(S).strip())

# *
def boj5397():
    for _ in range(int(input())):
        L = input().strip()
        s1, s2 = [], []
        for s in L:
            if s=='<':
                if s1: s2.append(s1.pop())
            elif s=='>':
                if s2: s1.append(s2.pop())
            elif s=='-':
                if s1: s1.pop()
            else:
                s1.append(s)

        s1.extend(reversed(s2))
        print(''.join(s1))

# *
from collections import deque
def boj1158():
    N, K = map(int, input().split())
    queue = deque([ i for i in range(1,N+1)])
    answer=[]

    while queue:
        for _ in range(K-1):
            queue.append(queue.popleft())
        answer.append(queue.popleft())
    print(str(answer).replace('[','<').replace(']','>'))

def boj1158_2():
    N, K = map(int, input().split())
    arr = [i for i in range(1, N + 1)]
    answer = []
    count = 0
    for _ in range(N):
        count = (count + (K - 1)) % len(arr)
        answer.append(arr.pop(count))

    print(str(answer).replace('[', '<').replace(']', '>'))


if __name__ == '__main__':
    boj1158()