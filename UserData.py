import mysql.connector

# This method displays all current holds for all library
# members.
def getUserBookHolds():
    try:
        # connection info
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get the user's member id
        member_id = int(raw_input("Please enter your member id: "))
        print "\n"

        # create and execute query
        rs = con.cursor()
        # query used to display the user's current book holds in their account which returns the member's id,
        # hold id, book title, author name, and pickup deadline of the book by nearest pickup deadline date
        query = "SELECT lm.memberID, h.hold_id, b.title, a.authorName, h.hold_expiration AS PICKUP_DEADLINE FROM (LibraryMember lm JOIN Hold h USING (memberID) JOIN Inventory i USING (inventory_id) JOIN Book b ON b.ISBN = i.copy_id) JOIN AuthorCredits a USING (ISBN) WHERE lm.memberID = '" + str(member_id) + " ' GROUP BY lm.memberID, h.hold_id, b.title, a.authorName ORDER BY PICKUP_DEADLINE ASC;"

        rs.execute(query, (member_id))

        # print the result
        print "Member ID | Hold ID | Book Title | Author Name | Pickup Deadline"
        for (memberID, holdID, bookTitle, authorName, pickupDeadline) in rs:
            print str(memberID) + " | " + str(holdID) + " | " + str(bookTitle) + " | " + str(authorName) + " | " + str(pickupDeadline)
        print "\n"
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This method displays films put on hold by a particular user.
def getUserFilmHolds():
    try:
        # connection info
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'

        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get the user's member id
        member_id = int(raw_input("Please enter your member id: "))
        print "\n"

        # create and execute query
        rs = con.cursor()
        # query used to display the user's current film holds in their account which returns the member's id,
        # hold id, film title, director name, and pickup deadline of the book by nearest pickup deadline date
        query = "SELECT lm.memberID, h.hold_id, m.title, dc.directorName, h.hold_expiration AS PICKUP_DEADLINE FROM (LibraryMember lm JOIN Hold h USING (memberID) JOIN Inventory i USING (inventory_id) JOIN Film m ON m.filmID = i.copy_id) JOIN DirectorCredits dc USING (filmID) WHERE lm.memberID = '" + str(member_id) + " ' GROUP BY lm.memberID, h.hold_id, m.title, dc.directorName ORDER BY PICKUP_DEADLINE ASC;"

        rs.execute(query, (member_id))

        # print the result
        print "Member ID | Hold ID | Film Title | Director Name | Pickup Deadline"
        for (memberID, holdID, filmTitle, directorName, pickupDeadline) in rs:
            print str(memberID) + " | " + str(holdID) + " | " + str(filmTitle) + " | " + str(directorName) + " | " + str(pickupDeadline)
        print "\n"
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This method displays audio titles a particular user has placed
# on hold.
def getUserAudioHolds():
    try:
        # connection info
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get the user's member id
        member_id = int(raw_input("Please enter your member id: "))
        print "\n"

        # create and execute query
        rs = con.cursor()
        # query used to display the user's current audio holds in their account which returns the hold id,
        # audio title, artist name, and pickup deadline of the audio by nearest pickup deadline date
        query = "SELECT lm.memberID, h.hold_id, a.title, ac.artistName, h.hold_expiration AS PICKUP_DEADLINE FROM (LibraryMember lm JOIN Hold h USING (memberID) JOIN Inventory i USING (inventory_id) JOIN Audio a ON a.audioID = i.copy_id) JOIN ArtistCredits ac USING (audioID) WHERE lm.memberID = '" + str(member_id) + " ' GROUP BY lm.memberID, h.hold_id, a.title, ac.artistName ORDER BY PICKUP_DEADLINE ASC;"

        rs.execute(query, (member_id))

        # print the result
        print "Member ID | Hold ID | Audio Title | Artist Name | Pickup Deadline"
        for (memberID, holdID, audioTitle, artistName, pickupDeadline) in rs:
            print str(memberID) + " | " + str(holdID) + " | " + str(audioTitle) + " | " + str(artistName) + " | " + str(pickupDeadline)
        print "\n"
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)
        
