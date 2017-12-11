"""

"""

# This function displays all main menu items and gets
# a selection from the user.
def selectMainMenu():
	options = ["Search Items", "Exit"]

	for i in range(options.length):
		print str(i) + ": " + options[i]

	selection = int(raw_input("Please enter the number for your selection: "))

	return options[selection]

# If the user selects Search Items, this function takes
# specifics of what to look for from the user and then
# calls the appropriate function from the Inventory
# module.
def searchInventory():
	mediums = ["Book", "Film", "Audio"]
	filmAttrs = ["Title", "Director"]
	bookAttrs = ["Title", "Author"]
	audioAttrs = ["Title", "Artist"]

	selectMedium = raw_input("Please select from above: ")

	if selectMedium = "Book":
		
	elif selectMedium = "Film":
	elif selectMedium = "Audio":
	else:
		print "Invalid selection."




def main():
	print "Welcome to the Borg Library System\n"

	while True:
		choice = selectMainMenu();

		if choice == "Exit":
			break
		elif choice == "Search Items":
			searchInventory()


main()