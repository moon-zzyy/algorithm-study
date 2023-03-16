import itertools
import sys
input = sys.stdin.readline

# ... 포기
def boj15683():
    N, M = map(int, input().split())  # 세로, 가로
    board = [map(int, input().split()) for _ in range(N)]




# 1도 모르겠음...
# 참고: https://baejinsoo.github.io/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EB%AC%B8%EC%A0%9C%ED%92%80%EA%B8%B0/BOJ_18808/
def boj18808():
    def pastable(x, y):
        for i in range(R):
            for j in range(C):
                if board[x + i][y + j] == 1 and sticker[i][j] == 1:
                    return False  # 붙일수없음
        for i in range(R):
            for j in range(C):
                if sticker[i][j] == 1:
                    board[x + i][y + j] = 1
        return True  # 붙임

    def rotate(s):
        rotated = [[0] * R for _ in range(C)]
        for i in range(R):
            for j in range(C):
                rotated[j][R - i - 1] = s[i][j]
        return rotated

    N, M, K = map(int, input().split())  # 노트북 세로, 가로, 스티커 개수
    board = [[0] * M for _ in range(N)]  # 노트북

    for i in range(K):
        R, C = map(int, input().split())  # 스티커 세로, 가로
        sticker = [list(map(int, input().split())) for _ in range(R)]

        for i in range(4):  # 회전
            flag = False

            if flag: break
            for i in range(N - R + 1):
                if flag: break
                for j in range(M - C + 1):
                    if pastable(i, j):  # 붙이면
                        flag = True
                        break
            sticker = rotate(sticker)
            R, C = C, R  # 행 열 바꾸기

    print(sum(map(sum, board)))  # 스티커 칸 수

# velog
# 다른풀이: https://velog.io/@toma/python-%EC%B9%98%ED%82%A8-%EB%B0%B0%EB%8B%AC-%EB%B0%B1%EC%A4%80-15686%EB%B2%88
def boj15686():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    houses, chickens = [], []  # 집과 치킨집 위치
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:  # 집
                houses.append((i, j))
            elif board[i][j] == 2:  # 치킨집
                chickens.append((i, j))

    dist = [] # 치킨거리 합
    for chicken in list(itertools.combinations(chickens, M)):
        temp = {h: 1e9 for h in houses} # 현재 M개의 치킨집과의 치킨거리
        for cx, cy in chicken:
            for hx, hy in houses: # 한 치킨집과 모든 집과의 거리
                temp[(hx, hy)] = min(temp[(hx, hy)], abs(cx - hx) + abs(cy - hy))
        dist.append(sum(temp.values())) # 현재 조합 치킨거리 합

    print(min(dist)) # 여러 치킨거리 중 최소


if __name__ == '__main__':
    boj15686()