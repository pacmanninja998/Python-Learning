import random

def toss(flips):
    H = T = 0
    for i in range(flips):
        coin = random.choice(['H', 'T'])
        #print(f"coin")
        if (coin == "H"):
            H += 1
        else:
            T += 1
    print(f"Out of {flips} Flips \nHeads: {H}\nTails: {T}")

def main():
	toss(int(input("# of Flips: ")))

if __name__ == "__main__":
    main()