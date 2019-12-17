from datetime import date
dat1 = input("Enter date in YYYY/MM/DD : ")
dat2 = input("Enter date in YYYY/MM/DD : ")
dat1 = dat1.split('/')
dat2 = dat2.split('/')
date1 = date(int(dat1[0]),int(dat1[1]),int(dat1[2]))
date2 = date(int(dat2[0]),int(dat2[1]),int(dat2[2]))
diff = date2 - date1
print(diff.days)