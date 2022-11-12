from string import ascii_lowercase
from string import ascii_uppercase
from random import randint
from time import sleep
import math

print("Welcome to Alphaton, the programming language that only uses letters for main commands. It is case-sensitive. Type '?' for a list of commands.\n\nLatest Version: 0.7 on 12 Nov 2022")

chars = ascii_lowercase + ascii_uppercase + " .!?+-×÷\n\t"

value = 0

cell_count = 15

saved = 0
carry = 0
temp = 0

saved_string = "None"

ints = [value] * cell_count + [value] * 2
id = 0

delay = 0.1

use = True
while use:
	
	print(f"\n\nData Integer Tape:\n[{ints[id-2]},{ints[id-1]},{ints[id]},{ints[id+1]},{ints[id+2]}]\nCell No.: {id-1},{id},{id+1},{id+2},{id+3}\n\nCurrent Data Integer (Left -> Right): {id+1}\nCell Count: {cell_count}\nSaved Value: {saved}")
	
	command = input("\nMain Command Line >")
	
	for char in command:
		
		if char == "?":
			print("\nA: Adds 1 to current integer.\nS: Subtracts 1 from current integer\nM: Multiplies current integer by saved value.\nD: Floor divides the current integer by the saved value.\nm: Advanced math functions.\nr: 2 integers needed. Random number will be selected from range.\nL: Move to the next integer to the left.\nR: Move to the next integer to the right.\nP: Prints corrosponding letter of alphabet. Type '*' for the list.\np: Prints current integer value.\nI: Asks for a number. Number will replace current integer value.\ni: Asks for a number. Number will be the selected value on tape.\nE: Resets current integer to 0.\ns: Saves current number to memory\nl: Loads saved number to current position, replacing the previous.\ne: Clear saved value.\nZ: Transfers current value to the left.\nX: Transfers current value to the right.\nc: Asks for an integer. Integer will be no. of cells for memory.\nd: Asks for a float. Float will be time between instructions.\nO: Opens loop if value of integer IS NOT 0.\nC: Closes loop if value of integer IS 0. (Loops are NOT stackable)")
			
		elif char == "*":
			print("\nAlphabet list with corrosponding integer.\n\nA = 1\nB = 2\nC = 3\nD = 4\nE = 5\nF = 6\nG = 7\nH = 8\nI = 9\nJ = 10\nK = 11\nL = 12\nM = 13\nN = 14\nO = 15\nP = 16\nQ = 17\nR = 18\nS = 19\nT = 20\nU = 21\nV = 22\nW = 23\nX = 24\nY = 25\nZ = 26\nCapital letters are 27 -> 52\nSPACE = 53\n. = 54\n! = 55\n? = 56\n+ = 57\n- = 58\n× = 59\n÷ = 60\nNEW LINE = 61\nTAB = 62")
			
		elif char == "A":
			ints[id] += 1
			
		elif char == "S":
			ints[id] -= 1
			
		elif char == "M":
			ints[id] *= saved
			
		elif char == "D":
			ints[id] //= saved
			
		elif char == "m":
			print("\n1: Exponent of current value with saved value.\n2: Square root of current value as integer.\nELSE: Return to main interpreter.")
			func = input("\nChoose a math function >")
			
			if func == "1":
				ints[id] = ints[id] ** saved
				
			elif func == "2":
				ints[id] = int(math.sqrt(ints[id]))
			
		elif char == "r":
			min = int(input("\nMinimum Int >"))
			max = int(input("\nMaximum Int >"))
			
			temp = randint(min,max)
			ints[id] = temp
			
		elif char == "L":
			if id > 0:
				id -= 1
				
		elif char == "R":
			if id < cell_count - 1:
				id += 1
				
		elif char == "P":
			if 1 <= ints[id] <= len(chars):
				print(chars[ints[id]-1], end="")
				
		elif char == "p":
			print(ints[id], end="")
			
		elif char == "I":
			ask = int(input("\nEnter an integer >"))
			ints[id] = ask
		
		elif char == "i":
			ask = int(input("\nEnter a tape position >"))
			id = ask-1
			
		elif char == "E":
			ints[id] = 0
			
		elif char == "s":
			saved = ints[id]
			
		elif char == "l":
			ints[id] = saved
			
		elif char == "e":
			saved = 0
			
		elif char == "Z":
			carry = ints[id]
			ints[id] = 0
			if id > 0:
				id -= 1
			ints[id] = carry
			
		elif char == "X":
			carry = ints[id]
			ints[id] = 0
			if id < cell_count - 1:
				id += 1
			ints[id] = carry
			
		elif char == "c":
			cell_count = int(input("\nEnter a new cell count >"))
			
			ints = [value] * cell_count
			
		elif char == "d":
			delay = float(input("Enter a delay for processing >"))
	
		elif char == "O":
			if ints[id] != 0:
				loop = input("\nLoop Command Line >")
				
				done = False
				while not done:
					
					for char2 in loop:
						
						if char2 == "A":
							ints[id] += 1
			
						elif char2 == "S":
							ints[id] -= 1
								
						elif char2 == "M":
							ints[id] *= saved
			
						elif char2 == "D":
							ints[id] //= saved
							
						elif char2 == "m":
							print("\n1: Exponent of current value with saved value.\n2: Square root of current value as integer.\nELSE: Return to main interpreter.")
							func = input("\nChoose a math function >")
			
							if func == "1":
								ints[id] = ints[id] ** saved
				
							elif func == "2":
								ints[id] = int(math.sqrt(ints[id]))
							
						elif char2 == "r":
							min = int(input("\nMinimum Int >"))
							max = int(input("\nMaximum Int >"))
			
							temp = randint(min,max)
							ints[id] = temp
			
						elif char2 == "L":
							if id > 0:
								id -= 1
				
						elif char2 == "R":
							if id < cell_count - 1:
								id += 1
				
						elif char2 == "P":
							if 1 <= ints[id] <= len(chars):
								print(chars[ints[id]-1], end="")
				
						elif char2 == "p":
							print(ints[id], end="")
			
						elif char2 == "I":
							ask = int(input("\nEnter an integer >"))
							ints[id] = ask
		
						elif char2 == "i":
							ask = int(input("\nEnter a tape position >"))
							id = ask-1
			
						elif char2 == "E":
							ints[id] = 0
			
						elif char2 == "s":
							saved = ints[id]
			
						elif char2 == "l":
							ints[id] = saved
							
						elif char2 == "e":
							saved = 0
			
						elif char2 == "Z":
							carry = ints[id]
							ints[id] = 0
							if id > 0:
								id -= 1
							ints[id] = carry
			
						elif char2 == "X":
							carry = ints[id]
							ints[id] = 0
							if id < cell_count - 1:
								id += 1
							ints[id] = carry
							
						elif char2 == "c":
							cell_count = int(input("\nEnter a new cell count >"))
			
							ints = [value] * cell_count
							
						elif char2 == "d":
							delay = float(input("Enter a delay for processing >"))
						
						elif char2 == "C":
							if ints[id] == 0:
								done = True
							else:
								continue
							if id > 0 or id < cell_count - 1:
								done = True
							else:
								continue
								
						print(f"\nCurrent Loop Command: {char2}\n[{ints[id-2]},{ints[id-1]},{ints[id]},{ints[id+1]},{ints[id+2]}]\nCell No.: {id-1},{id},{id+1},{id+2},{id+3}\nPointer: {id+1}\nSaved: {saved}\nCells: {cell_count}")
						sleep(delay)
				
		print(f"\nCurrent Command: {char}\n[{ints[id-2]},{ints[id-1]},{ints[id]},{ints[id+1]},{ints[id+2]}]\nCell No.: {id-1},{id},{id+1},{id+2},{id+3}\nPointer: {id+1}\nSaved: {saved}\nCells: {cell_count}")
