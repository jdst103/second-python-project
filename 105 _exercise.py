#Assignment for post class
# Learning outcome: [variables, print, different data types]
# ask and store the following in variables:
 # Name, last_name, age, age_of_mother, 3 skills
name = 'Bobby'
age = 6
age_of_mother = 34
skill1 = 'climbing'
skill2 = 'falling over'
skill3 = 'getting dirty'

 # Print out the information in a formated manor
name = input('hi, what is your name?        :')
name = name.strip().lower().capitalize()

age = input('how old are you?        :')
age = int(age.strip())

age_of_mother = input('if you know your mothers age, how old is she?        :')
age_of_mother = int(age_of_mother.strip())

skill1 = input('name me a skill you have?       :')
skill1 = skill1.strip().lower()

skill2 = input('can you name me another skill?      :')
skill2 = skill2.strip().lower()

skill3 = input('and another one?        :')
skill3 = skill3.strip().lower()

# Calculate age difference between response and mother
age_difference = age_of_mother - age

# Store skills in a list
skills_list = (skill1, skill2, skill3)

# Print each skill in a formated way.
print(f'\nWow {name}, I didnt know you was good at {skills_list[0]}, {skills_list[1]} and {skills_list[2]}. ')
print(f'Your mother looks good for her age at {age_of_mother}!!!. did you know your mother was only \n{age_difference} when you was born.')

# Definition of formated
 # a little context text
 # appropriate string formating like lower case or upper case, or other
# assignment to variable