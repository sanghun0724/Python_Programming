import SLIPs_list

#1
sum = 0
for i in SLIPs_list.slips:
    if (i[4]==20210117):
        sum+=i[13]
        print(sum)
##11번쟤 항목이 계정코드 14번째 항목이 금액  I[10] , I[13]

#2
result = 0
for idx in range(0, len(SLIPs_list.slips)):
    if (SLIPs_list.slips[idx][4] == 20210117):
        result+=SLIPs_list.slips[idx][13]
        print(result)
#출력 = 계정별 합계금액  list or dic

#3
list = []
total = []
for i in SLIPs_list.slips:
    if (i[10] not in list):
         list.append(i[10])
         total.append(i[13])
    else:
     idx = list.index(i[10])
     total[idx] = total[idx] + i[13]
print("@@@@@@@@@@@@@@@@@@@@@@@2")
print(list)
print(total)

#4
resultTotal = {}
for i in SLIPs_list.slips:
    if (i[10] not in resultTotal):
        resultTotal[i[10]] = i[13]
    else:
        resultTotal[i[10]] = resultTotal[i[10]] + i[13]

for result in resultTotal:
    print(result,resultTotal[result])
