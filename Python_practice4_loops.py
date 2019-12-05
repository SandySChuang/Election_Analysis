#While Loops
x = 0
while x <= 5:
    print(x)
    x = x + 1

#For Loops
counties = ("Arapahoe", "Denver", "Jefferson")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

#Loops with tuple
counties_tuple = ("Arapahoe","Denver","Jefferson")

for county in counties_tuple:
    print(county)

#Loops with dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for key in counties_dict.keys():
    print(key)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for voters in counties_dict.values():
    print(voters)

#Get Key-Value Pair
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for a, b in counties_dict.items():
    print(a,b)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(county,"county has", voters, "registered voters.")

#F-String with number format
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")