def avgGrade(students):
	sum=0.0
	for key in students:
		sum=sum+students[key]['grade']
	avg=sum/len(students)
	return avg