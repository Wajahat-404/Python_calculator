#hey there! I'm going to try for python inputs...
#message = input('What is your name? ');
#print('My name is: ', message);
#no = max(5,10);
#print(no);
#first_name = "dada"
#last_name = "lovelace"
#full_name = f"{first_name} {last_name}"
#print(f"Hello, {full_name.title()}!")

#---------#TABLE USING FOR LOOP-------------
#userin = input('Enter your input: ')
#if type(userin) == str:
 #   print("yes it's a string!!!")
#else: 
    #print("not a string!!!")
#---------------- -------------------------

#famous_person  = "Albert Einstin"
#quote = '"A person who never made a mistake never tried anything new."' 
#message =  f"{famous_person} once said,  {quote} " 
#print(message)
#----------------------- ---------------
#print(4+4)
#print(10-2)
#print(4*2)
#print(int(16/2))
#----------------------- ---------------
#PYTHON CALCULATOR
print("Plz enter your 1st number: ")
a = int(input())
print("Plz enter your  2nd: ")
b = input()
print("Plz enter your 2nd number: ")
c = int(input())

if(b == '+'):
    print(int(a+c))
elif(b == '-'):
    print(int(a-c))
elif(b == '*'):
    print(int(a*c))
elif(b == '/'):
    if (c == 0):
        print("Math Error!")
    else: 
        print(int( a/c))
else:
    print("Enter correct inputs.")
#print(a,b,c)