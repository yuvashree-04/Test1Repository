a=[4,7,8,3,9,2]
b=[1,5,7,8,9,3]
c=[2,4,7,3,0,9]
 
 #set() returns unique values from the list
d=set(a) & set(b) &  set(c)
print(list(d))