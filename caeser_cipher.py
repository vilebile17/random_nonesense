import sys

letters = ["a", "b" , "c" , "d" ,"e" ,"f" ,"g" ,"h" ,"i", "j" ,"k" ,"l","m","n","o","p" ,"q" ,"r" ,"s" ,"t","u" ,"v", "w" ,"x" ,"y" ,"z"  ]

try:
    message = sys.argv[1]
except:
    print("Usage: python3 caeser_cipher.py <message_to_encode>")
    exit()

for i in range(len(letters)):
    new_message = ""
    index = 6
    for letter in message:
        if letter != "" and letter != " ":
            for j in range(i):
                if letters.index(letter) + j < 26:
                    index = letters.index(letter) + j
                else:
                    index = letters.index(letter) - 26 + j
            new_message += f"{letters[index]}"

    print(new_message , "\n")


