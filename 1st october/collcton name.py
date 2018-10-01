stu, marks = int(input()), input().split().index("MARKS")
print (sum([int(input().split()[marks]) for x in range(stu)]) / stu)