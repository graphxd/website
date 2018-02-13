from tabulate import tabulate

headers = ["Time", "Activity"]
day1 = [["9:00--9:30", "**Breakfast**"],
        ["9:30--10:00", "Welcome"],
        ["10:00--10:30", "Talk"],
        ["10:30--11:00", "Talk"],
        ["11:00--11:30", "Talk"],
        ["11:30--12:00", "Talk"],
        ["12:00--1:00", "**Lunch**"],
        ["1:00--2:00", "Talk"],
        ["2:00--2:30", "Talk"],
        ["2:30--3:00", "Talk"],
        ["3:00--3:30", "**Tea**"],
        ["3:30--5:00", "Planning"]]

day2 = [["9:00--9:30", "**Breakfast**"],
        ["9:30--10:00", "Talk"],
        ["10:00--11:00", "Talk"],
        ["11:00--11:30", "Talk"],
        ["11:30--12:00", "Talk"],
        ["12:00--1:00", "**Lunch**"],
        ["1:00--3:00", "TBD"],
        ["3:00--3:30", "**Tea**"],
        ["3:30--5:00", "TBD"]]

day3 = [["9:00--9:30", "**Breakfast**"],
        ["9:30--12:00", "TBD"],
        ["12:00--1:00", "**Lunch**"],
        ["1:00--3:00", "TBD"],
        ["3:00--3:30", "**Tea**"],
        ["3:30--5:00", "TBD"]]

print "March 27"
print "--------"
print
print tabulate(day1, headers, tablefmt="grid")
print

print "March 28"
print "--------"
print
print tabulate(day2, headers, tablefmt="grid")
print

print "March 29"
print "--------"
print
print tabulate(day3, headers, tablefmt="grid")

