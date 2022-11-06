# Collections in Python

list = ["Udit", "Rahul","Amit"]
print(list)
list[1] = "Ankur"
print(list[1])
print(list)
for item in list:
    print(item)
    if item == "Udit":
        print("Yes 'Udit' is present")
    else:
        print("No 'Udit' is not present")

new_list = ["Ankit", "Pragya", "Pratyush"]
variable = iter(new_list)
print(next(variable))
print(next(variable))
print(next(variable))
