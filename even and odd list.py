list=[10,501,22,37,100,999,87,351]
even=[] #empty list to store even numbers in list
odd=[] #empty list to store odd numbers in list

for i in range(len(list)):
    if list[i]%2==0: #given number divisible by 2 and remainder is zero then print even number
        even.append(list[i])
    else:  
        odd.append(list[i]) 

print("Even number list:",even)
print("Odd number list:",odd)