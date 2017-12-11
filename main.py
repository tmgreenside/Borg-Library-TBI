"""

"""

import Inventory
import BorgLibrary
import UserData

# This function displays all main menu items and gets
# a selection from the user.
def selectMainMenu():
	options = ["Search Items", "Show User Stats", "Show Library Stats", "View Full Branch Inventories", "Exit"]
        
	for i in range(len(options)):
		print str(i) + ": " + options[i]
	# Carlos change
        print "\n"
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
	# Carlos change
	print "\n"
		
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
	options = ["Which branch has most checkouts", "Which films have never been checked out", "What is the most popular book in stock"]

	for i in range(len(options)):
		print str(i) + ": " + options[i]

	selection = int(raw_input("Please enter the number for your selection: "))

	if options[selection] == "Which branch has most checkouts":
		BorgLibrary.branchMostCheckouts()
	elif options[selection] == "Which films have never been checked out":
		BorgLibrary.filmsNeverCheckedOut()
	elif options[selection] == "What is the most popular book in stock":
		BorgLibrary.mostPopularBook()
	# Carlos change
	else:
		print "Invalid selection."
		
# Carlos change
# If the user wants to view their current Rentals or Holds,
# this function allows the user to find out what holds they
# have place and their pickup deadlines or their checkouts
# and their due dates, and then calls the proper function
# from the UserData module.
def showUserStats():
    options = ["Which books has the user placed on hold", "Which films has the user checked out"]

    for i in range(len(options)):
		print str(i) + ": " + options[i]

	selection = int(raw_input("Please enter the number for your selection: "))
	if options[selection] == "Which books has the user placed on hold":
		UserData.getUserHolds()
	elif options[selection] == "Which films has the user checked out":
		UserData.getUserRentals()
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
		# Carlos change
		elif choice == "Show User Stats":
			showUserStats()
		elif choice == "Show Library Stats":
			showLibraryStats()
		elif choice == "View Full Branch Inventories":
			Inventory.viewFullBranchInventory()
		



main()
