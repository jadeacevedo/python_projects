def bodymassindex(height, weight):
    return round (( weight / height ** 2),2)
h = float(input(" enter your height in meters: "))
w = float (input( "enter your weight in kg "))
bmi = bodymassindex (h, w)
print( "your bmi is ", bmi)
if bmi <=18.5:
    print ( "you are underweight.")

elif 18.5 < bmi <= 24.9:
    print ( "your weight is normal.")
elif 25< bmi <= 29.29:
    print(" you are overweight.")
else:
    print(" you are obese.")
    
