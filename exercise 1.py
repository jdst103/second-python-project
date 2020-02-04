## Guess how much points Kobe Bryant has scored in total for LA Lakers to the nearest thausand.

#define variables (anwser)
actual_points = 33643
points = 34000

#prompt user for anwser
anwser =input('Guess how much points Kobe Bryant has scored in total for LA Lakers to the nearest thausand')

###check if anwser is correct
#use operator equation and check if anwser is correct


#boolean as a question


anwser_difference = points - int(anwser)
anwser_difference == 0
print(anwser_difference == 0)
i = 0   i += 1
if anwser_difference == 0:
    print(f"You are correct! Kobe bryant scored a total of {actual_points}points between 1996 and 2016.")
    break
elif 0 < anwser_difference < 5001:
    print("so close! try a little bit lower.. ")
elif -5001 < anwser_difference < 0:
    print("so close! try a little bit higher.. ")


