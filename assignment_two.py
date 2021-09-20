name = input("PLEASE STATE YOUR NAME.")
print("nice name. I like it.")
where=input("PLEASE STATE WHERE YOU ARE FROM.")
print("I have been to", where,"many times. I hope to go again soon.")
favnum = int(input("AS SIMPLY AS POSSIBLE, TELL ME YOUR FAVORITE NUMBER"))

favcar = input("WHAT IS YOUR DREAM CAR MODEL, BRAND, AND YEAR?")

carabs = float(input("WHAT IS THE TOTAL PRICE OF THIS CAR?"))

carmon = float(input("WHAT IS THE MONTHLY INTEREST OF THIS CAR?"))

howmany = float(input("HOW MANY PAYMENTS DO YOU NEED TO MAKE?"))

mpymt = (carmon * carabs) / (1 - (carmon + 1)**-howmany)