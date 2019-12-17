x = int(input("Enter n1 : "))
y = int(input("Enter n2 : "))

def hcfnaive(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b)
    
print("GCD of two nums("+x+","+y+") is : "+hcfnaive(x,y))
