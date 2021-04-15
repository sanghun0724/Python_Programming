#1

a = input()

if a.isdigit():

    print("숫자입니다")

else:

    print("문자열입니다")

#2





음료 = ['아메리카노','카페라떼','카푸치노','오렌지주스','콜라','자몽주스']

가격 = [2500,3000,3000,4000,1500,4000]

sum = 0



def switch(menu):

    if menu == '아메리카노':

        sum+=2500

    elif menu == '카페라떼':

        sum+=3000

    elif menu == '카푸치노':

        sum+=3000

    elif menu == '오렌지주스':

        sum+=4000

    elif menu == '콜라':

        sum+=1500

    elif menu == "자몽주스":

        sum+=4000



for i in range(0,5):

    b = input()

    switch(b)



print(sum)

#3

answer = input()

answer = answer.upper()

## 대문자로 만든뒤 넘겨주면된다.  소문자도 가능



#4 what is bianry search?

##오름차순으로 정렬된 배열에서 원하는 숫자를 찾는 탐색방법

## target 정한뒤 크면 오른쪽 작으면 왼쪽 탐색

##한번 돌때마다 반씩 줄어드니 시간복잡도는 O(logn)



#5
#binary search configuration 그냥 반복문
#리스트 생성

searchArr = list()

i = 1

while i <= 100:

    searchArr.append(i)

    i+=1



target = int(input())

left = 0

right = len(searchArr) - 1



while left>right:

    middle = left+right/2

    if searchArr[middle] == target:

        print("찾았다")

        print(searchArr[middle]+1 + "번째")

    elif searchArr[middle] > target:

        right = middle - 1

    else:

        left = middle + 1



print("찾는 수가 없습니다")
