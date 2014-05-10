class Spiral():

	def __init__ (self, side):

		self.directions = ['R','D','L','U']
		self.dir_dict = {'R': [1,0],'D': [0,1],'L': [-1,0],'U':[0,-1]}

		self.side = side
		self.matrix_size = side**2
		line = [[] for i in range(side)] 
		self.spiral_matrix = [list(line) for i in range(0, side)]
		
		self.x = self.y = side // 2

	def generate_dir_seq(self):
		times = 1
		ways = [["R", "D"], ["L", "U"]]

		self.set_n(1)
		n = 2
		
		for i in range (0, self.side - 1, 2):
			for way in ways:	
				way_coords = [ self.times_dir(times, way[0])[0], 
								self.times_dir(times, way[1])[0] ]

				for way_coord in way_coords:
					for _ in range(0, times):
						self.x += self.dir_dict[way_coord][0]
						self.y += self.dir_dict[way_coord][1]				

						self.set_n(n)
						n += 1

				times += 1
				#self.print_matrix()	

		#print ("i n ", i, n)

		for x in range (1, len(self.spiral_matrix[0])):
			self.spiral_matrix[0][x] = n
			n += 1

		return 

	def times_dir(self, t, d):
		arr = []
		for i in range(t):
			arr.append(d)

		return arr			

	def set_n (self, n):
		self.spiral_matrix[self.y][self.x] = n	

	def get_matrix(self):			
		return self.spiral_matrix

	def print_matrix(self):
		for line in self.spiral_matrix:
			print (line)

	def sum_of_diagonals(self):
		total = 0
		for x in range (self.side):
			total += self.spiral_matrix[x][x] 
			inverse = self.side - 1 - x
			total += self.spiral_matrix[inverse][x] 
		
		s = self.side // 2				
		total -= self.spiral_matrix[s][s] 
		return total
	
def main():
	side = 1337
	spiral = Spiral(side)
	#print (spiral.get_matrix())	

	spiral.generate_dir_seq()
	
	#print ( len(spiral.get_matrix()) )	
	print ("sum diag is ", spiral.sum_of_diagonals())

main()
