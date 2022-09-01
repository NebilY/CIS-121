#(Nebil Yousuf)

human_age = float(input("Enter age: "))# Here I created an input for human age
dog_age = human_age * 7
dog_month = dog_age - int(dog_age)# So what I did was substract the the deciaml point for dog age to get dog month
dog_day = 0 #set dog day at zero 

#did the same thing
cat_age = human_age /  9
cat_month = cat_age - int(cat_age)
cat_day = 0

#did same thing
horse_age = 3*(((human_age ** 2 -47)/7)+12)

horse_month = horse_age - int(horse_age)
horse_day = 0


if dog_month != 0:# here I used if statments to set our dog days
    dog_month *= 12
    dog_day = dog_month - int(dog_month)# if our dog month is not equal to 0 we would multiply dog month with 12 and our dog_day would be dog_month substructed by the integer of dog_month
    
    if dog_day != 0:
        dog_day *= 30

if cat_month !=0:# for cat days
    cat_month *= 12
    cat_day = cat_month - int(cat_month)
    
    if cat_day != 0:
        cat_day *= 30

    
if horse_month !=0: # horse days
    horse_month *= 12
    horse_day = horse_month - int(horse_month)
    
    if horse_day != 0:
        horse_day *= 30
    
        
        
#Then we just print our values, I couldn't print the values as a float but the answer is same with the output listed on the question
print("You're age in dog years is", int(dog_age), "years", int(dog_month), "months", int(dog_day), "days")

print("You're age in cat years is", int(cat_age), "years", int(cat_month), "months", int(cat_day), "days")

print("You're age in horse years is", int(horse_age), "years", int(horse_month), "months", int(horse_day), "days")