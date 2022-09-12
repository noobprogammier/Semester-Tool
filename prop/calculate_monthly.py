class calculate_monthly(object):
	def __init__(self):
		self.total = [[(self.elec + self.water_bills + self.other_bills)], self.elec, self.water_bills, self.other_bills]
		self.totalsal = [(self.month_salary * 12), self.month_salary]
		self.run()