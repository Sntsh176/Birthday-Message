import json

if __name__ == '__main__':

    with open('birthdaydict.json', 'r') as file:
        birthdays = json.load(file)

    print("Welcome to Birthday Dictionary , we know Birthdays for below : ")
    for name in birthdays:
        print(name)

    while True:
        print("Type 'add' to add or 'exit' to quit\n")
        print("Who's birthday you want to know ")
        name = input()

        if name.lower() == 'exit':
            break
        elif name.lower() == 'add':
            new_name = input("Please enter the new Name : ")
            new_date = input("Please enter the new Birth date  : ")
            birthdays[new_name] = new_date
            with open('birthdaydict.json', 'w') as file:
                json.dump(birthdays, file)
        elif name in birthdays:
            print("The birthday of %s is on %s \n"%(name, birthdays[name]))
        else:
            print("\nSadly we dont have record of Birthday", name)