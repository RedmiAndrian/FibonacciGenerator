print("Hello!")
print("This is a Python fibonacci generator!")
inp = int(input("Enter an integer that is greater than 5:  "))
list = [0, 1, 1]
a = 1
b = 2
first_num = 0
if inp < 5:
  print("Dude, that was easy to do!! >:( ")
else:
  for i in range(0 , (inp - 3)):
    first_num = list[a] + list[b]
    list.append(first_num)
    a = a + 1
    b = b + 1

print(list)
