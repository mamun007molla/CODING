alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
def encrypt(text,shift):
    new_text=""
    for i in text:
        if i in alphabet:
            if ord(i)+shift>122:
                count=ord(i)+1+shift-26
                
                new_text+=chr(count)
            else:
                new_text+=chr(ord(i)+shift)
        else:
            new_text+=i
    
    print(f"Here's the encoded result: {new_text}")

def decode(text,shift):
    new_text=""
    for i in text:
        if i in alphabet:
            if ord(i)-shift<97:
                count=ord(i)-shift+26-1
                
                new_text+=chr(count)
            else:
                new_text+=chr(ord(i)-shift)
        else:
            new_text+=i
    
    print(f"Here's the decoded result: {new_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction=="encode":
        encrypt(text,shift)
    elif direction=="decode":
        decode(text,shift)
    next=input("Type 'yes' if you want to go again. otherwise type 'no'.")
    if next=="no":
        break
        


