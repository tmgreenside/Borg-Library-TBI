import mysql.connector

def branchMostCheckouts():
	try:
		# connection info
	    usr = 'trevapp'
	    pwd = 'bowers321'
	    hst = 'localhost'
	    dab = 'tgreenside_DB'
	    # create a connection
	    con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)
	    rs = con.cursor()

	    query = "SELECT lb.branchName, lb.city, lb.state, COUNT(r.rentalID) AS NUM_RENTALS FROM Rental r JOIN Inventory i USING (inventory_id) JOIN LibraryBranch lb USING (branchID) GROUP BY lb.branchName, lb.city, lb.state HAVING NUM_RENTALS >= ALL (SELECT COUNT(*) FROM Rental r JOIN Inventory i USING (inventory_id) JOIN LibraryBranch lb USING (branchID) GROUP BY lb.branchName, lb.city, lb.state);"

	    print "Branch Name | City | State | NUM_RENTALS"
	    for (branchName, city, state, numRentals) in rs:
	    	print branchName + " | " + city + " | " + state + " | " + numRentals
	    rs.close()
	    con.close()

    except mysql.connector.Error as err:
        print (err)