from tablemaker import tablemaker

#------------Code for calculating the share--------

def calculator(names,expenses):
	
	while(1):
		print('Who paid the expense?')
		paid_person = input()
		if(paid_person not in names):
			print('Sorry, this name is not in the names mentioned. Try again.')
		else:
			break
	paid_person_id = names.index(paid_person)
	
	while(1):
		print('How much did he/she pay?')
		try:
			amount = int(input())
			# print(amount)
			if(type(num_of_names) == int and amount > 0):
				break
			else:
				print("Expenses cannot be negative. Please enter a valid amount.")
		except:
			print('Enter a proper number only')
			
	share = amount//len(names)
	for i in range(0,len(names)):
		if(expenses[paid_person_id][i] != 0):
			expenses[paid_person_id][i] -= share
			if(expenses[paid_person_id][i] < 0):
				expenses[i][paid_person_id] = abs(expenses[paid_person_id][i])
				expenses[paid_person_id][i] = 0
		else:
			expenses[i][paid_person_id] += share
		expenses[paid_person_id][paid_person_id] = 0
	return expenses
	


#------------------Main Program Begin----------------

while(1):
	try:
		num_of_names = int(input('Enter number of roommates: '))
		if(type(num_of_names) == int):
			break
	except:
		print('Enter a number only')
	
	
names = []
for i in range(0,num_of_names):
	while(1):
		print('Enter roommate #',i+1,'name:')
		temp = input()
		if(temp in names):
			print('Kindly enter a unique name. That name is already taken!')
		else:
			break
	names.append(temp)
	
	
expenses = []
for i in range(0,num_of_names):
	expenses.append([0]*num_of_names)
	
	
while(1):
	print("Choose Option:")
	print("1. Add Expense")
	print("2. Show Expenses")
	print("3. Exit Program")
	option = input()
	if(option == '1'):
		expenses = calculator(names,expenses)
	elif(option == '2'):
		tablemaker(names,expenses)
	elif(option == '3'):
		exit(0)
	else:
		print("Enter a valid option")