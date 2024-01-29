import os
if __name__=='__main__':
    print("Welcome to RoboSpeaker by Krishna Handa")
    while True:
        x=input("Enter what you want to speak: ")
        if x == "Q":
            os.system("say 'bye bye friend")
            break 
        command = f"say {x}"
        os.system(command)
