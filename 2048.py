from tkinter import Frame, Label, CENTER
import logic
import constants as c

class Game2048(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.grid()
		self.master.title('2048')
		self.master.bind("<Key>",self.key_down)
		self.commands = {c.key_up: logic.move_up, c.key_down: logic.move_down, c.key_right: logic.move_right, c.key_left: logic.move_left}
		self.grid_cells = []
		self.init_grid()
		self.init_matrix()
		self.update_grid_cells()
		self.mainloop()

	def init_grid(self):
		bg = Frame(self,bg=c.bg_colour,width = c.size, height = c.size)
		bg.grid()

		for i in range(c.grid_len):
			grid_rows = []
			for j in range(c.grid_len):
				cell = Frame(bg, bg=c.bg_cell_empty, width = c.size//c.grid_len, height = c.size//c.grid_len)
				cell.grid(row = i,column = j, padx = c.grid_pad, pady = c.grid_pad)

				t = Label(master = cell, text = "", bg = c.bg_cell_empty,justify = CENTER, font = c.font,width = 5, height = 2)

				t.grid()

				grid_rows.append(t)
			self.grid_cells.append(grid_rows)

	def init_matrix(self):
		self.matrix = logic.start_game()
		logic.add_2(self.matrix)
		logic.add_2(self.matrix)

	def update_grid_cells(self):
		for i in range(c.grid_len):
			for j in range(c.grid_len):
				new_number = self.matrix[i][j]
				if new_number == 0:
					self.grid_cells[i][j].configure(text = "", bg = c.bg_cell_empty)
				else:
					self.grid_cells[i][j].configure(text = str(new_number), bg = c.bg_dict[new_number], fg = c.number_dict[new_number])

		self.update_idletasks()

	def key_down(self,event):
		key = repr(event.char)
		if key in self.commands:
			self.matrix,changed = self.commands[key](self.matrix)

			if changed:
				logic.add_2(self.matrix)
				self.update_grid_cells()
				changed =False

				if logic.get_currentstate(self.matrix) == "Won":
					self.grid_cells[1][1].configure(text = "You",bg = c.bg_cell_empty)
					self.grid_cells[1][2].configure(text = "Won!",bg = c.bg_cell_empty)

				if logic.get_currentstate(self.matrix) == "Lost":
					self.grid_cells[1][1].configure(text = "Game",bg = c.bg_cell_empty)
					self.grid_cells[1][2].configure(text = "Over",bg = c.bg_cell_empty)

gamegrid = Game2048()



