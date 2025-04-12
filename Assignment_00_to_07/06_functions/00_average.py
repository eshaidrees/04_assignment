def average(num1, num2):
    sum = num1 + num2
    return sum / 2

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = average(num1, num2)
    print(f"The average of {num1} and {num2} is: {result}")

if __name__ == '__main__':
    main()