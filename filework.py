try:
    file = open('text1.txt','r')
    file.write("This write command")
    file.write("It allows us to write in a particular file")
    file = open('text1.txt','r')
    for each in file:
        print (each)
    file.close()
except :
    print("error")
finally:
    print(" i m still working")
    
    
    
