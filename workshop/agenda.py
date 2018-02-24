from tabulate import tabulate

headers = ["Time", "Activity"]
day1 = [["9:00--9:30", "**Breakfast**"],
        ["9:30--10:00", "Welcome"],
        ["10:00--10:30", "Lauren Ponisio, :ref:`ponisio`"],
        ["10:30--11:00", "Erica Newman, :ref:`newman`"],
        ["11:00--11:30", "**Tea**"],
        ["11:30--12:00", "Aaron Schild, :ref:`schild`"],
        ["12:00--12:30", "Theo McKenzie, :ref:`mckenzie`"],
        ["12:30--2:00", "**Lunch**"],
        ["2:00--3:00", "Aric Hagberg, :ref:`hagberg`"],
        ["3:00--3:30", "Aydin Buluc, :ref:`buluc`"],
        ["3:30--4:00", "**Tea**"],
        ["4:00--4:30", "Nelle Varoquaux, :ref:`varoquaux`"],
        ["4:30--5:00", "Katelyn Arnemann, :ref:`arnemann`"],
        ["5:00--7:00", "BBQ"]]

day2 = [["9:00--9:30", "**Breakfast**"],
        ["9:30--10:00", "Camille Scott, :ref:`scott`"],
        ["10:00--11:00", "Kimon Fountoulakis, :ref:`fountoulakis`"],
        ["11:00--11:30", "**Tea**"],
        ["11:30--12:00", "Rasmus Kyng, :ref:`kyng`"],
        ["12:00--12:30", "Ludwig Schmidt, :ref:`schmidt`"],
        ["12:30--2:00", "**Lunch**"],
        ["2:00--3:00", "Discussion"],
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
