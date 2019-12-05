#What is the score?
#score = int(input("What is your test score? "))

# Determine the grade
#if score >= 90:
        #print('Your grade is an A.')
#elif score >= 80:
        #print('Your grade is a B.')
#elif score >= 70:
        #print('Your grade is a C.')
#elif score >= 60:
        #print('Your grade is a D.')
#else:
        #print('Your grade is an F.')

#Membership
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
        print("El Paso is in the list of counties.")
else:
        print("El Paso is not in the list of counties.")

#Logical Operators
if "Arapahoe" and "El Paso" in counties:
        print("Arapahoe and El Paso are in the list of counties.")
else:
        print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" or "El Paso" in counties:
        print("Arapahoe or El Paso are in the list of counties.")
else:
        print("Arapahoe and El Paso are not in the list of counties.")