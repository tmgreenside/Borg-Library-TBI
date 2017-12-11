import mysql.connector

# This function queries the database to find the 
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

# Option #3 Query

# Option #4 Query

# Option #5 Query

# Option #6 Query

# Option #7 Query

# Option #8 Query

# Option #9 Query

# Option #10 Query

# Option #11 Query


# Option #1 Query
def findBookAuthor():
    try:
        # connection info
        usr = config.mysql['user']
        pwd = config.mysql['password']
        hst = config.mysql['host']
        dab = 'cvillagomez_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        authorName = str(raw_input("Enter the author's name: "))

        # create and execute query
        rs = con.cursor()
        # query used to retrieve the country's name, code, gdp, and inflation values
        # using constraints given in comments of function header
        query = 'SELECT a.authorName, b.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Book b ON b.ISBN = i.copy_id) JOIN AuthorCredits a USING (ISBN) WHERE a.authorName = %s GROUP BY a.authorName, b.title, lb.branchName ORDER BY NUM_COPIES DESC'
        rs.execute(query, (authorName))
        
        # print the result
        for (authorName, bookTitle, branchName, numCopies) in rs:
            print ("{} ({})".format(authorName, bookTitle, branchName, numCopies))
        print("")
        displayMenu()
        
        rs.close()
        con.close()

    except mysql.connector.Error as err:
        print (err)