

import time
from time import gmtime, strftime
money=0
n=None
am=["The correct answer to this question can win you 1000, wrong can kick you out",
    "The correct answer to this question can win you 5000, wrong can fall you to 1000",
    "The correct answer to this question can win you 10,000, wrong can fall you to 1000",
    "The correct answer of this question can renew 50,000, wrong can KICK YOU out with ZERO"]

Ql=["Who was the first prime minister of India ",
    "Champaran is situated in which state",
    "Who was the president of USA before Barack Obama",
    "Which city is known as valley of flowers"]

Al=[["a- Jawaharlal Nehru", "b- Mahatma Gandhi", "c- Dr Rajendra Prasad", "d- None of these"],
    ["a- Uttarakhand", "b- UttarPradesh", "c- Bihar", "d- Maharashtra"],
    ["a- Donald Trump", "b- G W Bush", "c- Abraham Lincoln", "d- J F Kennedy"],
    ["a- Lohaghat", "b- Massorie", "c- Dehradun", "d-Haridwar"]]

print(am[0])
print()
print(Ql[0])
for i in Al[0]:
    print(i)
n=input("\nEnter choice ")

if n=="A" or n=="a":
    print("Your answer is correct")
    money+=1000
    
    time.sleep(2)

    print()
    print()
    print(am[1])
    print()
    print(Ql[1])
    for i in Al[1]:
        print(i)
    n=input("\nEnter choice ")
    if n=="C" or n=="c":
        print("Your answer is correct")
        money+=5000

        time.sleep(2)

        print()
        print()
        print(am[2])
        print()
        print(Ql[2])
        for i in Al[2]:
            print(i)
        n=input("\nEnter choice ")
        if n=="B" or n=="b":
            print("Your answer is correct")
            money+=10000

            time.sleep(2)

            print()
            print()
            print(am[3])
            print()
            print(Ql[3])
            for i in Al[3]:
                print(i)
            n=input("\nEnter choice ")
            if n=="B" or n=="b":
                print("Your answer is correct")
                money+=50000
                print("Total money won is",money)
            
            else:
                print("Your answer is incorrect sorry, the correct answer is B")
                print("\nAmount won is",money)
                
            
        else:
            print("your Answer is incorrect sorry, the correct answer is C")
            print("\nAmount won is",money)
            
        
    else:
        print("your Answer is incorrect sorry, the correct answer is C")
        print("\nAmount won is",money)
        
    
else:
    print("Your answer is incorrect sorry, the correct answer was A")
    


