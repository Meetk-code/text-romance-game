import dialogues_girl
import dialogues_player

class Girl:
    def __init__(self, name, affection, mood="normal"):
        self.name = name
        self.affection = affection
        self.mood = mood
        
    def change_affc(self, affc_value):
        self.affection += affc_value
        if self.affection <= 30:
            self.mood = "angry"
        elif self.affection <= 60:
            self.mood = "normal"
        else:
            self.mood = "happy"
            
    def interact(self,ind = 1, action="normal"):
        print("Reply:\n")
        for ke, va in dialogues_player.events[ind].items():
            print(f"{ke} --> {va}")
       
        while True:
            choice = input("\n")
            if choice in dialogues_player.events[ind].keys():
                action = choice
                break
            else:
                print("Invalid! Try again")
        self.change_affc(dialogues_girl.events[ind][self.mood][action]["affc"])
        print(dialogues_girl.events[ind][self.mood][action]["text"])
        
    def get_end(self):
        if self.mood == "angry":
            return 5
        elif self.mood == "happy":
            return 7
        else:
            return 6
    
    def status(self):
        print(f"{self.name} has {self.affection} affection for you. She is {self.mood}")
        
    def update(self):
        if self.affection <= 30:
            self.mood = "angry"
        elif self.affection <= 60:
            self.mood = "normal"
        else:
            self.mood = "happy"