from datetime import datetime
print(20*"*","WELCOME TO RAM fruits market",20*"*")

customer_name=input("Enter the customer name:")

gender=int(input("for male press 1 or 2 for female:"))
for i in range(datetime.now):
    if datetime.now==12:
        print("good morning")
if gender==1:
    print("good morning",customer_name,"sir")
if gender==2:
    print("good morning",customer_name,"medam" )




list='''
apple       = Rs 120/kg
watermelon  = Rs 80/kg
grapes      = Rs 75/kg
banana      = Rs 40/DZ
cherry      = Rs 250/kg
coconut     = Rs 30/PS
pineapple   = Rs 100/kg
lemon       = Rs 90/kg
orange      = Rs 120/kg
kiwi        = Rs 250/kg
'''

# print (list)

price=0
listprice=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

items={'apple':120,'watermelon':80, 'grapes':75,'banana':40, 'cherry':250,
       'coconut':30,'pineapple':100,'lemon':90,'orange':120,'kiwi':250}

option=int(input("you want display list of fruits press 1: "))
if option ==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    # inp1 = int(input("If you want to buy, press 1. Press 2 to exit:"))

    if inp1==2:
        break
    if inp1==1:
        item=input("enter your fruits:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
# print(price)            
            listprice.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered iteam is no available")
    else:
        print("you entered wrong number")
    int=input("can i bill the iteam yes or no:")
    if int=='yes':
        pass
        if finalamount!=0:
            print(35*"*","RAM fruits market",35*"*")
            print(38*"=","RAJAHMUNDRY", 38*"=")
            print("Name:",customer_name,40*" ","Date:",datetime.now())
            print(90*":")
            print("s.no",20*" ",'items',20*" ",'quantity',20*" ",'price') 
            for i in range(len(listprice)):
                print(i,23*' ',ilist[i],21*' ',qlist[i],28*' ',plist[i])
                print(90*"-")
                print(60*" ",'totalamount:','Rs',totalprice)
            
                print(60*" ","gst amount",'Rs',gst)
                print(90*"-")
                print(60*" ",'finalamount:','Rs',finalamount)
                print(90*"-")
                print(35*" ","thanks for visiting")
                print(90*"*")
              





















































































































