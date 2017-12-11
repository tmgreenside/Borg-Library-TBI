import mysql.connector
import config



# Option #2 Query
def findBookTitle():
        try:
        # connection info
        usr = config.mysql['user']
        pwd = config.mysql['password']
        hst = config.mysql['host']
        dab = 'cvillagomez_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)

        # get a category from the user
        bookTitle = str(raw_input("Enter the book's title: "))

        # create and execute query
        rs = con.cursor()
        # query used to retrieve the country's name, code, gdp, and inflation values
        # using constraints given in comments of function header
        query = "SELECT b.title, lb.branchName, COUNT(i.inventory_id) AS NUM_COPIES FROM (LibraryBranch lb JOIN Inventory i USING (branchID) JOIN Book b ON b.ISBN = i.copy_id) JOIN AuthorCredits a USING (ISBN) WHERE b.title = %s GROUP BY b.title, lb.branchName HAVING NUM_COPIES > 0 ORDER BY NUM_COPIES DESC"
        rs.execute(query, (bookTitle))
        
        # print the result
        for (title, branchName, numCopies) in rs:
            print ("{} ({})".format(title, branchName, numCopies))
        print("")
        displayMenu()
        
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
