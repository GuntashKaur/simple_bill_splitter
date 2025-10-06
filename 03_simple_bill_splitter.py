def get_float(propmt):
    while True:
        try:
            return float(input(propmt))
        except:
            print("Please enter a valid number")



num_people = int(input("How many people are there is a group? "))

names = []

for i in range(num_people):
    names_entered = input(f"Enter name of person #{i+1}: ")
    names.append(names_entered)

enter_amount = get_float("\n Enter the total amount in number only: ")

share = round(enter_amount/ num_people)

print(f" \n Total Bill is: {enter_amount}")
print(f"\n Share per person is: {share}")

for name in names:
    print(f"\n {name} owes {share} ruppes")