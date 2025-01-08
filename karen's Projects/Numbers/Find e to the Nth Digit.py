from decimal import Decimal, getcontext

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def get_e(digits):
    if digits > 1000:
        digits = 1000
        print("Limited to 1000 digits")
        
    getcontext().prec = digits + 1
    
    e = Decimal(1)
    for n in range(1, digits + 10):
        try:
            term = Decimal(1) / Decimal(factorial(n))
            e += term
            if term < Decimal(10) ** (-digits):
                break
        except Exception:
            break
            
    return str(e)[0:digits+2]

def main():
    while True:
        try:
            digits = int(input("Enter number of decimal places (max 1000): "))
            if digits < 1:
                print("Please enter a positive number")
                continue
            print(get_e(digits))
            break
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    main()