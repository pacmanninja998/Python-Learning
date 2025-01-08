def start(bottles):
    while (bottles != 0):
        print(spell_chunks(bottles), last_call(bottles) + " of Beer on the Wall")
        print(spell_chunks(bottles), last_call(bottles) + " of Beer")
        bottles -= 1
        print("Take One Down and Pass it Around")
        print(spell_chunks(bottles))
        if (bottles >= 1):
            print(last_call(bottles) + " of Beer")
        else:
            print("No More Bottles of Beer")

def last_call(last):
    if (last != 1):
        Cond = "Bottles"
        return Cond
    else:
        Cond = "Bottle"
        return Cond

def get_ones(num):
    ones = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 
            5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    return ones[num]

def get_teens(num):
    teens = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    return teens[num]

def get_tens(num):
    tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
            6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
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

def main():
    bottles = 99
    start(bottles)

if __name__ == "__main__":
    main()