"""

"""

import Inventory
import BorgLibrary
import UserData

# This function displays all main menu items and gets
# a selection from the user.
def selectMainMenu():
	options = ["Search Items", "Show User Stats", "Show Library Stats", "View Full Branch Inventories", "Add Inventory", "Add Member", "Exit"]
        
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
	print "\n"

	if selectMedium == "Book":
		for attr in bookAttrs:
			print attr
		choice = raw_input("Please select a search parameter: ").lower()
		if choice == "title":
                        print "\n"
			Inventory.findBookTitle()
		elif choice == "author":
                        print "\n"
			Inventory.findBookAuthor()
	elif selectMedium == "Film":
		for attr in filmAttrs:
			print attr
		choice = raw_input("Please select a search parameter: ").lower()
		if choice == "title":
                        print "\n"
			Inventory.findFilmTitle()
		elif choice == "director":
                        print "\n"
			Inventory.findFilmDirector()
	elif selectMedium == "Audio":
		for attr in bookAttrs:
			print attr
		choice = raw_input("Please select a search parameter: ").lower()
		if choice == "title":
                        print "\n"
			Inventory.findAudioTitle()
		elif choice == "artist":
                        print "\n"
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
	print "\n"

	selection = int(raw_input("Please enter the number for your selection: "))
	print "\n"

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
	mediums = ["Book", "Film", "Audio"]
	userOptions = ["Rental", "Hold"]
	for medium in mediums:
		print medium
	# Carlos change
	print "\n"
		
	selectMedium = raw_input("Please select from above: ")
	print "\n"

	print "Please enter your selection: "
	if selectMedium == "Book":
		for attr in userOptions:
			print attr
		choice = raw_input("Please select a search parameter: ").lower()
		if choice == str("rental"):
			print "\n"
			UserData.getUserBookRentals()
		elif choice == str("hold"):
			print "\n"
			UserData.getUserBookHolds()
		else:
			print "Invalid selection."
                        
	elif selectMedium == "Film":
		for attr in userOptions:
			print attr
		choice = raw_input("Please select a search parameter: ").lower()
		if choice == str("rental"):
			print "\n"
			UserData.getUserFilmRentals()
		elif choice == str("hold"):
			print "\n"
			UserData.getUserFilmHolds()
		else:
			print "Invalid selection."
                        
	elif selectMedium == "Audio":
		for attr in userOptions:
			print attr
		choice = raw_input("Please select a search parameter: ").lower()
		if choice == "Hold":
			print "\n"
			UserData.getUserAudioRentals()
		elif choice == "Rental":
			print "\n"
			UserData.getUserAudioHolds()
		else:
			print "Invalid selection."
                        
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
		elif choice == "Add Inventory":
			Inventory.addToInventory()
		elif choice == "Add Member":
			BorgLibrary.addNewMember()

main()