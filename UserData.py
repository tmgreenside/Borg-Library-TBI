import mysql.connector
import config

# Option #3 Query
# Carlos changes
def getUserHolds():
    try:
        # connection info
##        usr = 
##        pwd = 
##        hst = 
##        dab = 
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get the user's member id
        member_id = int(raw_input("Please enter your member id: "))

        # create and execute query
        rs = con.cursor()
        # query used to display the user's current book holds in their account which returns the hold id,
        # book title, author name, and pickup deadline of the book by nearest pickup deadline date
        query = "SELECT lm.memberID, h.hold_id, b.title, a.authorName, h.hold_expiration AS PICKUP_DEADLINE FROM (LibraryMember lm JOIN Hold h USING (memberID) JOIN Inventory i USING (inventory_id) JOIN Book b ON b.ISBN = i.copy_id) JOIN AuthorCredits a USING (ISBN) WHERE lm.memberID = '" + member_id + " ' GROUP BY lm.memberID, h.hold_id, b.title, a.authorName ORDER BY PICKUP_DEADLINE ASC;"

        rs.execute(query, (member_id))

        # print the result
        print "Member ID | Hold ID | Book Title | Author Name | Pickup Deadline"
        for (memberID, holdID, bookTitle, authorName, pickupDeadline) in rs:
            print str(memberID) + " | " + str(holdID) + " | " + str(bookTitle) + " | " + str(authorName) + " | " + str(pickupDeadline)
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)
        
# Option #4 Query
# Carlos changes
def getUserRentals():
    try:
        # connection info
##        usr = 
##        pwd = 
##        hst = 
##        dab = 
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get the user's member id
        member_id = int(raw_input("Please enter your member id: "))

        # create and execute query
        rs = con.cursor()
        # query used to display the user's current book holds in their account which returns the hold id,
        # book title, author name, and pickup deadline of the book by nearest pickup deadline date
        query = "SELECT lm.memberID, r.rentalID, f.title, dc.directorName, r.returnDate AS RETURN_DATE FROM (LibraryMember lm JOIN Rental r USING (memberID) JOIN Inventory i USING (inventory_id) JOIN Film f ON f.filmID = i.copy_id) JOIN DirectorCredits dc USING (filmID) WHERE lm.memberID = '" + member_id + " ' GROUP BY lm.memberID, r.rentalID, f.title, dc.directorName ORDER BY RETURN_DATE ASC;"

        rs.execute(query, (member_id))

        # print the result
        print "Member ID | Rental ID | Film Title | Director Name | Return Date"
        for (memberID, rentalID, filmTitle, directorName, returnDate) in rs:
            print str(memberID) + " | " + str(rentalID) + " | " + str(filmTitle) + " | " + str(directorName) + " | " + str(returnDate)
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# Option #5 Query

# Option #6 Query

# Option #7 Query

# Option #8 Query

# Option #9 Query

# Option #10 Query

# Option #11 Query
