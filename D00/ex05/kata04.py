t = (0, 4, 132.42222, 10000, 12345.67)
day = "day_" + str(t[0]).zfill(2)
ex = "ex_" + str(t[1]).zfill(2)
three = round(t[2], 2)
four = "{:.2e}".format(t[3])
five = "{:.2e}".format(t[4])

print(day + ", " + ex + " :", str(three) + ", " + str(four) + ", " + str(five))
