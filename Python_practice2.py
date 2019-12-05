#If Statement
counties = ["Arapahoe","Denver","Jefferson"]
if counties[2] != 'Jefferson':
    print(counties[2])

#If-Else Statement
temperature = int(input("What is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")