
def encode(s):
    r = ""
    for n in s:
        n = int(n)
        n += 3
        if n == 12:
            r += "2"
        elif n == 11:
            r += "1"
        elif n == 10:
            r += "0"
        else:
            r += str(n)
    return r
    
   def decode(s):           
    r = ""               
    for n in s:          
        n = int(n)       
        n -= 3           
        if n == -3:      
            r += "0"     
        elif n == -2:    
            r += "9"     
        elif n == -1:    
            r += "8"     
        else:            
            r += str(n)  
        return r       

if __name__ == '__main__':
    e = ""
    p = ""

    while True:
        print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")

        opt = int(input("Please enter an option:"))
        if opt == 1:
            p = input("Please enter your password to encode:")
            e = encode(p)
            print("Your password has been encoded and stored!")
        elif opt == 2:
            print(f"The encoded password is {e}, and the original password is {p}.")
        elif opt == 3:
            quit()
        else:
            pass


