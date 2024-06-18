#arithmatic functions 

def add(num1,num2):
    return num1+num2
def substract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
if __name__ == "__main__":
    print("------CALCULATOR------")
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
while True:
    
    select = input("Enter choice(1/2/3/4): ")
    if select in ('1','2','3','4'):
        try:
            num1=float(input("enter the 1st number : "))
            num2=float(input("enter the 2nd number : "))
        except ValueError: 
            print("invalid input, please enter a proper function")
            continue
        if select=='1' :
            print(num1,"+",num2,'=',add(num1,num2))
        elif select=='2' :
            print(num1,"-",num2,'=',substract(num1,num2))
        elif select=='3':
            print(num1,"*",num2,'=',multiply(num1,num2)) 
        elif select=='4':
            print(num1,"/",num2,'=',divide(num1,num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
