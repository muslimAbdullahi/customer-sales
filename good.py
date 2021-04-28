# -*-coding:utf8;-*-
# qpy:console
# Geeting to the customer
import time

print("------welcome to Ab store-------")
time.sleep(1.0)
print("We provide you many kind of food")
print(" To proceed put your information")
time.sleep(0.95)
name = input("what is your name ? ")
print(" We welcome you" + " " + name)
rice = 250
beans = 150
pepper = 300
yam = 500
egg = 50
time.sleep(0.95)
food = (" This are the food we have: 1=Rice, 2=yam ,3=egg, 4=beans, 5=peppe ")
print(food)
time.sleep(0.95)
customer_question = input(" which kind of food did you  want ?")
if customer_question.lower() == "rice":
    print(f" we sell rice for" + "#" + str(rice))
elif customer_question.lower() == "beans":
    print(f" we sell beans for" + "#" + str(beans))
elif customer_question.lower() == "pepper":
    print(f"we sell pepper for" + "#" + str(pepper))
elif customer_question.lower() == "yam":
    print(f"we sell yam  for" + "#" + str(yam))
elif customer_question.lower() == "egg":
    print(f"we sell egg for" + "#" + str(egg))
else:
    print("This food is out of stock")
    exit()
print("These are the methods 1=cash , 2=transfer")
time.sleep(0.95)
paying = input("choose method to pay ? ")
if paying == "cash":
    me = input("put your account pin ::")
    men = int(me)
    print(" Payment received")
elif paying == "transfer":
    print("pay to account name: muslim abdullahi, account number: 0153561051")
    print("Your payment is recieved")
    time.sleep(0.95)
else:
    print("Payment is not allowed")
    exit()
time.sleep(0.95)
print(name + " " + "your food will be deliver to you in the next 24hours")
