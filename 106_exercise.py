# Assignment2 for post class

# define an empty dictionary# name_dict = {}

# Prompt user for input for a story.
# it should have:
    # hero, beggiging, middle, end
    # 2 other things you define to be part of the story.
    # add each response to the dictionary under an appropriate key

# Print out a the dictionary information in an ordered way so we can read the story.

#defining a empty dictionary
whoever_dict = {}

#prompting user for input for story
beginning = input('Today you have a chance to create a wonderful story! \nStart by inserting the beginning of this story. \n:')
beginning = beginning.capitalize()
middle = input('Insert the middle part of this fantastic story!\n')
middle = middle.capitalize()
end = input('Finally, enter the last part of your fantastic story....\n')
end = end.capitalize()
hero = input('Who is your hero in this story? *hint* obviously Jason ...\n:')
hero = hero.strip().capitalize()
villain = input('Who is the villain in this story? *uses eye emoji* \n:')
villain = villain.strip().capitalize()
plot = input('Please enter a plot for this amazing story!\n:')
plot = plot.strip().capitalize()

# Adding user inputs for each story part into dictionary
whoever_dict['beginning'] = beginning
whoever_dict['middle'] = middle
whoever_dict['end'] = end
whoever_dict['hero'] = hero
whoever_dict['villain'] = villain
whoever_dict['plot'] = plot


view_whole_story = input('Do you want to view your whole story? (yes or no)\n:')
view_whole_story = view_whole_story.strip().lower()

if view_whole_story == 'yes':
    view_story = input('Which part of the story would you like to see? (beginning, middle or end or all) \n:')
    view_story = view_story.strip().lower()
    if view_story == 'beginning':
        print(whoever_dict['beginning'])
    if view_story == 'middle':
        print(whoever_dict['middle'])
    if view_story == 'end':
        print(whoever_dict['end'])
    if view_story == 'all':
        print(whoever_dict['beginning'], whoever_dict['middle'], whoever_dict['end'])

if view_whole_story == 'no':
    print('Thank you for your story!')

else:
    print('invalid entry!, try again!')