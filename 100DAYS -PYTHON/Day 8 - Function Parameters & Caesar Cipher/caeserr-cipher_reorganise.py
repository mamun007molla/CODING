alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

 
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

 
def caeser(text,shift,direction):
    new_text=""
    alp=-25
    if direction=="decode":
            shift*=-1
            alp*=-1
    for i in text:
       
        if i in alphabet:
            if (ord(i)+shift>122) or (ord(i)+shift<97 ):
                count=ord(i)+alp+shift
                
                new_text+=chr(count)
            else:
                new_text+=chr(ord(i)+shift)
        else:
            new_text+=i
    
    print(f"Here's the {direction}d result: {new_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction !="encode":
        if direction!="decode":
            print("it is wrong input.please press the right value")
            continue

    

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if type(shift)!= int:
        print("please give me int value only")
        continue
    shift=shift%26
    caeser(text,shift,direction)
    
    next=input("Type 'yes' if you want to go again. otherwise type 'no'.")
    if next=="no":
        print("Good Bye")
        break
        


