#task1------------------------------------------------------------
"""
���� ��� ����� �����. ������� �������� � ���.
"""
a = int(input())
b = int(input())
if (a>b):
    print (b)
else:
    print(a)
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
������� ��������� �������sign(x), �� ����������� ��������� �����: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0..

"""
x = int(input())
if x>0:
    print(1)
if x==0:
    print(0)
if x<0:
    print(-1)
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
���� ��� ����� �����. ������� �������� � ���.
"""
a = int(input())
b = int(input())
c = int(input())
if a<b<=c:
    print (a) 
if a<c<b:
    print (a)
if b<a<=c:
    print (b)
if b<c<a:
    print (b)
if c<a<=b:
    print (c)
if c<b<a:
    print (c)
#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
���� ���� �����, �� ������� ��. ���������, �� � �������� �� ����������. ���� ���, �� ������� ����������� "LEAP", � ������ ������� � "�OMMON".
"""
a = int(input())
if (((a%4)==0) and ((a%100)!=0)) or ((a%400)==0):
    print ('LEAP')
else:
    print ('COMMON')
#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
���� ��� ����� �����. ��������, ������ � ��� ��������� ���� ������. �������� ������� �������� ���� � �����: 3 (���� �� ����� �������), 
2 (���� ��� � ��� ��������� ���� ������, � ���� �����������) ��� 0 (���� �� ����� ����).

"""
a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print ('3')
if a==b!=c or b==c!=a or c==a!=b:
    print ('2')
if a!=b and b!=c and c!=a:
    print ('0')
#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
������ ���� ����������� �� ���������� ��� �� ��������. ���� ���������� ���� ����� ������ �����. ���������, �� ���� ���� ������� � ����� ������ � ����� �� ���� ���. 
���������� ������� ������ ����� ����� �� 1 �� 8, ����� � ���� ������� ����� ����� �� ��������� ������. ����� ��� ����� - ��� ����� ������, ������� ��� ����� � ��� �����. 
�������� �� ������� "YES", ���� ���� ���� �������� ����������, ��� "NO" � ������ �������.
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a==c or b==d:
    print('YES')
else:
    print('NO')
#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
���� ���������� ���� ����� ������ �����. ���������, �� ���������� ���� �������. ���������� ������� ������ ����� ����� �� 1 �� 8, 
����� � ���� ������� ����� ����� �� ��������� ������. ����� ��� ����� - ��� ����� ������, ������� ��� ����� � ��� �����. 
�������� �� ������� "YES", ���� ���� ���������, ��� "NO" � ������ �������.
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if ((a+b)%2)==((c+d)%2):
    print('YES')
else:
    print('NO')
#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
������� ������ ����������� �� ����������, �� �������� ��� �� ������� �� ����-��� ������ �������. ���� ���������� ���� ����� ������ �����. ���������, 
�� ���� ������ ������� � ����� ������ � ����� �� ���� ���. ���������� ������� ������ ����� ����� �� 1 �� 8, ����� � ���� ������� ����� ����� �� ��������� ������. 
����� ��� ����� - ��� ����� ������, ������� ��� ����� � ��� �����. �������� �� ������� "YES", ���� ��� ��������, ��� "NO" � ������ �������.

"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if ((a==c) and ((b-d)==1 or (d-b)==1)) or (b==d and ((a-c)==1 or (c-a)==1)) or (((a-c)==1) and ((b-d)==1 or (d-b)==1)) or (((c-a)==1) and ((b-d)==1 or (d-b)==1)):
    print ('YES')    
else:
    print ('NO')
#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
������� ���� �������� �� ������� �� ����-��� ������� �����. ���� ���������� ���� ����� ������ �����. ���������, �� ���� ���� ������� � ����� ������ � ����� �� ���� ���. 
���������� ������� ������ ����� ����� �� 1 �� 8, ����� � ���� ������� ����� ����� �� ��������� ������. ����� ��� ����� - ��� ����� ������, ������� ��� ����� � ��� �����. 
�������� �� ������� "YES", ���� ��� ��������, ��� "NO" � ������ �������.
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if ((a-c)==(b-d) or (a-c)==(d-b)) or ((c-a)==(b-d) or (a-c)==(d-b)):  
    print ('YES')    
else:
    print ('NO')
#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
������ �������� �������� �� ����������, �� �������� ��� �� ������� �� ����-��� ������� �����. ���� ���������� ���� ����� ������ �����. ���������, 
�� ���� �������� ������� � ����� ������ � ����� �� ���� ���. ���������� ������� ������ ����� ����� �� 1 �� 8, ����� � ���� ������� ����� ����� �� ��������� ������. 
����� ��� ����� - ��� ����� ������, ������� ��� ����� � ��� �����. �������� �� ������� "YES", ���� ��� ��������, ��� "NO" � ������ �������.
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if ((a-c)==(b-d) or (a-c)==(d-b)) or ((c-a)==(b-d) or (a-c)==(d-b)) or (a==c or b==d):  
    print ('YES')    
else:
    print ('NO')
#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
������� ��� �������� �� ����� L. ³� ���� ����������� �� �� ������� �� ���������� � ���� ������� �� �������� ��� �� �� ������� �� �������� � ���� �� ����������. 
���� ���������� ���� ����� ������ �����. ���������, �� ���� ��� ������� � ����� ������ � ����� �� ���� ���. ���������� ������� ������ ����� ����� �� 1 �� 8, 
����� � ���� ������� ����� ����� �� ��������� ������. ����� ��� ����� - ��� ����� ������, ������� ��� ����� � ��� �����. 
�������� �� ������� "YES", ���� ��� ��������, ��� "NO" � ������ �������.

"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (((b-d)==2) or ((d-b)==2)) and (((a-c)==1)or((c-a)==1)) or (((a-c)==2) or ((c-a)==2)) and (((b-d)==1)or((d-b)==1)):
    print ('YES')
else:
    print('NO')
#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
������� �� ����� ������������, ���������� �� n?m �����. ������� ���� ���� ��������� �� �� ������� ����� �� ���������� ��� �� ��������, 
��� ����� ������ ����� ���� ������. ���������, �� ����� �������� ������� �� ���� ���� ����� �����, ��� ���� � ������ ������ ����� k �����. 
�������� �� ������� "YES", ���� ������� ����� �������, ��� "NO" � ������ �������.
"""
n = int(input())
m = int(input())
k = int(input())
a=n*m
b=a-k
if b>0 and (b%n==0 or b%m==0):
    print ('YES')
else:
    print ('NO')
#-----------------------------------------------------------------