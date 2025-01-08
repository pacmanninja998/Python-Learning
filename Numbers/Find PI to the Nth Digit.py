from decimal import Decimal, getcontext

def get_pi(digits):
    if digits > 1000:
        digits = 1000
        print("Limited to 1000 digits")
        
    getcontext().prec = digits + 1
    
    pi = sum(1/Decimal(16)**k * 
            (Decimal(4)/(8*k + 1) - 
             Decimal(2)/(8*k + 4) - 
             Decimal(1)/(8*k + 5) -
             Decimal(1)/(8*k + 6)) for k in range(digits))
    
    return str(pi)[0:digits+2]  # +2 for the "3."

def main():
    while True:
        try:
            digits = int(input("Enter number of decimal places (max 1000): "))
            if digits < 1:
                print("Please enter a positive number")
                continue
            print(get_pi(digits))
            break
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    main()