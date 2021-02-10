 # Python program to print all PRIME Numbers between 200 and 500
 # Part I checking if a number inputted is a prime or not
 # prime number has 2 factors

 # ex  5
 #check from 1 to 5 if they factors
first_num = 20
end_num = 2000
#loop to get the numbers from 200 to 500 as input for PRIME number checking
while( first_num <= end_num ): 
 num = first_num
 
 #print( "The number entered is ", num)

 factors = 0
 start = 1
 end = num
 #loop that gives the factors from one to the number
 while ( start <= end):
    if ( num % start  == 0):
        #incrementing factors count if the number is a factor
         factors += 1
    start += 1
 print ("The no of factors ", factors )   

 if ( factors == 2):
    print("The number ", num ," is a PRIME")
 else:
    print("NOT PRIME")

 first_num += 1

print("The END")  
