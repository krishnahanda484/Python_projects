if __name__=='__main__':
    pass
k,j,d=0,0,0
email=input("Enter your email : ")
#a@b.in(Minimum char-6)
if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@")==1):
            if (email[-4]=="." or email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Your email is wrong")
                else:
                    print("Your email is correct")
            else:
                print("Your email must contain '.com' or '.in' ")
        else:
            print("Your email must have a '@'")
    else:
        print("Your email must start from alphabet")
else:
    print("You email is short")