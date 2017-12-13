import mysql.connector

# This function queries the database to find books by Title
def findBookTitle():
    try:
        # connection info
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        bookTitle = str(raw_input("Enter the book's title: "))
        print "\n"

        # create and execute query
        rs = con.cursor()
        # query used to retrieve all books written by book title and the number of copies available
        # in the inventory for the book at each branch location in descending order
        query = "SELECT a.authorName, b.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Book b ON b.ISBN = i.copy_id) JOIN AuthorCredits a USING (ISBN) WHERE b.title = '" + bookTitle + "' GROUP BY a.authorName, b.title, lb.branchName ORDER BY NUM_COPIES DESC;"

        rs.execute(query, (bookTitle))
        
        # print the result
        print "Author Name | Title | Branch Name | Num Copies"
        for (authorName, title, branchName, numCopies) in rs:
            print str(authorName) + " | " + str(title) + " | " + str(branchName) + " | " + str(numCopies)

        print "\n"
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function queries the database to find books by Author
def findBookAuthor():
    try:
        # connection info
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        authorName = str(raw_input("Enter the author's name: "))
        print "\n"

        # create and execute query
        rs = con.cursor()
        # query used to retrieve all books written by author name and the number of copies available
        # in the inventory for the book at each branch location in descending order
        query = "SELECT a.authorName, b.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Book b ON b.ISBN = i.copy_id) JOIN AuthorCredits a USING (ISBN) WHERE a.authorName = '" + authorName + "' GROUP BY a.authorName, b.title, lb.branchName ORDER BY NUM_COPIES DESC"
        rs.execute(query)
        
        # print the result
        print "Author Name | Title | Branch Name | Num Copies"
        for (authorName, title, branchName, numCopies) in rs:
            print str(authorName) + " | " + str(title) + " | " + str(branchName) + " | " + str(numCopies)

        print "\n"
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function searches Films by Title
def findFilmTitle():
    try:
        # connection info
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        filmTitle = str(raw_input("Enter the film's title: "))
        print "\n"

        # create and execute query
        rs = con.cursor()
        # query used to retrieve all films by film title and the number of copies available
        # in the inventory for the film at each branch location in descending order
        query = "SELECT d.directorName, f.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Film f ON f.filmID = i.copy_id) JOIN DirectorCredits d USING (filmID) WHERE f.title = '" + filmTitle + "' GROUP BY d.directorName, f.title, lb.branchName ORDER BY NUM_COPIES DESC;"

        rs.execute(query)
        
        # print the result
        print "Director Name | Title | Branch Name | Num Copies"
        for (directorName, title, branchName, numCopies) in rs:
            print str(directorName) + " | " + str(title) + " | " + str(branchName) + " | " + str(numCopies)

        print "\n"
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function searches Films by DirectorCredits
def findFilmDirector():
    try:
        # connection info
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        directorName = str(raw_input("Enter the director's name: "))
        print "\n"

        # create and execute query
        rs = con.cursor()
        # query used to retrieve all films by director name and the number of copies available
        # in the inventory for the film at each branch location in descending order
        query = "SELECT d.directorName, f.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Film f ON f.filmID = i.copy_id) JOIN DirectorCredits d USING (filmID) WHERE d.directorName = '" + directorName + "' GROUP BY d.directorName, f.title, lb.branchName ORDER BY NUM_COPIES DESC"
        rs.execute(query)
        
        # print the result
        print "Director Name | Title | Branch Name | Num Copies"
        for (directorName, title, branchName, numCopies) in rs:
            print str(directorName) + " | " + str(title) + " | " + str(branchName) + " | " + str(numCopies)

        print "\n"
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function searches Audio by Artist
def findAudioArtist():
    try:
        # connection info
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        artistName = str(raw_input("Enter the artist's name: "))
        print "\n"

        # create and execute query
        rs = con.cursor()
        # query used to retrieve all audio by artist name and the number of copies available
        # in the inventory for the audio at each branch location in descending order
        query = "SELECT a.artistName, ad.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Audio ad ON ad.audioID = i.copy_id) JOIN ArtistCredits a USING (audioID) WHERE a.artistName = '" + artistName + "' GROUP BY a.artistName, ad.title, lb.branchName ORDER BY NUM_COPIES DESC"
        rs.execute(query)
        
        # print the result
        print "Artist Name | Title | Branch Name | Num Copies"
        for (artistName, title, branchName, numCopies) in rs:
            print str(artistName) + " | " + str(title) + " | " + str(branchName) + " | " + str(numCopies)

        print "\n"        
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function searches Audio recordings by Title
def findAudioTitle():
    try:
        # connection info
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        audioTitle = str(raw_input("Enter the item's title: "))

        # create and execute query
        rs = con.cursor()
        # query used to retrieve all audio by audio title and the number of copies available
        # in the inventory for the audio at each branch location in descending order
        query = "SELECT a.artistName, ad.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Audio ad ON ad.audioID = i.copy_id) JOIN ArtistCredits a USING (audioID) WHERE ad.title = '" + audioTitle + "' GROUP BY a.artistName, ad.title, lb.branchName ORDER BY NUM_COPIES DESC;"

        rs.execute(query)
        
        # print the result
        print "Artist Name | Title | Branch Name | Num Copies"
        for (artistName, title, branchName, numCopies) in rs:
            print str(artistName) + " | " + str(title) + " | " + str(branchName) + " | " + str(numCopies)

        print "\n"
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function displays the entire inventory, limited to user's choice
# of medium, that a particular branch carries. 
def viewFullBranchInventory():
    try:
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)
        mediums = ["Book", "Film", "Audio"]
        mediums2 = ["ID: 1 = Wonderville Public Library", "ID: 2 = Nowhereville Public Library", "ID: 3 = Everywhereville Public Library"]

        for medium in mediums:
            print medium
        # Carlos change
        print "\n"
        
        selectMedium = raw_input("Please select from above: ")
        print "\n"

        for medium1 in mediums2:
            print medium1
        # Carlos change
        print "\n"

        if selectMedium == "Book":
            # get a category from the user
            libraryBranch = raw_input("Please enter ID number corresponding to library branch: ")
            print "\n"

                        # create and execute query
            rs = con.cursor()
                        # query used to retrieve the audio and their number of copies available in the inventory by library
                        # and displays the artist name, audio title, library branch, condition, and number of Audio inventory 
                        # items and orders them by number of copies in descending order
            query = "SELECT b.title, a.authorName, COUNT(i.copy_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Book b ON b.ISBN = i.copy_id) JOIN AuthorCredits a USING (ISBN) WHERE lb.branchID = '" + str(libraryBranch) + "' GROUP BY b.title, a.authorName ORDER BY NUM_COPIES DESC;"
            rs.execute(query)

                        # print the result
            print "Title | Author Name | Num Copies"
            for (title, authorName, numCopies) in rs:
                print str(title) + " | " + str(authorName) + " | " + str(numCopies)
             
        elif selectMedium == "Film":
            # get a category from the user
            libraryBranch = raw_input("Please enter ID number corresponding to library branch: ")
            print "\n"

                        # create and execute query
            rs = con.cursor()
                        # query used to retrieve the audio and their number of copies available in the inventory by library
                        # and displays the artist name, audio title, library branch, condition, and number of Audio inventory 
                        # items and orders them by number of copies in descending order
            query = "SELECT f.title, dc.directorName, COUNT(i.copy_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Film f ON f.filmID = i.copy_id) JOIN DirectorCredits dc USING (filmID) WHERE lb.branchID = '" + str(libraryBranch) + "' GROUP BY f.title, dc.directorName ORDER BY NUM_COPIES DESC;"
            rs.execute(query)

                        # print the result
            print "Title | Director Name | Num Copies"
            for (title, directorName, numCopies) in rs:
                print str(title) + " | " + str(directorName) +  " | " + str(numCopies)
        
        elif selectMedium == "Audio":
            # get a category from the user
            libraryBranch = raw_input("Please enter ID number corresponding to library branch: ")
            print "\n"

                        # create and execute query
            rs = con.cursor()
                        # query used to retrieve the audio and their number of copies available in the inventory by library
                        # and displays the artist name, audio title, library branch, condition, and number of Audio inventory 
                        # items and orders them by number of copies in descending order
            query = "SELECT ad.title, a.artistName, COUNT(i.copy_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Audio ad ON ad.audioID = i.copy_id) JOIN ArtistCredits a USING (audioID) WHERE lb.branchID = '" + str(libraryBranch) + "' GROUP BY ad.title, a.artistName ORDER BY NUM_COPIES DESC;"
            rs.execute(query)

                        # print the result
            print "Title | Artist Name | Num Copies"
            for (title, artistName, numCopies) in rs:
                print str(title) + " | " + str(artistName) + " | " + str(numCopies)

        else:
            print "Invalid selection."

        print "\n"
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)
        
