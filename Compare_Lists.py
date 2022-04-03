"""def compare(l1,l2):
    i=len(l1)
    j=len(l2)
    flag=0
    x=0
    if i==j:
        while x<i:
            if l1[x]==l2[x]:
                flag=flag+1
                x=x+1
        if flag==i:
            print("List Are Same")
        else:
            print("Lists Are Not Same")
    else:
        print("List Are Not Same")

l1=[12,34,56,78,90]
l2=[12,34,56,78]
compare(l1,l2)"""

"""class Std_Name:
    def_init_(self, Std_firstName, Std_Phn, Std_lastName)
        self.Std_firstName=Std_firstName
        self.Std_PhnStd_Phn=Std_Phn
        self.Std_lastNameStd_lastName = Std_lastName
Std_firstName="Wick"
name=Std_Name(Std_firstName, 'F', "Bob")
Std=firstName= "Ann"
Name.lastName = "Nick"
print(name.Std_firstName, name.Std_lastName)"""

"""i=1
while True:
    if i%3==0:
        break
print(i)"""

"""x='pqrs'
for i in range(len(x)):
    x[i].upper()
print(x)"""

"""list1=[3,4,5,20,5,25,1,3]
list1.pop(1)
print(list1)"""

user_input = input("What is your name? ")
if user_input == "Python":
    print("Welcome to IDLE!")
else:
    print("Welcome to Python!")


print("This statement is an unsaved change!")