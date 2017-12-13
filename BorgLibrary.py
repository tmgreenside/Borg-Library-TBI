import mysql.connector

# 
def branchMostCheckouts():
	try:
		# connection info
		usr = "trevapp"
		pwd = 'bowers321'
		hst = 'localhost'
		dab = 'tgreenside_DB'
		# create a connection
		con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)
		rs = con.cursor()

		query = "SELECT lb.branchName, lb.city, lb.state, COUNT(r.rentalID) AS NUM_RENTALS FROM Rental r JOIN Inventory i USING (inventory_id) JOIN LibraryBranch lb USING (branchID) GROUP BY lb.branchName, lb.city, lb.state HAVING NUM_RENTALS >= ALL (SELECT COUNT(*) FROM Rental r JOIN Inventory i USING (inventory_id) JOIN LibraryBranch lb USING (branchID) GROUP BY lb.branchName, lb.city, lb.state);"

		rs.execute(query)

		print "Branch Name | City | State | NUM_RENTALS"
		for (branchName, city, state, numRentals) in rs:
			print str(branchName) + " | " + str(city) + " | " + str(state) + " | " + str(numRentals)
		rs.close()
		con.close()

	except mysql.connector.Error as err:
		print (err)

def filmsNeverCheckedOut():
	try:
		# connection info
		usr = "trevapp"
		pwd = 'bowers321'
		hst = 'localhost'
		dab = 'tgreenside_DB'

	    # create a connection
		con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)
		rs = con.cursor()

		query = "SELECT DISTINCT f.title, f.filmLanguage, f.filmLength, f.rating, f.releaseYear, dc.directorName FROM (Inventory i LEFT OUTER JOIN Rental r USING (inventory_id) JOIN Film f ON f.filmID = i.copy_id) JOIN DirectorCredits dc USING (filmID) WHERE r.rentalID IS NULL;"

		rs.execute(query)

		print "Title | Film Language | Length | Rating | Release Year | Directed By"
		for (title, filmLanguage, filmLength, rating, releaseYear, directorName) in rs:
			print str(title) + " | " + str(filmLanguage) + " | " + str(filmLength) + " | " + str(rating) + " | " + str(releaseYear) + " | " + str(directorName)
		print ""
		rs.close()
		con.close()
	except mysql.connector.Error as err:
		print (err)

def mostPopularBook():
	try:
		# connection info
		usr = "trevapp"
		pwd = 'bowers321'
		hst = 'localhost'
		dab = 'tgreenside_DB'
		# create a connection
		con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)
		rs = con.cursor()

		query = "SELECT b.title, a.authorName, COUNT(r.rentalID) AS NUM_RENTALS FROM (Inventory i JOIN Rental r USING (inventory_id) JOIN Book b ON b.ISBN = i.copy_id) JOIN AuthorCredits a USING (ISBN) GROUP BY b.title, a.authorName HAVING NUM_RENTALS >= ALL (SELECT COUNT(*) FROM (Inventory i JOIN Rental r USING (inventory_id) JOIN Book b ON b.ISBN = i.copy_id) JOIN AuthorCredits a USING (ISBN) GROUP BY b.title, a.authorName);"

		rs.execute(query)

		print "Title | Author | Check-Outs "
		for (title, author, numRentals) in rs:
			print str(title) + " | " + str(author) + " | " + str(numRentals)

		rs.close()
		con.close()
	except mysql.connector.Error as err:
		print (err)

def addNewMember():
	print "You must use an employee login to continue."
	userEntry = raw_input("Employee ID: ")
	passEnter = raw_input("Password: ")

	try:
		# connection info
		usr = "trevapp"
		pwd = 'bowers321'
		hst = 'localhost'
		dab = 'tgreenside_DB'
		# create a connection
		con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)
		rs = con.cursor()

		query = "SELECT eid, ePassword FROM Employee WHERE eid = " + userEntry + " AND ePassword = '" + passEnter + "';"

		rs.execute(query)

		authenticated = False

		for (eid, ePassword) in rs:
			if str(eid) == str(userEntry):
				authenticated = True;

		if authenticated == False:
			print "Invalid ID or Password."
			return

		print "Authenticated.\n"
		newName = raw_input("Name: ")
		newEmail = raw_input("Email: ")
		newPass = raw_input("Password: ")

		rs.execute("SELECT * FROM LibraryMember;")

		newID = 0

		for (memberID, memberName, email, memberPassword) in rs:
			newID += 1
		newID += 1

		insert = "INSERT INTO LibraryMember VALUES (" + str(newID) + ", '" + str(newName) + "', '" + newEmail + "', '" + newPass + "');"

		rs.execute(insert)

		rs.close()
		con.close()
	except mysql.connector.Error as err:
		print (err)
