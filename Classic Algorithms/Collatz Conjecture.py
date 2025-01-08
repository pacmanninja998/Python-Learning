def home():
    try:
        import msvcrt
        return interactive_menu()  # Use fancy menu if msvcrt works
    except:
        return simple_menu()       # Fallback to simple menu

def interactive_menu():
    import msvcrt
    options = ['Auto 1-100', 'Full Tree']
    selected = [False] * len(options)
    current_choice = 0
    
    while True:
        print('\n' * 50)
        print("Use W/S to move, SPACE to select, ENTER to confirm")
        print("\nCollatz Conjecture Options:")
        
        for i, option in enumerate(options):
            cursor = ">" if i == current_choice else " "
            checkbox = "[X]" if selected[i] else "[ ]"
            print(f"{cursor} {checkbox} {option}")
        
        key = msvcrt.getch().decode('utf-8').lower()
        
        if key == 'w':
            current_choice = (current_choice - 1) % len(options)
        elif key == 's':
            current_choice = (current_choice + 1) % len(options)
        elif key == ' ':
            selected[current_choice] = not selected[current_choice]
        elif key == '\r':
            break
            
    return [opt for i, opt in enumerate(options) if selected[i]]

def simple_menu():
    options = ['Auto 1-100', 'Full Tree']
    print("\nCollatz Conjecture Options:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("\nEnter numbers for choices (e.g., '1' or '12' for both): ")
    
    choice = input("> ")
    selections = []
    if '1' in choice:
        selections.append('Auto 1-100')
    if '2' in choice:
        selections.append('Full Tree')
    return selections
    
# Collatz Conjecture
def Collatz (n) :
    steps = []
    while (n > 1) :
        steps.append(n)
        if (n % 2 == 0) :
            n /= 2
        else :
            n = n * 3 + 1
    steps.append(n)
    return steps



def main () :
    choice = home()
    if 'Auto 1-100' in choice:
        for i in range(1,101):
            steps = Collatz(i)
            if 'Full Tree' in choice:
                for l in steps:
                    print(f"{l} --> ", end="")
                print("1\n")
            else:
                print(f"{i}:{len(steps)}")
    else:
        num = int(input("Enter an integer: "))
        steps = Collatz(num)
        if 'Full Tree' in choice:
            for l in steps:
                print(f"{l} --> ", end="")
            print("1")    
        else:
            print(f"{i}:{len(steps)}")
    

if __name__ == "__main__":
    main()