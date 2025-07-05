from datetime import datetime
name=input("Enter your name:")
lists='''
Rice  Rs 20/kg
Sugar Rs 30/kg
Salt Rs 20/kg
Oil Rs 80/litre
Paneer Rs 110/kg
Maggie Rs 50/kg
Boost Rs 90/each
Colgate Rs 85/each
'''
#declartion
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#rates for items
items={'Rice':20,
'Sugar':30,
'Salt':20,
'Oil':80,
'Paneer':110,'Maggie':50,'Boost':90,'Colgate':85}
Option=int(input("For list of items press1:"))
if Option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        bresk
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item is not available")
    else:
        print("You entered a wrong number")
    inp=input("Can I bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Rohini Supermarket",25*"=")
            print(28*" ","Vizag")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*' ',plist[i])
            print(75*"-")
            print(50*" ",'totalamount:','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")            
            print(50*" ",'finalamount:','Rs',finalamount)
            print(75*"-") 
            print(20*" ","Thanks for Visiting")
            print(75*"-")