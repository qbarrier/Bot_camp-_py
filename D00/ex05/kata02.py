t = (3,30,2019,9,25)

date = (str(t[3]).zfill(2), str(t[4]).zfill(2), str(t[2]))
date = "/".join(date)


hour = (str(t[0]).zfill(2), str(t[1]).zfill(2))
hour = ":".join(hour)

print(date, hour)
