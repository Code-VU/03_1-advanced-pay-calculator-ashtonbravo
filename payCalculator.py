#def calculatePay():
    # This first line is provided for you
hrs = float(input("Enter Hours:"))
rate = float(input("Enter hourly rate: "))

#print (hrs)    
if hrs <= 40 :
    print("You didn't work more than 40 hours, no overtime pay. Your check will be $",(hrs*rate)) 
else :
    ot = hrs - 40
    #print (ot)
    ot_pay = (rate * 1.5 * ot) 
    #print (ot_pay)
    normal_pay= 40*rate
    #print(normal_pay)
    calcuationOT = normal_pay + ot_pay
    print ("You get overtime pay of $", calcuationOT)
    #print ('You get overtime pay')
    #print ()
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
#if __name__ == "__main__":
   # calculatePay()
