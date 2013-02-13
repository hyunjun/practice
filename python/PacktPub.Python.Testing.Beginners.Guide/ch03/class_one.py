class class_one: 
	def __init__(self, arg1, arg2): 
		self.arg1 = int(arg1) 
		self.arg2 = arg2 

	def method1(self, x): 
		return x * self.arg1 

	def method2(self, x): 
		return self.method1(self.arg2) * x 
