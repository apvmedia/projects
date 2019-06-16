

shopping_list = []

def add_to_list(item):
	shopping_list.append(item)

def show_help():
	print("What should we pick up at the store?")
	print("""Enter 'DONE' to stop adding items. Enter 'HELP' for help.""")

new_item = " "

show_help()
while True:
	new_item = raw_input(">> ")
	if new_item == 'DONE':
		break
	elif new_item == 'HELP':
		show_help()
		continue

	add_to_list(new_item)