import matplotlib.pyplot as plt

'''
costStruct = [  {'date': '7.1', 'item': ['两餐'], 'consume': [33], 'flag': [0]},
                {'date': '7.2', 'item': ['两餐', '遮阳布', '!出行'], 'consume': [25, 6, 13], 'flag': [0, 0, 1]},
                ...
             ]
'''
costStruct = []
with open(file='cost.txt', mode='r', encoding='utf-8') as fp:
    costStrList = fp.readlines()

# 删除空白行
delNum = 0
for i in range(len(costStrList)):
    j = i - delNum
    costStrList[j] = costStrList[j].strip('\n')
    if len(costStrList[j].replace(' ', '')) == 0:
        delNum = delNum + 1
        del(costStrList[j])
# print(costStrList)

for i in range(len(costStrList)):
    costDic = {'date': '', 'item': [], 'consume': [], 'flag': []}
    strList = costStrList[i].split(' ')
    costDic['date'] = strList[0]
    for j in range(1, len(strList)):
        cost = strList[j].split('-')
        if cost[0][0] == '!':
            costDic['flag'].append(1)
            costDic['item'].append(cost[0][1:])
        else:
            costDic['flag'].append(0)
            costDic['item'].append(cost[0])
        costDic['consume'].append(int(cost[1]))
    costStruct.append(costDic)
# print(costStruct)

# 计算总共花费
dayCost = []
dateStr = []
sumConsumeFlag1 = 0     # 不统计在内
for i in range(len(costStruct)):
    sumConsumeFlag0 = 0
    for j in range(len(costStruct[i]['consume'])):
        if costStruct[i]['flag'][j] == 0:
            sumConsumeFlag0 = sumConsumeFlag0 + costStruct[i]['consume'][j]
        elif costStruct[i]['flag'][j] == 1:
            sumConsumeFlag1 = sumConsumeFlag1 + costStruct[i]['consume'][j]
    dayCost.append(sumConsumeFlag0)
    dateStr.append(costStruct[i]['date'])
    print(costStruct[i]['date'] + ' cost ￥' + str(dayCost[i]))
print('total cost ￥' + str(sum(dayCost)), end=', ')
print('and ￥' + str(sumConsumeFlag1) + ' are not counted')
# 绘图
plt.figure(figsize=(3+0.25*len(dayCost), 8), dpi=100)    # 自适应长度
plt.bar(dateStr, dayCost)
plt.xticks(rotation=45)
plt.title('total cost ' + str(sum(dayCost)) + ' yuan')
plt.xlabel('date')
plt.ylabel('consume')
plt.show()
