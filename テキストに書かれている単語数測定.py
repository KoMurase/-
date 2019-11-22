#!/usr/bin/python
# coding: UTF-8
f = open('*******.txt')
data1 = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()
print(type(data1)) # 文字列データ
lines1 = data1.split('\n') # 改行で区切る(改行文字そのものは戻り値のデータには含まれない)
print(len(lines1))

sum = 0
for line in lines1:
    l = line.split(',')
    sum += len(l)
print(sum)
#print(lines1[1])
#print(lines1[2])
#for line in lines1:
#    print(line)
