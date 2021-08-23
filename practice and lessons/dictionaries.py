#iterate through dict

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

#iterate through  dict with  keys method
for county in counties_dict.keys():
    print(county)

#iterate through  dict with values method
for voters in counties_dict.values():
    print(voters)

# use the format dictionary_name[key] to get the value for the key.
for county in counties_dict:
    print(counties_dict[county])

#iterate through with the get() method
for county in counties_dict:
    print(counties_dict.get(county))

# get key value pairs with items() method
for county, voters in counties_dict.items():            #for key, value in dictionary_name.items():
    print(county, voters)                               #    print(key, value)

#get each dict in a list of dicts
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

