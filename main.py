# a= "10"
# b= 2190
# c= 4168
#
# print("0" + a + "-" + str(b) + "-" + str(c))
#
# print("0{0}-{1}-{2}".format(a,b,c))
#
# print("내 이름은 ",end="강동훈입니다.\n")
#
# # name , age , lag 1개
# name,age,lag = input().split(" ")
# print("내 이름은 {0}이고, 나이는 {1}세이고, {2}천재입니다.╰(*°▽°*)╯".format(name,age,lag))
# ----------------------------------------------------------------------
# list (배열)
# dic (오브젝트)
# tuple 배열(내맘대로 수정가능, tuple은 내맘대로 수정 못함)
#
# arr = []
# arr.append("하나")
# arr.append("둘")
# arr.append("셋")
# print(arr)
# arr.pop(2)
# print(arr)
# for(i : arr){
# sysout(i)
# }
# for(int i = 0 ; i < arr.length; i++){
#
# }
#
# for i in arr:
#     print("i값은 : "+str(i))
#     for j in range(1,5):
#         print("j값은 : " + str(j))
# ----------------------------------------------------------------------
# 스타벅스
# 오늘 갓 내린 브라질산 아라비카 커피를 손님들에게 제공하기위해
# 스타벅스는 번호표를 뽑기로 하였다.
# 처음오는 손님부터 "1번손님 반갑습니다."

# for문을 사용하여 10명까지 드려보자

# for i in range(1,11):
#     print(str(i)+"번손님 반갑습니다.")
#
# num = int(input())
#
# if num == 0:
#     print("0입니다.")
# elif num % 2 == 0:
#     print("짝수 입니다.")
# else:
#     print("홀수입니다.")
#
# for i in range(0,11):
#     print("현재"+str(i)+"값은 : ",end="")
#     if i == 0:
#         print("0입니다.")
#     elif i % 2 == 0:
#         print("짝수 입니다.")
#     else:
#         print("홀수입니다.")
# ----------------------------------------------------------------------
# 우리가 계속 더해지는 숫자를 코딩하려합니다.
# 예를들어 x,y,z
# x는 제일 첫번째 숫자입니다.
# y는 계속해서 더해지는 숫자입니다.
# z는 몇번째 더해지는 숫자의 index입니다.
# x=1,y=2,z=5
# 1+2+2+2+2
# 9
# 등차수열이아함

# x,y,z = map(int,input().split())
# for i in range(int(z)-1):
#     x += int(y)
# print(x)
#
# arr = list(map(int,input().split()))
# for i in range(int(arr[2])-1):
#     arr[0] += int(arr[1])
# print( arr[0])


# 10 12 30 11 5 9 20
# 1~11 세의 손님은 돈 안받음

# age = list(map(int,input().split()))
#
# for i in age:
#     if 1<i<=11:
#         continue
#     print("500원입니다.")
# ----------------------------------------------------------------------
# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# 0 0 0 0 1
# n x m
#  0 이 아닌 숫자를 카운트 해보자
# arr = []
# li = []
# for i in range(5):
#     for j in range(5):
#         if i == j:
#             li.append(1)
#         else:
#             li.append(0)
#     arr.append(li)
#     li = []
#
# for i in arr:
#     print(i)

# [1,2],[2,1],[3,3],[4,4]
# 단이는 배추 농사를 하려한다.
# 5 x 5 의 농장에 위의 값이 입력될경우 해당칸에는 1 반대는 0
# 을 출력하는 프로그램을 만들어보자

# val = [[1,2],[2,1],[3,3],[4,4]]
# # 0 0 0 0 0
# # 0 0 1 0 0
# # 0 1 0 0 0
# # 0 0 0 1 0
# # 0 0 0 0 1
# val.append(["x","x"])
# for i in range(5):
#     print()
#     # print(val[i][0])
#     for j in range(5):
#         if val[i][1] == j and val[i][0] == val[j][0]:
#             print(1, end=" ")
#         else:
#             print(0,end=" ")
# #

# farm = []
# li = []
# for i in range(5):
#     for j in range(5):
#         li.append(0)
#     farm.append(li)
#     li=[]


# val = [[1,2],[2,1],[3,3],[4,4]]
# farm =[[0 for _ in range(5)] for _ in range(5)]
#
# for i in val:
#     farm[i[0]][i[1]] = 1
#
# for i in farm:
#     for j in i:
#         print(j,end=" ")
#     print()
#
# arr = [1,4,2,45,5,7,32,0]
# arr.sort()
# arr.reverse()
# print(arr)

def solution(m, load):
    ans = 0
    load.sort()
    now = 0
    back = len(load)-1
    print(load)

    while True:
        num = load[now] + load[back]
        # print(load[now], load[back])
        # print(num)
        if num < m:
            print("작다")
            while True:
                now += 1
                if num+load[now] > m:
                    back -= 1
                    ans += 1
                    break
        elif num == m:
            now += 1
            back -= 1
            ans += 1
        else:
            back -= 1
            ans += 1
        print(now , back)
        if now == back or now > back or back < now:
            if len(load) % 2 == 1:
                ans += 1
            print(ans)
            break

solution(20,[16,15,9,17,1,3])

# if load[now] + load[now + 1] + load[back] <= M:
#     now += 1
#     back -= 1
#     ans += 1




















