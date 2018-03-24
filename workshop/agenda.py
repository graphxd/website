from tabulate import tabulate

headers = ["Time", "Activity"]
day1 = [["9:00--9:30", "**Breakfast**"],
        ["9:30--10:00", "Jarrod Millman, :ref:`millman`"],
        ["10:00--10:30", "Lauren Ponisio, :ref:`ponisio`"],
        ["10:30--11:00", "Erica Newman, :ref:`newman`"],
        ["11:00--11:30", "**Tea**"],
        ["11:30--12:00", "Nick Ryder, :ref:`ryder`"],
        ["12:00--12:30", "Aaron Schild, :ref:`schild`"],
        ["12:30--2:00", "**Lunch**"],
        ["2:00--3:00", "Aric Hagberg, :ref:`hagberg`"],
        ["3:00--3:30", "Aydin Buluc, :ref:`buluc`"],
        ["3:30--4:00", "**Tea**"],
        ["4:00--4:30", "Katelyn Arnemann, :ref:`arnemann`"],
        ["4:30--5:00", "Kimon Fountoulakis, :ref:`fountoulakis`"],
        ["5:00--7:00", "BBQ"]]

day2 = [["9:00--9:30", "**Breakfast**"],
        ["9:30--10:00", "Camille Scott, :ref:`scott`"],
        ["10:00--11:00", "Rasmus Kyng, :ref:`kyng`"],
        ["11:00--11:30", "**Tea**"],
        ["11:30--12:00", "Discussion"],
        ["12:00--12:30", "Ludwig Schmidt, :ref:`schmidt`"],
        ["12:30--2:00", "**Lunch**"],
        ["2:00--3:00", "Planning"],
        ["3:00--5:00", "Self-organized activities"]]

day3 = [["9:00--9:30", "**Breakfast**"],
        ["9:30--12:30", "Self-organized activities"],
        ["12:30--1:30", "**Lunch**"],
        ["1:30--3:00", "Self-organized activities"],
        ["3:00--4:00", "Discussion"],
        ["3:30--5:00", "Reflection"]]

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
