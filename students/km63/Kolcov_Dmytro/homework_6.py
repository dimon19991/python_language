#task1------------------------------------------------------------
"""
�������� ��� �������� ������ � ������� ��������� (�� ���� A[0], A[2], A[4], ...). 
"""
def input_elements():
    element=input().split()
    return element
    
def even_elements(element):
    even_element=[]
    longe = len (element)
    for i in range(0, longe+1, 2):
        even_element.append(element[i])
    return even_element
    
def print_elements(output_element):
    for i in output_element:
        print (i, end=' ')
        
print_elements(even_elements(input_elements())) 
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
�������� ��� ������ �������� ������. ��� ���� ����������� ���� for, ������������ �������� ������, � �� �� �������! 
"""
def input_elements():
    element=input().split()
    return element
    
def even_elements(element):
    even_element=[]
    longe = len (element)
    for i in range(0, longe):
        if int(element[i])%2==0:
            even_element.append(element[i])
    return even_element
    
def print_elements(output_element):
    for i in output_element:
        print (i, end=' ')
        
print_elements(even_elements(input_elements())) 
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
��� ������ �����. �������� ��� �������� ������, ������� ������ ����������� ��������. 
"""
def input_elements():
    element=input().split()
    return element
    
def even_elements(element):
    even_element=[]
    longe = len (element)
    for i in range(0, longe-1):
        if int(element[i])<int(element[i+1]):
            even_element.append(element[i+1])
    return even_element
    
def print_elements(output_element):
    for i in output_element:
        print (i, end=' ')
        
print_elements(even_elements(input_elements())) 
#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, �������� ��� �����. 
���� �������� ��������� ������ ����� ��� � �� �������� ������. ���� ����� ��� ������� ��������� � �������� ������ ����. 
"""
def input_elements():
    element=input().split()
    return element
    
def even_elements(element):
    even_element=[]
    longe = len (element)
    for i in range(0, longe-1):
        if int(element[i])*int(element[i+1])>0:
            even_element.append(element[i])
            even_element.append(element[i+1])
            if len (even_element)>1:
                break
    return even_element
    
def print_elements(output_element):
    for i in output_element:
        print (i, end=' ')
        
print_elements(even_elements(input_elements()))
#-----------------------------------------------------------------

#task5------------------------------------------------------------------------------------------------------------------------
"""
��� ������ �����. ����������, ������� � ���� ������ ���������, ������� ������ ���� ����� �������, � �������� ���������� ����� ���������. 
������� �������� ������ ������� �� �����������, ��������� � ��� ������������ �������.  
"""
def input_elements():
    element=input().split()
    return element
    
def even_elements(element):
    count=0
    even_element=[]
    longe = len (element)
    for i in range(1, longe-1):
        if int(element[i])>int(element[i-1]) and int(element[i])>int(element[i+1]):
            count+=1
    return count
    
def print_elements(output_element):
    print (output_element)
        
print_elements(even_elements(input_elements()))
#-----------------------------------------------------------------

#task6------------------------------------------------------------
"""
��� ������ �����. �������� �������� ����������� �������� � ������, � ����� ������ ����� �������� � ������. 
���� ���������� ��������� ���������, �������� ������ ������� �� ���.  
"""
def input_elements():
    element=input().split()
    return element
    
def even_elements(element):
    maximum=element[0]
    counter=0
    even_element=[]
    longe = len (element)
    for i in range(1, longe):
        if int(element[i])>int(maximum):
            maximum=element[i]
    while element[counter]!=maximum:
        counter+=1

    return maximum, counter

    
def print_elements(output_element):
    for i in output_element:
        print (i, end=' ')
        
print_elements(even_elements(input_elements()))
#-----------------------------------------------------------------

#task7------------------------------------------------------------
"""
���� ������� � ������ �����. �� ����� ����������� ��� ������������ ���������� ��� ����� � �����. �������� ��� ��� �������.

��������� �������� �� ���� �������������� ������������������ ����������� �����, ���������� ���� ������� �������� � �����. 
����� ����� �������� ����� X � ���� ����. ��� ����� �� ������� ������ ����������� � �� ��������� 200.

�������� �����, ��� ������� ���� ������ ������ � �����. ���� � ����� ���� ���� � ���������� ������, 
����� ��, ��� � ����, �� �� ������ ������ ����� ���. 
"""
def input�():
    variable=input().split()
    return variable
    
def even_elements():
    height=input�()
    height_Petya=input�()
    count=1
    longe=len (height)
    for i in range (0, longe):
        if int(height_Petya[0])<=int(height[i]):
            count+=1
    printe(count)
    return

    
def printe(output_element):
    print (output_element)
        
even_elements()
#-----------------------------------------------------------------

#task8------------------------------------------------------------
"""
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, �������� ��� �����. 
���� �������� ��������� ������ ����� ��� � �� �������� ������. ���� ����� ��� ������� ��������� � �������� ������ ����. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------

#task9------------------------------------------------------------
"""
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, �������� ��� �����. 
���� �������� ��������� ������ ����� ��� � �� �������� ������. ���� ����� ��� ������� ��������� � �������� ������ ����. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------

#task10------------------------------------------------------------
"""
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, �������� ��� �����. 
���� �������� ��������� ������ ����� ��� � �� �������� ������. ���� ����� ��� ������� ��������� � �������� ������ ����. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------

#task11------------------------------------------------------------
"""
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, �������� ��� �����. 
���� �������� ��������� ������ ����� ��� � �� �������� ������. ���� ����� ��� ������� ��������� � �������� ������ ����. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------

#task12------------------------------------------------------------
"""
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, �������� ��� �����. 
���� �������� ��������� ������ ����� ��� � �� �������� ������. ���� ����� ��� ������� ��������� � �������� ������ ����. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------

#task13------------------------------------------------------------
"""
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, �������� ��� �����. 
���� �������� ��������� ������ ����� ��� � �� �������� ������. ���� ����� ��� ������� ��������� � �������� ������ ����. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------

#task14------------------------------------------------------------
"""
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, �������� ��� �����. 
���� �������� ��������� ������ ����� ��� � �� �������� ������. ���� ����� ��� ������� ��������� � �������� ������ ����. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------