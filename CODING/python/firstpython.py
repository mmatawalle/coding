name = input('Name: ')

if (len(name)) < 3:
    print('Name must me more than 3 characters')
elif (len(name)) > 50:
    print("Name shouldn't be more than 50 characters")
else:
    print('Name looks good !!')
    