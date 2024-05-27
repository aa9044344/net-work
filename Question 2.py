x=int(input('Enter the number of digits in the binary number : '))
sum=0
z=0
for i in range(x):
    print("The box",i)
    a=int(input("Enter it : "))
    if a==1:
        sum=sum+2**z
        z=z+1 
        continue           
    elif a==0:
        sum=sum+0
        z=z+1            
        continue
    else:
        print("invalid entry ")    
    break 
if a==1 or a==0  :         
  print(sum)    