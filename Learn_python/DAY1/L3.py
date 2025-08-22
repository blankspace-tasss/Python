age=5

if age>18:
    print("You are adult")
    print("you can vote")
    print("age:" + str(age))

elif age<18 and age>6:
    print("you are not adult")
    print("age:"+str(age))

else:
    print("you are a child")
    print("age:" + str(age))

    print("This is the end")