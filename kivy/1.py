class A():
	a = 0
	def k(self, a):
		for i in range(10):
			self.a += 1
		print(self.a)

A().k()
