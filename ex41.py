#Задача 41: Напишите программу вычисления арифметического
#выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
string=input('Введите выражение')
Symbol=['-','+','/','*']
ch=[]
sym=[]
s=''
def de(sym,ch,index):
    sym.pop(index)
    ch.pop(index + 1)
for i in string:
    if i not in Symbol:
        s+=str(i)
    else:
        ch.append(s)
        s=''
        sym.append(i)

ch.append(s)
while (len(ch)-1)!=0:
    if '*' in sym and '/' in sym :
        if sym.index('*')<sym.index('/'):
            index=sym.index('*')
            ch[index]=float(ch[index])*float(ch[index+1])
            de(sym,ch,index)
        else:
            while sym.index('/')<sym.index('*'):
                index = sym.index('/')
                ch[index] = float(ch[index]) / float(ch[index + 1])
                de(sym, ch, index)

    elif '*' in sym and '/' not in sym :
        index = sym.index('*')
        ch[index] = float(ch[index]) * float(ch[index + 1])
        de(sym, ch, index)
    elif '*' not in sym and '/' in sym:
        index = sym.index('/')
        ch[index] = float(ch[index]) / float(ch[index + 1])
        de(sym, ch, index)
    else:
        if '+' in sym and '-' in sym:
            if sym.index('+') < sym.index('-'):
                index = sym.index('+')
                ch[index] = float(ch[index]) + float(ch[index + 1])
                de(sym, ch, index)
            else:
                index = sym.index('-')
                ch[index] = float(ch[index]) - float(ch[index + 1])
                de(sym, ch, index)

        elif '+' in sym and '-' not in sym:
            index = sym.index('+')
            ch[index] = float(ch[index]) + float(ch[index + 1])
            de(sym, ch, index)
        elif '+' not in sym and '-' in sym:
            index = sym.index('-')
            ch[index] = float(ch[index]) - float(ch[index + 1])
            de(sym, ch, index)

print(*ch)
