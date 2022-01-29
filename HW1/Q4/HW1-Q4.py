# This is an example of a python dictionary which contains lists and tuples
# The dictionary contains information about an apartment building

from pprint import pprint

building = {
    'building_name' : '43rd Street Apartments',
    'city': 'Los Angeles',
    'state': 'CA',
    'number_of_floors': 20,
    'number_of_available_apartments': 5,
    'available_units': [1, 10, 15, 17, 25],
    'unit_types': ('studio', 'full', 'penthouse'),
    'unit_rates': (1000, 2000, 3000),
    'management_staff': ['John Smith', 'Jane Doe', 'Bob White', 'Kate Buck']
}

# Unit 15 is purchase
building['available_units'].remove(15)
building['number_of_available_apartments'] = 4

# Find the rate for a penthouse unit
penthouse_rate = building['unit_rates'][2]
print(penthouse_rate)

# Tuples are immutable, they cannot be modified

# A new employeed is hired onto the management staff. Append method adds a new item to the end of the list
building['management_staff'].append('Sharon Fields')

# See changes
pprint(building)