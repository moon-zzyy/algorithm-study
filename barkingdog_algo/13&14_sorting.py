import collections
import sys
input = sys.stdin.readline

# merge sort
def boj11728():
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    i, j = 0, 0
    result = []
    while len(result)<N+M:
        if i==N:
            result.append(arr2[j])
            j+=1
        elif j==M:
            result.append(arr1[i])
            i+=1
        elif arr1[i]<=arr2[j]: # stable sort
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    # if i<N:
    #     result.extend(arr1[i:])
    # if j<M:
    #     result.extend(arr2[j:])
    print(*result)

# counting sort
def boj15688():
    int_dict = {}
    for _ in range(int(input())):
        n = int(input())
        if n not in int_dict: int_dict[n]=1
        else: int_dict[n]+=1

    arr = sorted(int_dict.keys())
    for n in arr:
        print(f'{n}\n'* int_dict[n], end='')

# 다중조건
# 참고: https://hongcoding.tistory.com/61
def boj1431():
    def sum_serial(serial):
        temp = 0
        for s in serial:
            if s.isdigit(): temp += int(s)
        return temp

    N = int(input())
    arr = [input().strip() for _ in range(N)]
    sorted_arr=sorted(arr, key=lambda x : (len(x), sum_serial(x), x))
    print(*sorted_arr, sep='\n')


def boj11652():
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    arr.sort()

    count = 0
    answer = -2**62-1
    temp = 1
    for i in range(1, len(arr)):
        if arr[i-1]!=arr[i]:
            if count<temp:
                count = temp
                answer = arr[i-1]
            temp=1
        else:
            temp+=1
    if count<temp: answer = arr[-1]
    print(answer)

    # arr.sort()
    # count_arr = collections.Counter(arr)
    # print(count_arr.most_common()[0][0])

# 시간초과
# velog; 검색결과가 없음
# 참고: https://becca-codingdiary.tistory.com/entry/5648-%EC%97%AD%EC%9B%90%EC%86%8C-%EC%A0%95%EB%A0%AC
def boj5648():
    arr = []
    flag = True
    while True:
        try:
            line = input().strip()
            for num in line.split():
                if flag:  # 첫번째 숫자
                    flag = False
                    continue
                num = ''.join(num[::-1]).lstrip('0')
                arr.append(int(num))
        except EOFError: break

    arr.sort()
    for n in arr: print(n)


def boj1181():
    N = int(input())
    words = set(input().strip() for _ in range(N)) # 중복제거

    arr = sorted(list(words), key= lambda x:(len(x), x)) # 길이짧은 순, 알파벳순으로 정렬
    print(*arr, sep='\n')


def boj2910():
    N, C = map(int, input().split())
    arr = list(map(int, input().split()))

    counter = collections.Counter(arr)
    for k, v in counter.most_common():
        print(f'{k} '*v, end='')

if __name__=='__main__':
    boj2910()