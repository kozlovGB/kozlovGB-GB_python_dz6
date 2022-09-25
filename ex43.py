#Задача 43: Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
a=[10,10,13,15,78,15]
index=[]
print(a)
for i in range(len(a)):
    chet=0
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            a[j]='j'
            chet+=1
    if chet!=0:
        a[i]='j'
for i in range(len(a)):
    if a[i]!='j':
        index.append(a[i])
print(index)