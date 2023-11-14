import random

blocks = ["L", "J", "S", "Z", "T", "I", "O"]

def bag():
    global blocks
    choice = random.choice(blocks)
    blocks.remove(choice)
    print("Block chosen: ", choice)
    print("List now: ", blocks)
    
    if(blocks == []):
        blocks = ["L", "J", "S", "Z", "T", "I", "O"]
x=0
while(x<10):
    bag()
    x+=1