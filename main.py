user = input("Enter your name: ")
print("------------------------------WELCOME------------------------------")
# print("---------","----------",sep=user)
x=input(f"{user} Pls press enter to continue......")
# print(user)
print("please select your level:")


def result():

    out = input("nice try brohhh!!!!\n Play it again ? [y/n]")

    if out.lower() == "y":

        print()
        print()

        level()
    elif out.lower() == "n":

        print("\n   Thanks \n Visit again:)", end=user)
    else:

        print("Bye Bye:)")


def level():
    print(
        "1.Easy  \n (i)Generated number will between 1-50 \n (ii) You will get 10 attemps \n2.Intermediate   \n (i)Generated number will between 1-100 \n (ii) You will get 10 attemps \n3. Advance:- \n (i)Generated number will between 1-1000 \n (ii) You will get 15 attemps \n "
    )
    lvl1 = (input("Enter the level= "))

    if lvl1.isdigit():

      lvl = int(lvl1)



      if lvl == 1: 

        game(1, 50, 10)
      elif lvl == 2:

        game(1, 100, 10)

      elif lvl == 3:

        game(1, 1000, 15)

      else:

        print("Pls select a valid number:----")

        level()
 
    else :
       print("---:Invalid lvl:---")
       level()

def game(a, b, x):

    import random

    number = random.randint(a, b)

    count = x

    history = []

    score = 100

    while True:

        if count == 0:

            result()
            break
        else:
            user_num1 = (input("Enter your gussed number: "))
  
            if user_num1.isdigit():

             user_num = int(user_num1)
            
             history.append(user_num)

             if number == user_num:
                print(
                    "---------------Wowwww------------- \n you did it brooo!!!\n score=",
                    score,
                )
                print("Previous Gusses:",end=" ")
                print(history)
                print("Remaning Attemps:", count - 1)
                result()
                break

             elif number > user_num:
                
                if score == 0 :

                     print("Oops You have lost your total score:----------\n")
                     result()
                else:
                    score -= 10
                    print("your number is smaller:::\n score=", score)
                    print("Previous Gusses:",end=" ")
                    print(history)
                    print("Remaning Attemps:", count - 1)
                    if count - 1 == 0:
                      print("^^^^^^GAME OVER:^^^^^^")
                      print("Magical Number:", number)
             elif number < user_num:

                if score == 0 :

                     print("Oops You have lost your total score:----------\n")
                     result()
                else : 
                     score -= 10
                     print("Your number is larger:: \n score=", score)
                     print("Previous Gusses:",end=" ")
                     print(history,sep=",,")
                     print("Remaning Attemps:", count - 1)
                if count - 1 == 0:
                    print("^^^^^^GAME OVER:^^^^^^")
                    print("Magical Number:", number)
        
            else:

                 score-=20
                 print("Invalid guess :\n Score: ",score)
                   
        count -= 1
        history.sort()

level()
