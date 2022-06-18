import jieba
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False

with open('train.txt', 'r', encoding='utf8') as f:
    ads = [line.split('\t') for line in f]
with open('test.txt','r',encoding='utf8')as f:
    test=[line.split('\t') for line in f]

_,_ytest,_xtest=zip(*test)
_,y,x=zip(*ads)
test=list()
_ytest=list(_ytest)
_xtest=list(_xtest)
predix=list()
rate=0

y=list(y)
x=list(x)
key=list()
value=list()
countyes={}
countno={}
word=list()
words=list()
xtest=list()
xtests=list()
for i in range(len(x)):
    for j in x[i]:
        if j>=u'\u4e00'and j<=u'\u9fa5':
            continue
        else:
            x[i]=x[i].replace(j,'')

for i in range(len(x)):
    word.append(jieba.lcut(x[i]))
    words.append([])
    for j in word[i]:
          words[i].append(j)
#统计字符串出现的次数
for i in range(len(words)):
    for j in words[i]:
        sum=0
        for k in range(len(words)):
                for n in words[k]:
                    if j==n:
                        sum+=1
        if sum>3:
           key.append(j)
           value.append(sum)

no=y.count('0')
yes=y.count('1')

for i in key:
    sumyes=0
    sumno=0
    for j in range(len(words)):
        for k in words[j]:
            if i==k:
                if y[j]=='1':
                   sumyes+=1
                else:
                    sumno+=1
    countyes[i]=sumyes+1/yes+10
    countno[i]=sumno+1/no+10

for i in range(len(_xtest)):
    for j in _xtest[i]:
        if j>=u'\u4e00'and j<=u'\u9fa5':
            continue
        else:
            _xtest[i]=_xtest[i].replace(j,'')

for i in range(len(_xtest)):
    xtest.append(jieba.lcut(x[i]))
    xtests.append([])
    for j in xtest[i]:
          xtests[i].append(j)

for i in range(len(xtests)):
    for i in xtests[i]:
        predix_yes=1
        predix_no=1
        if i in countyes:
           predix_yes*=countyes[i]
           predix_no*=countno[i]
    if predix_no>=predix_yes:
        predix.append(0)
    else:       
        predix.append(1)

for i in range (len(_ytest)):
    test.append(i)
    _ytest[i]=int(_ytest[i])
    if predix[i]==_ytest[i]:
        rate+=1

rate=rate/len(_ytest)

plt.plot(predix,"ro",ms=1,label="预测值")
plt.plot(_ytest,"go",label="真实值")

plt.title("朴素贝叶斯实现垃圾短信分类")
plt.xlabel("测试样本序号")
plt.ylabel("分类")
plt.legend()

#绘制目标函数损失值

plt.show()
print("正常短信属性集")
print(countno)
print("垃圾短信属性集")
print(countyes)
print("预测准确度为：{}".format(rate))
print(predix,_ytest,rate)

