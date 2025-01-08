def get_ones(num):
    ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    return ones[num]

def get_teens(num):
    teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    return teens[num]

def get_tens(num):
    tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
            6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
    return tens[num]

def spell_chunks(number):
    if number == 0:
        return ''
    elif number < 10:
        return get_ones(number)
    elif number < 20:
        return get_teens(number)
    elif number < 100:
        tens, ones = divmod(number, 10)
        return get_tens(tens) + ('-' + get_ones(ones) if ones > 0 else '')
    else:
        hundreds, rest = divmod(number, 100)
        result = get_ones(hundreds) + ' hundred'
        if rest > 0:
            result += ' and ' + spell_chunks(rest)
        return result

def spell_number(number):
    if number == 0:
        return "zero"
    
    # Handle negative numbers
    if str(number)[0] == '-':
        return "negative " + spell_number(abs(number))
    
    # Split into chunks of thousands
    chunks = []
    num = number
    while num > 0:
        chunks.append(num % 1000)
        num //= 1000
    
    # Names for powers of 1000
    chunk_names = ['', ' thousand', ' million']
    
    # Build the result from right to left
    result = []
    for i, chunk in enumerate(chunks):
        if chunk > 0:
            chunk_text = spell_chunks(chunk)
            if i > 0:
                chunk_text += chunk_names[i]
            result.append(chunk_text)
    
    return ' '.join(reversed(result))

def get_spelling(number):
    # Handle integers
    if isinstance(number, int):
        return spell_number(number)
    
    # Handle floats
    int_digits, dec_digits = split_number(number)
    
    # Convert digits lists to numbers
    int_part = int(''.join(map(str, int_digits)))
    if not dec_digits:  # If no decimal part
        return spell_number(int_part)
    
    dec_part = int(''.join(map(str, dec_digits)))
    
    # Spell out both parts
    return f"{spell_number(int_part)} point {' '.join(spell_number(int(d)) for d in str(dec_part))}"

def split_number(number):
    # Handle negative numbers
    is_negative = str(number).startswith('-')
    number_str = str(abs(number))  # Remove negative sign for processing
    
    try:
        integer_part, decimal_part = number_str.split('.')
        int_digits = [int(digit) for digit in integer_part]
        if is_negative:
            int_digits[0] = -int_digits[0]  # Make first digit negative if needed
        return (int_digits, [int(digit) for digit in decimal_part])
    except ValueError:
        int_digits = [int(digit) for digit in number_str]
        if is_negative:
            int_digits[0] = -int_digits[0]  # Make first digit negative if needed
        return (int_digits, [])

def get_number():
    while True:
        try:
            user_input = input("Enter a number: ")
            if user_input == "0":
                print("zero")
                quit()
            # Handle negative numbers
            if user_input.startswith('-'):
                if user_input[1:].isdigit():  # Check if rest is a digit
                    return int(user_input)
                return float(user_input)
            # Handle positive numbers
            if user_input.isdigit():
                return int(user_input)
            return float(user_input)
        except ValueError:
            print("Please enter a valid number!")

def main():
    number = get_number()
    print(get_spelling(number))

if __name__ == "__main__":
    main()