import sys
input = sys.stdin.readline

def boj4949():
    while True:
        line = input().rstrip()
        if line=='.': break

        stack = []
        wrong = False
        for s in line:
            if s=='.':  break
            elif s == ')':
                if stack and stack[-1]=='(': stack.pop()
                else:
                    wrong=True
                    break
            elif s==']':
                if stack and stack[-1]=='[': stack.pop()
                else:
                    wrong=True
                    break
            elif s=='(' or s=='[':
                stack.append(s)

        print('no' if wrong or stack else 'yes')


def boj3986():
    answer=0
    for _ in range(int(input())):
        stack = []
        for s in input().strip():
            if stack and stack[-1]==s: stack.pop()
            else: stack.append(s)
        if not stack: answer+=1

    print(answer)

# *
# 참고: https://claude-u.tistory.com/331
def boj10799():
    line = input().strip()
    stack = [] # count sticks
    answer = 0
    i = 0 # index for line
    while i<len(line):
        if line[i:i+2] == '()': # lazer
            answer+=len(stack)
            i+=2
            continue
        elif line[i]=='(': # start of stick
            stack.append(1)
            answer += 1
        elif line[i]==')': # end of stick
            stack.pop()
        i+=1

    print(answer)

# *
# https://www.jongung.com/283
def boj2504():
    line = input().strip()
    stack = []
    answer = 0
    temp = 1 # 중간 계산
    for i,s in enumerate(line):
        if s=='(':
            temp*=2
            stack.append(s)
        elif s=='[':
            temp*=3
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1]!='(': # 잘못된 괄호
                answer=0
                break
            if line[i-1]=='(': answer+=temp # '()' 만 값을 더해줌
            temp //= 2
            stack.pop()
        elif s == ']':
            if not stack or stack[-1] != '[': # 잘못된 괄호
                answer=0
                break
            if line[i-1]=='[':answer += temp # '[]' 만 값을 더해줌
            temp //= 3
            stack.pop()

    print(answer if not stack else 0)


if __name__ == '__main__':
    boj2504()