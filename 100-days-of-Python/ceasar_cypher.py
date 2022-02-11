
from numpy import indices
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = '''
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
| |     ______   | || |  _________   | || |      __      | || |    _______   | || |      __      | || |  _______     | |  
| |   .' ___  |  | || | |_   ___  |  | || |     /  \     | || |   /  ___  |  | || |     /  \     | || | |_   __ \    | |  
| |  / .'   \_|  | || |   | |_  \_|  | || |    / /\ \    | || |  |  (__ \_|  | || |    / /\ \    | || |   | |__) |   | |  
| |  | |         | || |   |  _|  _   | || |   / ____ \   | || |   '.___`-.   | || |   / ____ \   | || |   |  __ /    | |  
| |  \ `.___.'\  | || |  _| |___/ |  | || | _/ /    \ \_ | || |  |`\____) |  | || | _/ /    \ \_ | || |  _| |  \ \_  | |  
| |   `._____.'  | || | |_________|  | || ||____|  |____|| || |  |_______.'  | || ||____|  |____|| || | |____| |___| | |  
| |              | || |              | || |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
| |     ______   | || |     _____    | || |   ______     | || |  ____  ____  | || |  _________   | || |  _______     | |  
| |   .' ___  |  | || |    |_   _|   | || |  |_   __ \   | || | |_   ||   _| | || | |_   ___  |  | || | |_   __ \    | |  
| |  / .'   \_|  | || |      | |     | || |    | |__) |  | || |   | |__| |   | || |   | |_  \_|  | || |   | |__) |   | |  
| |  | |         | || |      | |     | || |    |  ___/   | || |   |  __  |   | || |   |  _|  _   | || |   |  __ /    | |  
| |  \ `.___.'\  | || |     _| |_    | || |   _| |_      | || |  _| |  | |_  | || |  _| |___/ |  | || |  _| |  \ \_  | |  
| |   `._____.'  | || |    |_____|   | || |  |_____|     | || | |____||____| | || | |_________|  | || | |____| |___| | |  
| |              | || |              | || |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   


'''

print(logo)


def caesar(t,s,dir):
    result = ""
    indices = 0
    if(dir == "decode"):
       s *= -1
    for char in t:
        if char in alphabet:
            indices = alphabet.index(char)
            new_index = int(indices) + int(s)
            new_letter = str(alphabet[new_index])
            result += new_letter
        else:
            end_text += char
    print(f"The {dir}d text is {result}")

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(t = text, s = shift, dir = direction)
    restart = input("Type 'Y' if you want to go again. Otherwise type 'N'.\n")
    if restart == "N":
        should_end = True
        print("You have completed your cipher journey, till next time!")