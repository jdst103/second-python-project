## Guess how much points Kobe Bryant has scored in total for LA Lakers to the nearest thausand.

#define variables (anwser)
actual_points = 33643
points = 34000

#prompt user for anwser
anwser =input('Guess how much points Kobe Bryant has scored in total for LA Lakers to the nearest thausand!!')

###check if anwser is correct
#use operator equation and check if anwser is correct


#boolean as a question


anwser_difference = points - int(anwser)
anwser_difference == 0
print(anwser_difference == 0)

while anwser_difference != 0:
    anwser = input('Oh noo, try again!!')
    anwser_difference = points - int(anwser)
    print(anwser_difference == 0)

    if anwser_difference == 0:
        print(f"You are correct! Kobe bryant scored a total of {actual_points} points between 1996 and 2016.")
    if 0 < anwser_difference < 5001:
        print("so close! try a little bit lower.. ")
    if -5001 < anwser_difference < 0:
         print("so close! try a little bit higher.. ")


