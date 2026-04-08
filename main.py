from Girl import Girl
import story
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

girl = Girl("Aiko", 40)
girl.update()

game_loop = True

for k, v in story.events.items():
        
        loop = True
        if k in story.end:
            ending = girl.get_end()
            k = ending
            loop = False
        
        for I in story.events[k].split("|"):
            print(I)
        print("")
        girl.interact(k)
            
        girl.status()
        input("\npress any key to continue...")
        clear()
        
        if not loop:
            break
    