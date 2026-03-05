#N2
# < , > , >= , <= , == , !=
print(10>5)
print(5>4)
print(8<15)
print(5<10)
print(10>=10)
print(10>=5)
print(8<=8)
print(5<=10)
print(10==10)
print(44==48)
print(10!=5)
print(1!=14)


#N3
#or - არამკაცრი ოპერატორია რომლის დროსაც არ არის საჭირო ორივე დადებითი რომ იყოს 
#and - მკაცრი ოპერატორია რომლის დროსაც აუცილებელია ორივე პუნქტი დადებითი იყოს


#N4

height = int(input ("enter your height"))
my_height = 180
print(height < my_height)


#N5
num1 = "21"
num2 = 21
print(num1 == num2)
#stirng-ის და integer-ის შედარება არ შეიძლება



#N6

lastname = "dvalidze"
lastname2 = input("enter your lastname")
print(lastname == lastname2)



#N7

# False or True and True and False

# • True and False or False or True

# • True or True and False or True or False and True or False

print(False or True and True and False)
#     True        True       false

print(True and False or False or True )
#         false    false      true  

print(True or True and False or True or False and True or False)
#      true      false    true    true   false  true




#N8
Degrees = int(input ("enter degree : "))
print(Degrees > 30)


#N9
temperature = int(input("enter celsius: "))
fahrenheit = temperature * 1.8 + 32 
print(temperature > 89.6)
