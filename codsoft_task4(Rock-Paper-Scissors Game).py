import random

# a Function for "Who is the Winner"
def point_Count (upoint,cpoint): 
    if upoint==cpoint:
        print("Overall Match draw.")
        print("Computer's Point: ",cpoint)
        print("Your Point: ",upoint)
        print("Thanks for Playing.")
    elif upoint > cpoint:
        print("User win overall match.")
        print("Computer's Point: ",cpoint)
        print("Your Point: ",upoint)
        print("Thanks for Playing.")
    else:
        print("Computer win overall match.")
        print("Computer's Point: ",cpoint)
        print("Your Point: ",upoint)
        print("Thanks for Playing.")


print("Welcome Rock-Paper-Scissors Game : ") #print the title
value={1:"Stone",2:"Paper",3:"Sessior"}
cpoint=0 #it track computer's point
upoint=0 #it track user's point
while True:
    print("--------------------------------------------------") #it seperated the next Iteration
    uch=int(input("Enter Your Choice\n1.Stone 2.Paper 3.Sessior 0.Quit:\n"))
    cch=random.randint(1,4)
    if uch==0:
        break
    if cch==uch:
        print("Computer's choice: ",value[cch])
        print("User's choice: ",value[uch])
        print("Match Draw.")
        print("------------------------------------------") #it seperated the next Iteration
    elif (uch== 1 and cch == 2) or (uch== 2 and cch == 3) or (uch== 3 and cch == 1):
        print("Computer's choice: ",value[cch])
        print("User's choice: ",value[uch])
        print("Computer Win")
        cpoint+=1
        print("------------------------------------------") #it seperated the next Iteration
    elif (uch== 2 and cch == 1) or (uch== 3 and cch == 2) or (uch== 1 and cch == 3):
        print("Computer's choice: ",value[cch])
        print("User's choice: ",value[uch])
        print("User Win")
        upoint+=1
        print("------------------------------------------") #it seperated the next Iteration
    elif (uch > 3 or uch < 0):
        print("Invalid input.")
        print("------------------------------------------") #it seperated the next Iteration

point_Count(upoint,cpoint)
