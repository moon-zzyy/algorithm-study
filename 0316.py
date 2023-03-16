# backtraking
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

def boj15649():

    def func():
        if len(arr) == M:
            print(' '.join(map(str, arr)))
            return

        for i in range(1,N+1):
            if i not in arr:
                arr.append(i)
                func()
                arr.pop()

    N, M = map(int, input().split())
    arr = []
    func()


def boj15650():

    def func(start):
        if len(arr)==M:
            print(' '.join(map(str,arr)))
            return

        for i in range(start,N+1):
            if i not in arr:
                arr.append(i)
                func(i+1)
                arr.pop()
    N, M = map(int, input().split())
    arr = []
    func(1)


def boj15651():

    def func():
        if len(arr) == M:
            print(' '.join(map(str, arr)))
            return

        for i in range(1,N+1):
            arr.append(i)
            func()
            arr.pop()

    N, M = map(int, input().split())
    arr = []
    func()


def boj15652():

    def func(start):
        if len(arr) == M:
            print(' '.join(map(str, arr)))
            return

        for i in range(start,N+1):
            arr.append(i)
            func(i)
            arr.pop()

    N, M = map(int, input().split())
    arr = []
    func(1)


if __name__=='__main__':
    boj15652()