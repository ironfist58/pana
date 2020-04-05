distance = int(input('What is the distance? '))
rate = int(input('How many miles per hour are you going? '))

def bmicalulator():
	try:
		time = (distance / rate)
		hours = (time // 1)
		convert_decimals_time = (time % 1 * 60)
		seconds = 					(round(convert_decimals_time % 1 * 60))
		minutes = (round(convert_decimals_time))	
		if seconds >= 60:
			print(f"Result: {hours} Hours, {minutes} Minutes")
		if minutes <= 0:
			print(f"Hours: {hours}")		
		elif seconds <= 0:
			print(f"{minutes} Minutes")
		elif hours <= 0:
			print(f"Result: {minutes} Minutes, {seconds} Seconds")
		else:
			print(f"Result: {hours} Hours, {minutes} Minutes, {seconds} Seconds")
	except TypeError:
		print("Invalid Entry, Enter distance of miles and how fast you are going to get result!")
	return ""
		

print(bmicalulator())