# This function adds a book to a branch inventory.
def addBook():
    try:
        # connection info
        # usr = 'cvillagomez'
        # pwd = 'cvillagomez79849078'
        # hst = '147.222.163.1'
        # dab = 'cvillagomez_DB'
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)
        
        newISBN = raw_input("Enter the book's ISBN: ")
        newTitle = raw_input("Enter the book's title: ")
        newReleaseYear = raw_input("Enter the book's release year: ")
        newBookLanguage = raw_input("Enter the book's language: ")
        newBookPublisher = raw_input("Enter the book's publisher: ")
        newAuthorName = raw_input("Enter the author's name: ")

        rs = con.cursor(buffered=True)

        rs.execute("SELECT * FROM Book;")
        rs.execute("SELECT * FROM AuthorCredits;")
        
        insert = "INSERT INTO Book VALUES (" + str(newISBN) + ", '" + str(newTitle) + "', '" + str(newReleaseYear) + "', '" + str(newBookLanguage) + "', '" + str(newBookPublisher) + "');"
        insert2 = "INSERT INTO AuthorCredits VALUES (" + str(newISBN) + ", '" + str(newAuthorName) + "');"
                
        rs.execute(insert)
        rs.execute(insert2)
        
        con.commit()
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function adds an audio recording to a branch inventory.    
def addAudio():
    try:
        # connection info
        # usr = 'cvillagomez'
        # pwd = 'cvillagomez79849078'
        # hst = '147.222.163.1'
        # dab = 'cvillagomez_DB'
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)
        
        newAudioID = raw_input("Enter the audio's ID: ")
        newTitle = raw_input("Enter the audio's title: ")
        newGenre = raw_input("Enter the audio's genre: ")
        newAudioLanguage = raw_input("Enter the audio's language: ")
        newRecordLabel = raw_input("Enter the audio's record label: ")  
        newReleaseYear = raw_input("Enter the audio's release year: ")
        newArtistName = raw_input("Enter the artist's name: ")

        rs.execute("SELECT * FROM Audio;")
        rs.execute("SELECT * FROM ArtistCredits;")

        insert = "INSERT INTO Audio VALUES (" + str(newAudioID) + ", '" + str(newTitle) + "', '" + str(newGenre) + "', '" + str(newAudioLanguage) + "', '" + str(newRecordLabel) + "', '" + str(newReleaseYear) + "');"
        insert2 = "INSERT INTO ArtistCredits VALUES (" + str(newAudioID) + str(newArtistName) + "');"

        rs.execute(insert)
        rs.execute(insert2)

        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function adds a film to Film records.
