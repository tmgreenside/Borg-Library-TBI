import mysql.connector

# This function queries the database to find books by Title
def findBookTitle():
    try:
        # connection info
##        usr = 'trevapp'
##        pwd = 'bowers321'
##        hst = 'localhost'
##        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        bookTitle = str(raw_input("Enter the book's title: "))

        # create and execute query
        rs = con.cursor()
        # query used to retrieve the country's name, code, gdp, and inflation values
        # using constraints given in comments of function header
        query = "SELECT a.authorName, b.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Book b ON b.ISBN = i.copy_id) JOIN AuthorCredits a USING (ISBN) WHERE b.title = '" + bookTitle + "' GROUP BY a.authorName, b.title, lb.branchName ORDER BY NUM_COPIES DESC;"

        rs.execute(query, (bookTitle))
        
        # print the result
        print "Author Name | Title | Branch Name | Num Copies"
        for (authorName, title, branchName, numCopies) in rs:
            print str(authorName) + " | " + str(title) + " | " + str(branchName) + " | " + str(numCopies)
        
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function queries the database to find books by Author
def findBookAuthor():
    try:
        # connection info
##        usr = 'trevapp'
##        pwd = 'bowers321'
##        hst = 'localhost'
##        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        authorName = str(raw_input("Enter the author's name: "))

        # create and execute query
        rs = con.cursor()
        # query used to retrieve the country's name, code, gdp, and inflation values
        # using constraints given in comments of function header
        query = "SELECT a.authorName, b.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Book b ON b.ISBN = i.copy_id) JOIN AuthorCredits a USING (ISBN) WHERE a.authorName = '" + authorName + "' GROUP BY a.authorName, b.title, lb.branchName ORDER BY NUM_COPIES DESC"
        rs.execute(query, (authorName))
        
        # print the result
        print "Author Name | Title | Branch Name | Num Copies"
        for (authorName, title, branchName, numCopies) in rs:
            print str(authorName) + " | " + str(title) + " | " + str(branchName) + " | " + str(numCopies)
        
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function searches Films by Title
def findFilmTitle():
    try:
        # connection info
##        usr = 'trevapp'
##        pwd = 'bowers321'
##        hst = 'localhost'
##        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        filmTitle = str(raw_input("Enter the film's title: "))

        # create and execute query
        rs = con.cursor()
        # query used to retrieve the country's name, code, gdp, and inflation values
        # using constraints given in comments of function header
        query = "SELECT d.directorName, f.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Film f ON f.filmID = i.copy_id) JOIN DirectorCredits d USING (filmID) WHERE f.title = '" + filmTitle + "' GROUP BY d.directorName, f.title, lb.branchName ORDER BY NUM_COPIES DESC;"

        rs.execute(query)
        
        # print the result
        print "Directpr Name | Title | Branch Name | Num Copies"
        for (directorName, title, branchName, numCopies) in rs:
            print str(directorName) + " | " + str(title) + " | " + str(branchName) + " | " + str(numCopies)
        
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function searches Films by DirectorCredits
def findFilmDirector():
    try:
        # connection info
##        usr = 'trevapp'
##        pwd = 'bowers321'
##        hst = 'localhost'
##        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        directorName = str(raw_input("Enter the director's name: "))

        # create and execute query
        rs = con.cursor()
        # query used to retrieve the country's name, code, gdp, and inflation values
        # using constraints given in comments of function header
        query = "SELECT d.directorName, f.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Film f ON f.filmID = i.copy_id) JOIN DirectorCredits d USING (filmID) WHERE d.directorName = '" + directorName + "' GROUP BY d.directorName, f.title, lb.branchName ORDER BY NUM_COPIES DESC"
        rs.execute(query)
        
        # print the result
        print "Director Name | Title | Branch Name | Num Copies"
        for (directorName, title, branchName, numCopies) in rs:
            print str(directorName) + " | " + str(title) + " | " + str(branchName) + " | " + str(numCopies)
        
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function searches Films by DirectorCredits
def findAudioArtist():
    try:
        # connection info
##        usr = 'trevapp'
##        pwd = 'bowers321'
##        hst = 'localhost'
##        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        artistName = str(raw_input("Enter the artist's name: "))

        # create and execute query
        rs = con.cursor()
        # query used to retrieve the country's name, code, gdp, and inflation values
        # using constraints given in comments of function header
        query = "SELECT a.artistName, ad.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Audio ad ON ad.audioID = i.copy_id) JOIN ArtistCredits a USING (audioID) WHERE a.artistName = '" + artistName + "' GROUP BY a.artistName, ad.title, lb.branchName ORDER BY NUM_COPIES DESC"
        rs.execute(query)
        
        # print the result
        print "Artist Name | Title | Branch Name | Num Copies"
        for (artistName, title, branchName, numCopies) in rs:
            print str(artistName) + " | " + str(title) + " | " + str(branchName) + " | " + str(numCopies)
        
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function searches Audio recordings by Title
def findAudioTitle():
    try:
        # connection info
##        usr = 'trevapp'
##        pwd = 'bowers321'
##        hst = 'localhost'
##        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        audioTitle = str(raw_input("Enter the item's title: "))

        # create and execute query
        rs = con.cursor()
        # query used to retrieve the country's name, code, gdp, and inflation values
        # using constraints given in comments of function header
        query = "SELECT a.artistName, ad.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Audio ad ON ad.audioID = i.copy_id) JOIN ArtistCredits a USING (audioID) WHERE ad.title = '" + audioTitle + "' GROUP BY a.artistName, ad.title, lb.branchName ORDER BY NUM_COPIES DESC;"

        rs.execute(query)
        
        # print the result
        print "Artist Name | Title | Branch Name | Num Copies"
        for (artistName, title, branchName, numCopies) in rs:
            print str(artistName) + " | " + str(title) + " | " + str(branchName) + " | " + str(numCopies)
        
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

def viewFullBranchInventory():
    # Carlos fill in here