
from tkinter import *

import boggle_Solve


import random

# A conventional boggle grid is 4 x 4
SIZE = 4

alphabet = \
	"AAAAAABBCCDDDEEEEEEEEEEEFFGGHHHHHIIIIIIJKLLLLMM"+\
	"NNNNNNOOOOOOOPPQRRRRRSSSSSSTTTTTTTTTUUUVVWWWXYYYZ"


class Display(Frame):

	def __init__(self, root):

		Frame.__init__(self, root)

		self.grid()

		self.display_text = \
				Text(right_side, height = 10, width = SIZE*SIZE, \
				font = ("courier new", 16))
		self.display_text.grid(row=0, column=0)

		self.word_list = []



	def display_words(self, set_of_words):

		self.clear()
		words = set_of_words

		words.sort()

		words.sort(key=lambda x:len(x), reverse=True)

		self.word_list = words


		for word in words:
			self.display_text.insert(END, word+'\n')



	def clear(self):
		self.display_text.delete("0.0", END)

	def alpha_sort(self):

		self.clear()

		words = sorted(self.word_list)

		for word in words:
			self.display_text.insert(END, word+'\n')


class Board(Frame):

	def __init__(self, root, display):
		Frame.__init__(self, root)

		self.grid()

		self.entries = []
		for i in range(SIZE):
			self.entries.append([])
			for j in range(SIZE):
				contents = StringVar()
				e = Entry(text=contents, font = ("courier new", 36), width=1)
				e.grid(row = i, column = j, padx = 16)
				self.entries[-1].append(e)

	def clear(self):

		for listy in self.entries:
			for entry in listy:
				entry.delete(0, END)

		display.clear()

		display.word_list = []


	def random_board(self):

		for listy in self.entries:
			for entry in listy:
				entry.delete(0, END)
				entry.insert(0, random.choice(alphabet))

		display.clear()


	def find_words(self):

		array_of_letters = []
		for listy in self.entries:
			col = []
			for entry in listy:
				letter = entry.get()

				if len(letter) > 1:
					display.display_words\
						(["some entries\ncontain more\nthan one\ncharacter"])
					return

				col.append(letter)
			array_of_letters.append(col)

		display.display_words(boggle_Solve.findWords(array_of_letters))



class Controls(Frame):

	def __init__(self, root, board, display):
		Frame.__init__(self, root)
		self.grid()

		start_button = \
			Button(self, text="find words", command=board.find_words)

		clear_button = Button(self, text = "clear", command=board.clear)
		
		random_button = \
			Button(self, text="random", command=board.random_board)

		sort_alpha_button = Button\
			(self, text="sort alphabetically", command=display.alpha_sort)

		start_button.grid(row = 0, column = 2)
		clear_button.grid(row = 0, column = 1)
		random_button.grid(row = 0, column = 0)
		sort_alpha_button.grid(row = 0, column = 3)



if __name__ == '__main__':


	root = Tk()
	root.title("Boggle Solver")

	upper_left = Frame(root)
	upper_left.grid(row = 0)
	lower_left = Frame(root)
	lower_left.grid(row = SIZE,columnspan = SIZE*2)
	right_side = Frame(root)
	right_side.grid(row = 0, rowspan = SIZE, column = SIZE)


	display = Display(right_side)
	board = Board(upper_left, display)
	controls = Controls(lower_left, board, display)

	root.mainloop()