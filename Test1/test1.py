import random, numpy, pygame, time, os




phrase = "your cute and amazing"

text = ""

for i in range(len(phrase)):

    text += phrase[i]
    
    os.system("cls")
    
    print(text, end="")
    
    print("")
    
    if i % 2 == 1 or i == len(phrase) - 1:
        print(":3")
    else:
        print(":o")
    
    time.sleep(random.uniform(0.25,0.05))
    
