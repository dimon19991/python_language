#task1------------------------------------------------------------
"""
�������� ��������, ��� ������ ��� ����� � ����� �� ����. ����� ����� ���������� ������� � �������� �����.
"""
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
�������� ��������, ��� ������ ������� ���� ������ ������������ ���������� �� �������� ���� �����. ���������� ������� ������� ������ � ������� ������.

"""
b = int(input())
h = int(input())
print(1/2*b*h)
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
N �������� �������� K ����� � ���������� �� �� ����� ������. ��������� ������ ���������� � ������. ������ ����� ������ ����� �������? ������ ����� ���������� � ������?
"""
n = int(input())
k = int(input())
print(k // n)
print(k % n)
#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
����� ����� N - ������� ������, ����������� ���� ������. ������ ����� � ������ ���� ���������� �������� ��������, ���� �� ���� ����� 00:00?
"""
a = int(input())
b=a//60
b=b%24
c=a%60
print(b,c)
#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
�������� ��������, ��� ��� �����������, �������� ����� "Hello", ��'� ����������� � ���� ������ ���� �����. ��������� �Hello, Mike!�

"""
a = str(input())
print("Hello, "+a+"!")
#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
�������� ��������, ��� ����� ���� ����� � ����� ���� ��������� � �������� �������� �� ��������:
"""
a = int(input())
b=(a+1)
c=(a-1)
a=str(a)
b=str(b)
c=str(c)
print("The next number for the number "+a+" is "+b+".")
print("The previous number for the number "+a+" is "+c+".")

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
����� ������� ���������� ��� ��� ����� ����� �� ������ �� ����� �����. � ������� ���� ��������� ���������� ����� ��� �����, 
� ����������, �� �� ����� ������ ���� ����� �� ����� ���� �����. ��� ��������� ������� ����� ��������� ��������?
"""
a = int(input())
b = int(input())
c = int(input())
d=(a+1)//2
e=(b+1)//2
f=(c+1)//2
print(d+e+f)
#-----------------------------------------------------------------