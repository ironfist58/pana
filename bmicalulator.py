bmi = (f"\u001b[1m\u001b[32mERROR, ENTER YOUR INCHES & WEIGHT TO GET YOUR RESULT!\u001b[0m")
def bmi_calulator():
	try:
		global bmi 
		inches = int(float(input("\u001b[34;1mWhat is your inches? ")))
		weight = int(float(input("\u001b[34;1mWhat is your weight? ")))
		bmi = (703 * weight / inches **2)
		if bmi > 25:
			print("\u001b[31;1moverweight")
		elif bmi < 18.5:
			print("\u001b[31;1munderweight")
		else:
			print("\u001b[32;1maverage")
	except ValueError:
		print("\u001b[31;1mInvalid Entry!\u001b[0m")
	return(f"\u001b[33;1mBMI> \u001b[35;1m{bmi}\u001b[0m")
print(bmi_calulator())
print("""
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater
""")