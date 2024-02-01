from time import *
import random as r
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error += 1
        except:
            error += 1
    return error
def speed_time(time_s,time_e,usreinput):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed=len(usreinput)/time_R
    return round(speed)
if __name__ == "__main__":
    while True:
        ck=input("Ready to Type? : Y/N  ")
        if ck=="Y":
            test = ["Write : My name is Krishna Handa","Write : I am Btech 1st year student ","Write : I am studying in LPU"]
            test1=r.choice(test)
            print("*****typing speed*****")
            print(test1)
            print()
            print()
            time_1=time()
            testinput=input("Enter : ")
            time_2=time()
            print('Speed : ',speed_time(time_1,time_2,testinput),"w/sec")
            print("Error : ",mistake(test1,testinput))
        elif(ck == 'N'):
            print("Good Bye")
            break
        else:
            print("Invalid Input")
