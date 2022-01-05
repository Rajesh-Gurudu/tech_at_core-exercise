for i in range(1,101): #Iterating Integers from 1-100.
    if i%2 == 0 and i%3 == 0:  #checking whether the number is divisible by 2 and 3.
        print("The number '{}' divisible by 2 and 3".format(i))
      
    elif i%3 == 0:#Checking whether the number is divisble by 3.
         print("The number '{}' divisible by 3".format(i))
    
    elif i%2 == 0:#checking whether the number is divisible by 2.
            print("The number '{}' is even".format(i))
         
    
    else:#Checking whether the number is odd.
        print("The number '{}' is odd".format(i))
