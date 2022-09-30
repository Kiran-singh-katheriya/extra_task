'''1. Create a list of given structure and get the Access list as provided below:
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
Access list: [1, 2, 3, 4]
Access list: [600, 700]
Access list: [100, 300, 500, 600, 800]
Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
Access list: [10]
Access list: [ ]

#solution:
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
l1=x[5][0:4]
print(l1)
#[1, 2, 3, 4]

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
l2=x[-3:-1]
print(l2)
#[600, 700]

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
l3=x[0:5]
l=x[6]
ll1=x[-1]
l3.append(l)
l3.append(ll1)
print(l3)
#[100, 200, 300, 400, 500, 600, 800]

x.reverse()
print(x)
#[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]

l5=x[5][5][0]
print(l5)

x.clear()
print(x)
'''

'''
2. Create a list of thousand numbers using range and xrange and see the difference between each
other

r=range(0,1000)
print(type(r))
print(len(r))

rx=xrange(0,1000)
print(type(rx))
print(len(rx))
'''

'''
3. How Tuple is beneficial as compared to the list?
Answer:
If we talk about memory,Tuples are more memory efficient than the lists because tuple are immutable in nature so,Tuples are stored in a single block of memory.It doesn't require extra space to store new objects which makes it more faster than list.
'''

'''4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
the number which is divisible by 3 and is a multiple of 2.

for i in range(1,1001):
    if((i%3==0) and (i%2==0)):
        print(i,end=" ")
'''  

'''5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
string with their index.

#solution:


def rev_str(x):
    results=""
    for i in x:
        if i not in 'aieouAIEOU':
            results+=i
    return results[::-1] 

print(rev_str("I am in halloween month"))
#htnm nwllh n m
'''

'''6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
string which is having an even length.

s="This is a python language and i am learning this"
char=s.split(" ")
for i in char:
  if len(i)%2==0:
    print(i,end=" ")
'''


'''7. Write a program in python to print the pair of numbers whose sum is equal to the result
number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1] 

def pair_num(x,n):
    x.sort()
    i=n-1
    while(i>=0):
        j=0
        k=i-1
        while (j<k):
            if (x[i]==x[j]+x[k]):
                print("This is perfect pair:",x[i],x[j],x[k])
                return
            elif(x[i]>x[j]+x[k]):
                j+=1
            else:
                k-=1
        i-=1
    print("no match found")

x=[1,2,3,4,5,6,7,8,9,-1]
n=len(x)
pair_num(x,n)

'''

'''8. Write a program in Python to complete the following task:
Create two lists such as even_list and odd_list
Ask user to enter a number in the range of 1,50 and make sure if the entered number is even, append it to the even_list and if the entered number is odd append it to the odd_list
Keep that in mind you can only add 5 items in each list.
Make sure once you enter all the 5 elements, calculate the sum of the list and return the maximum of the list.

'''


'''
#solution:
x=int(input("Enter a number between"))
even_list=[]
odd_list=[]
for i in x:
    if i%2==0:
        even_list.append(i)
        if len(even_list)==5:
            pass
    else:
        odd_list.append(i)
        if len(odd_list)==5:
            pass


print(even_list)
print(odd_list)
#[2, 34, 2, 8]
#[31, 17, 5, 33, 5]

'''

#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]




'''
9.Write a program to find out the occurrence of a specific character from an alphanumeric string.
Sample input: 12abcbacbaba344ab 
Expected output: a=5 b=5 c=2

#solution:

s="12abcbacbaba344ab"
count_a=0
count_b=0
count_c=0
for i in s:
    if i =='a':
        count_a +=1
    elif i=='b':
        count_b+=1
    elif i=='c':
         count_c+=1

print("a=",count_a)
print("b=",count_b)
print("c=",count_c)
'''



'''
10. Generate and print another tuple whose values are even numbers in the given tuple
(1,2,3,4,5,6,7,8,9,10)

#solution:

x=(1,2,3,4,5,6,7,8,9,10)
tp=list(x)
result_tup=[]

for i in tp:
    if i%2==0:
        result_tup.append(i)

print(tuple(result_tup))

'''