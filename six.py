format = input("Enter Format of time : (H/M/S) ")
if format != 'H' and format != 'M' and format != 'S':
    print("invalid input")
else:
    time = int(input("Enter Time Amount : "))
    if format == 'H':
        secs = time * 60 * 60
    elif format == 'M':
        secs = time * 60
    else:
        secs = time
    print("Seconds Calculated : "+str(secs))