def addFilm():
    try:
        # connection info
        # usr = 'cvillagomez'
        # pwd = 'cvillagomez79849078'
        # hst = '147.222.163.1'
        # dab = 'cvillagomez_DB'
        usr = 'trevapp'
        pwd = 'bowers321'
        hst = 'localhost'
        dab = 'tgreenside_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)
        
        newFilmID = raw_input("Enter the film's ID: ")
        newTitle = raw_input("Enter the film's title: ")
        newFilmLanguage = raw_input("Enter the film's language: ")
        newFilmLength = raw_input("Enter the film's length: ")
        newRating = raw_input("Enter the film's rating: ")
        newReleaseYear = raw_input("Enter the film's release year: ")
        newDirectorName = raw_input("Enter the director's name: ")

        rs.execute("SELECT * FROM Film;")
        rs.execute("SELECT * FROM DirectorCredits;")
        
        insert = "INSERT INTO Film VALUES (" + str(newFilmID) + ", '" + str(newTitle) + "', '" + str(newFilmLanguage) + "', '" + str(newFilmLength) + "', '" + str(newRating) + "', '" + str(newReleaseYear) + "');"
        insert2 = "INSERT INTO DirectorCredits VALUES (" + str(newFilmID) + ", '" + str(newDirectorName) + "');"

        rs.execute(insert)
        rs.execute(insert2)

        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)

