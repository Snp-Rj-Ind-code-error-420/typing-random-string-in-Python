import keyboard, time
import random
count=0
time.sleep(10)

def generate(k):
    list_strong=[" ","1","2","3","4","5","6","7","8","9","0",
                 "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                 "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                 "!","@","#","$","%","^","&","*","(",")","_","+","{","}","|",":","<",">","?","-","=","[","]",";",",",".","/","\'","\"","\\"]
    count=0
    
    num_max = random.randint(1,100)

    while count<num_max:
            
                k=k+random.choice(list_strong)
                count=count+1
    return k

while True:
    if count==5:
        keyboard.write(generate(""))
        keyboard.press_and_release('enter')
        time.sleep(2)
        count+=1
    else:
        time.sleep(15)
        count=0
