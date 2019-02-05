if __name__ == '__main__':
    birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

    print('Welcome to the birthday dictionary. We know the birthdays of:\n')
    for name in birthdays:
        print(name)

    choice = input("Who's birthday you want to check\n")
    if choice in birthdays:
        print("\nThe Birthday of %s is on %s" % (choice, birthdays[choice]))
    else:
        print("\nSadly we dont have record of Birthday", choice)