# This function calls either addBook, addFilm, or addAudio
# per the user choice to add an item to a particular branch
# inventory.
def addToInventory():
    print "You must use an employee login to continue."
    userEntry = raw_input("Employee ID: ")
    passEnter = raw_input("Password: ")
    try:
        # connection info
        # usr = 'cvillagomez'
        # pwd = 'cvillagomez79849078'
        # hst = '147.222.163.1'
        # dab = 'cvillagomez_DB'
        usr = 'trevapp'
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
    
        mediums = ["Book", "Film", "Audio"]

        for medium in mediums:
            print medium
        # Carlos change
        print "\n"
        
        selectMedium = raw_input("Please select from above: ")
        print "\n"

        if selectMedium == "Book":
            addBook()
            newInventory_id = raw_input("Enter the inventory's ID: ")
            newCopy_id = raw_input("Enter the book's ISBN: ")
            newItemFormat = "Book"
            newItemCondition = raw_input("Enter the book's condition: ")
            newBranchID = raw_input("Enter the library branch's ID that has the book: ")

            insertion = "INSERT INTO Inventory VALUES (" + str(newInventory_id) + "," + str(newCopy_id) + ",'" + str(newItemFormat) + "', '" + str(newItemCondition) + "'," + str(newBranchID) + ");"
            # print insertion
            rs.execute(insertion)
                        #UNREAD RESULT FOUND MESSAGE DISPLAYS AFTER ENTERING ALL USER INPUT
            #NEED TO FIGURE OUT WHY NEW BOOK IS NOT DISPLAYED IN INVENTORY AFTER BEING ADDED
        elif selectMedium == "Film":
            addFilm()
            newInventory_id = raw_input("Enter the inventory's ID: ")
            newCopy_id = raw_input("Enter the film's ID: ")
            newItemFormat = "Film"
            newItemCondition = raw_input("Enter the film's condition: ")
            newBranchID = raw_input("Enter the library branch's ID that has the film: ")
            insertion = "INSERT INTO Inventory VALUES (" + str(newInventory_id) + "," + str(newCopy_id) + ",'" + str(newItemFormat) + "', '" + str(newItemCondition) + "'," + str(newBranchID) + ");"
            # print insertion
            rs.execute(insertion)
        
        elif selectMedium == "Audio":
            addAudio()
            newInventory_id = raw_input("Enter the inventory's ID: ")
            newCopy_id = raw_input("Enter the audio's ID: ")
            newItemFormat = "Audio"
            newItemCondition = raw_input("Enter the audio's condition: ")
            newBranchID = raw_input("Enter the library branch's ID that has the audio: ")
            insertion = "INSERT INTO Inventory VALUES (" + str(newInventory_id) + "," + str(newCopy_id) + ",'" + str(newItemFormat) + "', '" + str(newItemCondition) + "'," + str(newBranchID) + ");"
            # print insertion
            rs.execute(insertion)

        else:
            print "Invalid selection."
    
        con.commit()
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)