"""

"""

import Inventory

# This function displays all main menu items and gets
# a selection from the user.
def selectMainMenu():
	options = ["Search Items", "Show Holds", "Show Library Stats", "Exit"]

	for i in range(len(options)):
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

	for medium in mediums:
		print medium
	selectMedium = raw_input("Please select from above: ")

	if selectMedium == "Book":
		for attr in bookAttrs:
			print attr
		choice = raw_input("Please select a search parameter: ").lower()
		if choice == "title":
			Inventory.findBookTitle()
		elif choice == "author":
			Inventory.findBookAuthor()
	elif selectMedium == "Film":
		for attr in filmAttrs:
			print attr
		choice = raw_input("Please select a search parameter: ").lower()
		if choice == "title":
			Inventory.findFilmTitle()
		elif choice == "director":
			Inventory.findFilmDirector()
	elif selectMedium == "Audio":
		for attr in bookAttrs:
			print attr
		choice = raw_input("Please select a search parameter: ").lower()
		if choice == "title":
			Inventory.findAudioTitle()
		elif choice == "artist":
			Inventory.findAudioArtist()
	else:
		print "Invalid selection."

# If the user wants to view Library Stats, this function
# allows the user to tell which stats to view, and then
# calls the proper function from the BorgLibrary module.
def showLibraryStats():
	options = ["Which branch has most checkouts"]

	for i in range(len(options)):
		print str(i) + ": " + options[i]

	selection = int(raw_input("Please enter the number for your selection: "))

	if options[selection] == "Which branch has most checkouts":
		BorgLibrary.branchMostCheckouts()



def main():
	print "Welcome to the Borg Library System\n"

	while True:
		choice = selectMainMenu();

		if choice == "Exit":
			break
		elif choice == "Search Items":
			searchInventory()
		elif choice == "Show Library Stats":
			showLibraryStats()



main()