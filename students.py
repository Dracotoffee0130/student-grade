name = input("Enter name")
mark1 = int(input("Enter mark 1:"))
mark2 = int(input("Enter mark 2:"))

average = int((mark1 + mark2)/2)
print(f'Name: {name}')
print(f'Average: {average}')


total = mark1 + mark2
print(f'Total marks: {total}')

if (mark1 < 40) or (mark2 < 40):
  print("Fail")
else:
  print("passed")