# Option #4 Query
# Carlos changes
def getUserFilmRentals():
    try:
        # connection info
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get the user's member id
        member_id = int(raw_input("Please enter your member id: "))
        print "\n"


        # create and execute query
        rs = con.cursor()
        # query used to display the user's current film rentals in their account which returns the hold id,
        # film title, director name, and pickup deadline of the film by nearest pickup deadline date
        query = "SELECT lm.memberID, r.rentalID, f.title, dc.directorName, r.returnDate AS RETURN_DATE FROM (LibraryMember lm JOIN Rental r USING (memberID) JOIN Inventory i USING (inventory_id) JOIN Film f ON f.filmID = i.copy_id) JOIN DirectorCredits dc USING (filmID) WHERE lm.memberID = '" + str(member_id) + " ' GROUP BY lm.memberID, r.rentalID, f.title, dc.directorName ORDER BY RETURN_DATE ASC;"

        rs.execute(query, (member_id))

        # print the result
        print "Member ID | Rental ID | Film Title | Director Name | Return Date"
        for (memberID, rentalID, filmTitle, directorName, returnDate) in rs:
            print str(memberID) + " | " + str(rentalID) + " | " + str(filmTitle) + " | " + str(directorName) + " | " + str(returnDate)
        print "\n"
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)
        
# Option #4 Query
# Carlos changes
def getUserBookRentals():
    try:
        # connection info
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get the user's member id
        member_id = int(raw_input("Please enter your member id: "))
        print "\n"


        # create and execute query
        rs = con.cursor()
        # query used to display the user's current book rentals in their account which returns the rental id,
        # book title, author name, and pickup deadline of the book by nearest pickup deadline date
        query = "SELECT lm.memberID, r.rentalID, b.title, ac.authorName, r.returnDate AS RETURN_DATE FROM (LibraryMember lm JOIN Rental r USING (memberID) JOIN Inventory i USING (inventory_id) JOIN Book b ON b.ISBN = i.copy_id) JOIN AuthorCredits ac USING (ISBN) WHERE lm.memberID = '" + str(member_id) + " ' GROUP BY lm.memberID, r.rentalID, b.title, ac.authorName ORDER BY RETURN_DATE ASC;"

        rs.execute(query, (member_id))

        # print the result
        print "Member ID | Rental ID | Book Title | Author Name | Return Date"
        for (memberID, rentalID, bookTitle, authorName, returnDate) in rs:
            print str(memberID) + " | " + str(rentalID) + " | " + str(bookTitle) + " | " + str(authorName) + " | " + str(returnDate)
        print "\n"
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)
        
# Option #4 Query
# Carlos changes
def getUserAudioRentals():
    try:
        # connection info
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get the user's member id
        member_id = int(raw_input("Please enter your member id: "))
        print "\n"


        # create and execute query
        rs = con.cursor()
        # query used to display the user's current film rentals in their account which returns the hold id,
        # film title, director name, and pickup deadline of the film by nearest pickup deadline date
        query = "SELECT lm.memberID, r.rentalID, a.title, ac.artistName, r.returnDate AS RETURN_DATE FROM (LibraryMember lm JOIN Rental r USING (memberID) JOIN Inventory i USING (inventory_id) JOIN Audio a ON a.audioID = i.copy_id) JOIN ArtistCredits ac USING (filmID) WHERE lm.memberID = '" + str(member_id) + " ' GROUP BY lm.memberID, r.rentalID, a.title, ac.artistName ORDER BY RETURN_DATE ASC;"

        rs.execute(query, (member_id))

        # print the result
        print "Member ID | Rental ID | Audio Title | Artist Name | Return Date"
        for (memberID, rentalID, audioTitle, artistName, returnDate) in rs:
            print str(memberID) + " | " + str(rentalID) + " | " + str(artistTitle) + " | " + str(artistName) + " | " + str(returnDate)
        print "\n"
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
