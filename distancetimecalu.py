try:
    distance = int(float(input(f'\u001b[34;1mWhat is the distance of miles? \u001b[35m')))
    rate = int(float(input(f'\u001b[34;1mHow many miles per hour are your going? \u001b[35m')))
    time = (distance / rate)
    hours = (time // 1)
    convert_decimals_time = (time % 1 * 60)
    seconds = (round(convert_decimals_time % 1 * 60))
    minutes = (round(convert_decimals_time))
    if seconds >= 60:
        print(f"\u001b[30;1mResult: \u001b[31;1m{hours} Hours, \u001b[32;1m{minutes} Minutes")
    elif hours <= 0:
        print(f"\u001b[30;1mResult: \u001b[32;1m{minutes} Minutes, \u001b[33;1m{seconds} Seconds")
    elif minutes <= 0:
        print(f"\u001b[30;1mResult: \u001b[31;1m{hours} Hours")
    elif seconds <= 0:
        print(f"\u001b[30;1mResult: \u001b[32;1m{minutes} Minutes")
    else:
        print(f"\u001b[30;1mResult: \u001b[31;1m{hours} Hours, \u001b[32;1m{minutes} Minutes, \u001b[33;1m{seconds} Seconds")


except ValueError:
    print(f'\u001b[31;1mInvalid Entry, \u001b[30;1mENTER DISTANCE AND RATE IN MILES TO GET RESULT!')