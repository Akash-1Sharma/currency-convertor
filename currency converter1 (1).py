# Project to make a Currency Converter 
currency={"USD":81.63,"EUR":85,"INR":1,"YEN":11.41,"Canadian Dollar":60.81,"Pound":99.15,"Russian Rubal":1.35,"South Korean Won":0.062,"Japanese Yen":0.59,"Australian Dollar":55.29,"Peso":0.017,"Pakistani Rupee":0.36} # Add more currency here
def convert(CU,a,CU2):
    if(CU2=="INR"):
        print("The Currency After Converting from %s is"%CU2,(amount*currency[CU]))
    elif(CU=="INR"):
        print("The Currency After Converting from %s is"%CU2,(amount/currency[CU2]))
    else:    
        print("The Currency After Converting from %s is"%CU2,(amount/currency[CU])*currency[CU2])

print(" ---------------------- ")
print("|  Currency Converter  |")
print(" ---------------------- ")
for i in currency.keys():
    print(i)
CU=input("Enter The Currency you want to convert to: ")
amount=eval(input("Enter The Amount: "))
CU2=input("Enter The Currency you want to convert from: ")
convert(CU,amount,CU2)
