n = int(input("enter how many values you want to enter : "))
arr= []
flag = False
while(n>=1):
    arr.append(input("Enter value : "))
    n=n-1;
    
for i in range(len(arr)-1):
    flag= False;
    if arr[i] == arr[i+1]:
        flag = True
        break

if flag == True:
    print("same nums")
else:
    print("lodo maro")