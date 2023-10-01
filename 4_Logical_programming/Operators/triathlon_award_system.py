# retrieve inputs from the user
swimming = float(input("How long did it take you to finish the swimming in minutes? "))
cycling = float(input("How long did it take you to finish the cycling in minutes? "))
running = float(input("How long did it take you to finish the running in minutes? "))

# calculate and display the total time taken to complete the triathlon
time = swimming + cycling + running
print(f"It took you {time} minutes to complete the triathlon!")

# calculate and display the award earned
if time <= 100:
    award = "Provincial Colours"
elif time <= 105:
    award = "Provincial Half Colours"
elif time <= 110:
    award = "Provincial Scroll"
else:
    award = "No award"

print(f"You receive: {award}")