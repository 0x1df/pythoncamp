age = int(input("enter youre age please:\n"))
license = input("DO you have license?(True/False):\n").lower()=='true'

if age >= 19 and license :
    print("yes u can drive the vechile ")

elif age < 19:
    print(" you need to grow up kido ;]")

elif  age >= 19 and license == False:
    print("you need to apply for lisence bro you can apply from here https://sarathi.parivahan.gov.in/sarathiservice/stateSelection.do")      

else:
    print("sry u can't drive the vechile ")