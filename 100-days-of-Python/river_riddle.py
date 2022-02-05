#PS. I did this using if statements because it was the task for todays lesson. But I think I will try it again with a switch case soon or any other better method.
#However if you find a way to do this with less lines of code feel free to reach out.
#I have added the source of the ASCII art to the log.md file in case you'd like to try something out yourself.
#I added my own rules to the game ;).
#You fail the riddle if:
#1. You repeat a step
#2. Enter an invalid choice(not one provided)

print('''
*******************************************************************************
       ;~
       THE RIVER CROSSING RIDDLE
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----.....___
           \               ""/
      ~^~^~^~^~^`~^~^`^~^~^`^~^~^
       ~^~^~`~~^~^`~^~^~`~~^~^~
*******************************************************************************
''')
print("Welcome to The River Crossing Riddle")
print("Your goal is to help the farmer cross the river successfully with a wolf(W), a goat(G) and a cabbage(C).")
print("If left unattended together, the wolf would eat the goat, or the goat would eat the cabbage.")
print("After making a trip, he can return with an item on None(N).\n")



first = input("Which will you take first, W , G or C?\n")#g
#r1 = input("Which do you return with? W,G,C or N")#n

#second = input("Which will you take second, W , G or C?")#w or cW
#r2 = input("Which do you return with? W,G,C or N")#g

#third = input("Which will you take third, W , G or C?")#w or c
#r3 = input("Which do you return with? W,G,C or N")#n

#fourth = input("Which will you take fourth, W , G or C?")#g

if(first == "G"):
    print("You have taken the goat across the river. No casualties.")
    r1 = input("Do you wish to return with the goat? Y or N\n")#n
    if(r1 == "N"):
        print("You have returned to shore with no item")
        second = input("Which will you take second, W or C?\n")#w or c
        if(second == "W"):
            print("You have taken the wolf accross the river. No casualties.")
            r2 = input("Which do you return with? W,G or N\n")#g
            if(r2 == "G"):
                print("You have returned with the goat to shore.")
                third = input("Which will you take third, G or C?\n")#c
                if(third == "C"):
                    print("You have taken the cabbage accross the river. No casualties.")
                    r3 = input("Which do you return with? W,C or N\n")#n
                    if(r3 == "N"):
                        print("You have returned to shore with no item")
                        fourth = input("Will you take the goat across the river? Y or N\n")#g
                        if(fourth == "Y"):
                            print("You have taken the goat accross the river.")
                            print("Congratulations!! You have solved the riddle.")
                        else:
                            print("You have taken everything else across the bridge but the goat.")
                            print("Riddle Failed")
                    #elif for returning with wolf or cabbage
                    elif(r3 == "W"):
                        print("The wolf is back to shore and has eaten the goat.")
                        print("Riddle Failed")
                    elif(r3 == "C"):
                        print("You have taken the cabbage back to shore and the goat has eaten it.")
                        print("Riddle Failed") 
                    else:
                        print("Invalid choice")  
                        print("Riddle Failed")       
                #elif for going with goat
                elif(third == "G"):
                    print("You have taken the goat accross and the wolf has eaten the goat.")
                    print("Riddle Failed")
                else:
                        print("Invalid choice")  
                        print("Riddle Failed")
            #elif for returning with wolf
            elif(r2 == "W"):
                print("The wolf is back to shore. You have repeated this step.")
                print("Riddle Failed")
            #else for returning with nothing   
            elif(r2 == "N"):
                print("You haven't returned with an item. The wolf has eaten the goat.")
                print("Riddle Failed")
            else:
                print("Invalid choice")  
                print("Riddle Failed") 
        elif(second == "C"):
            print("You have taken the cabbage accross the river. No casualties.")
            r2 = input("Which do you return with? G,C or N\n")#g
            if(r2 == "G"):
                print("You have returned with the goat to shore.")
                third = input("Which will you take third, W , G or N?\n")#w
                if(third == "W"):
                    print("You have taken the wolf accross the river. No casualties.")
                    r3 = input("Which do you return with? W,C or N\n")#n
                    if(r3 == "N"):
                        print("You have returned to shore with no item")
                        fourth = input("Will you take the goat across the river? Y or N\n")#g
                        if(fourth == "Y"):
                            print("You have taken the goat accross the river.")
                            print("Congratulations!! You have solved the riddle.")
                        else:
                            print("You have taken everything else across the bridge but the goat. Sorry You will get it next time.")
                    elif(r3 == "W"):
                        print("The wolf is back to shore and has eaten the goat.")
                        print("Riddle Failed")
                    elif(r3 == "C"):
                        print("You have taken the cabbage back to shore and the goat has eaten it.")
                        print("Riddle Failed") 
                    else:
                        print("Invalid choice")  
                        print("Riddle Failed")
                elif(third == "G"):
                    print("You have taken the goat accross the river.The goat has eaten the cabbage.")
                    print("Riddle Failed")
                else:
                        print("You haven't taken anything across the river. The wolf has eaten the goat.")  
                        print("Riddle Failed")    
            elif(r2 == "C"):
                print("The cabbage is back to shore. You have repeated this step.")
                print("Riddle Failed")
            #else for returning with nothing   
            elif(r2 == "N"):
                print("You haven't returned with an item. The goat has eaten the cabbage.")
                print("Riddle Failed")
            else:
                print("Invalid choice")  
                print("Riddle Failed")    #   
        else:
            print("Invalid choice. You can only choose the wolf or cabbage.")  
            print("Riddle Failed") 
    elif(r1 == "G"):
        print("You have taken the goat back to shore. You have repeated a step.")   
        print("Riddle Failed")
    else:
            print("Invalid choice. You can only return the goat.")  
            print("Riddle Failed")     
elif(first == "C"):
    print("You have taken the cabbage accross the river. The wolf has eaten the goat.")
    print("Riddle Failed")   
elif(first == "W"):
    print("You have taken the wolf across the river. The goat has eaten the cabbage.")
    print("Riddle Failed") 
else:
    print("Invalid choice")  
    print("Riddle Failed")   
