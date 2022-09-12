from prop.calculate_monthly import calculate_monthly
class main_task(calculate_monthly):
	def __init__(self, month_salary:[int], elec=100, water_bills=100, other_bills=150, rise_percentage=0, for_harchene=50, semester=400, semester_years=4.5) -> [int, int, int, int, int]:
		# average elec, average water bills and other bills.
		self.month_salary = month_salary; self.elec = elec; self.water_bills = water_bills; self.other_bills = other_bills; self.rise_percentage = rise_percentage; self.for_harchene = for_harchene; self.semester = semester; self.semester_years = semester_years
		calculate_monthly.__init__(self)
	def run(self):
		actual_salary = self.month_salary
		final = []
		weekx = []
		for indexs, times in enumerate(range(self.semester_years), 1):
			if len(weekx) == 4:
				if len(final) != 0:
					add = final[len(final)-1][1]
				else:
					add = 0
				temp = actual_salary + add
				if self.rise_percentage != 0:
					self.total[0][0] = (self.total[0][0]+self.rise_percentage/100)
					self.rise_percentage += 1
				temp = (temp-self.total[0][0]) - self.for_harchene
				sum = temp
				sum -= self.semester
				final.append((times, sum))
				weekx = []
			weekx.append(times)
		total = 0
		for items, income in final:
			total += income
		print("\r\x0A".join("%d. - %d"%(semester, income) for semester, income in final) + "\r\x0A\r\x0ATotal: %d, Months: %d, Salary: %d, Semester: %d"%(total, self.semester_years/4.345, self.month_salary, self.semester))
xz = main_task(month_salary=400, elec=50, water_bills=50, other_bills=50, rise_percentage=1, for_harchene=20, semester=200, semester_years=51)