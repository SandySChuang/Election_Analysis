print("Hello World!")
#Creating and modifying list
counties = ["Arapahoe", "denver","Jefferson"]
counties
print(counties)
counties.append("El Paso")
print(counties)
#Tuple
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
counties_tuple[0:2]
#Creating dictionary
counties_dict = dict()
counties_dict["Arapahoe"] = 422829
counties_dict
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
len(counties_dict)
counties_dict.items()
    #counties_dict.Keys()
    #counties.dict.values()
counties_dict.get("Denver")
#Methods to get specific key value
    counties_dict["Arapahoe"]
    counties_dict.get("Arapahoe")
    print(counties_dict['Arapahoe'])
    print(counties_dict.get("Arapahoe"))
#List of Dictionaries
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data
len(voting_data)
#Add El Paso to second position
voting_data.insert(1,{"county":"El Paso", "registered_voters": 461149})
#Remove Arapahoe
voting_data.pop(0)
#Make Denver third item
voting_data[2] = {"county":"Denver", "registered_voters": 463353}
#Make Jefferson second item
voting_data[1] = {"county": "Jefferson", "registered_voters": 432438}
#Add Arapahoe
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data

#memberships
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in countries:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties. ")