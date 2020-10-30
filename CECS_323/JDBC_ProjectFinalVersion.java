package jdbcproject;
import java.sql.*;
import java.util.Scanner;
//Donovan and Frank
public class JDBCProject {

    //  Database credentials
    static String USER = "";
    static String PASS;
    static String DBNAME;
    //This is the specification for the printout that I'm doing:
    //each % denotes the start of a new field.
    //The - denotes left justification.
    //The number indicates how wide to make the field.
    //The "s" denotes that it's a string.  All of our output in this test are
    //strings, but that won't always be the case.
    static final String writingDisplayFormat = "%-25s%-35s%-25s%-20s\n";
    static final String publisherDisplayFormat = "%-25s%-45s%-25s%-30s\n";
    static final String bookDisplayFormat = "%-25s%-35s%-20s%-20s%-4s\n";
// JDBC driver name and database URL
    static final String JDBC_DRIVER = "org.apache.derby.jdbc.ClientDriver";
    static String DB_URL = "jdbc:derby://localhost:1527/";
    
    static final String INTEGER_ERROR = "Invalid input, please enter an integer!\n";
//            + "testdb;user=";
/**
 * Takes the input string and outputs "N/A" if the string is empty or null.
 * @param input The string to be mapped.
 * @return  Either the input string or "N/A" as appropriate.
 */
    public static String dispNull (String input) {
        //because of short circuiting, if it's null, it never checks the length.
        if (input == null || input.length() == 0)
            return "N/A";
        else
            return input;
    }

    public static void main(String[] args) {
        //Prompt the user for the database name, and the credentials.
        //If your database has no credentials, you can update this code to
        //remove that from the connection string.
        Scanner in = new Scanner(System.in);
        System.out.print("Name of the database (not the user account): ");
        DBNAME = in.nextLine();
        System.out.print("Database user name: ");
        USER = in.nextLine();
        System.out.print("Database password: ");
        PASS = in.nextLine();
        //Constructing the database URL connection string
        DB_URL = DB_URL + DBNAME + ";user="+ USER + ";password=" + PASS;
        Connection conn = null; //initialize the connection
        Statement stmt = null;  //initialize the statement that we're using
        try {
            //STEP 2: Register JDBC driver
            Class.forName("org.apache.derby.jdbc.ClientDriver");

            //STEP 3: Open a connection
            System.out.println("Connecting to database...");
            conn = DriverManager.getConnection(DB_URL);

            //STEP 4: Execute a query
            int choice;
            boolean flag = true;
            System.out.println("Please select from the following: ");
            
            do {
                System.out.println("1. List a database ");
                System.out.println("2. List specified data from database ");
                System.out.println("3. Insert information into data base ");
                System.out.println("4. Remove a book ");
                System.out.println("5. Quit ");
                    
                choice = checkInt(INTEGER_ERROR);
                System.out.println();
                
                while (choice < 1 || choice > 5) {
                    System.out.println("Invalid number. Please enter \"1\", \"2\", \"3\", \"4\", or \"5\".\n");
                    choice = in.nextInt();
                } 
                switch(choice) {
                    case 1: 
                        System.out.println("Which database would you like to display? ");
                        System.out.println("1. Writing  Groups ");
                        System.out.println("2. Publishers ");
                        System.out.println("3. Books\n");
                        
                        int dataBaseChoice = checkInt(INTEGER_ERROR);
                        while (dataBaseChoice < 1 || dataBaseChoice > 4) {
                            System.out.println("Invalid number. Please enter \"1\", \"2\", \"3\", \"4\", or \"5\".\n");
                            dataBaseChoice = checkInt(INTEGER_ERROR);
                        }
                        if (dataBaseChoice == 1) {
                            displayWritingGroup();
                        } else if (dataBaseChoice == 2) {
                            displayPublisher();
                        } else {
                            displayBooks();
                        }                    
                        break;
                    
                    case 2:
                        int dataChoice;
                            String dataEntry;
                            String sql;
                            String sql1;
                            String sql2;
                            boolean display = false;
                            boolean displayAtt = false;
                            
                            //Displays choices
                            System.out.println( "Which database do you want to select from? " );
                            System.out.println( "1.  Writing Groups" );
                            System.out.println( "2.  Publishers" );
                            System.out.println( "3.  Books" );
                            System.out.println( "4.  Go Back\n");
                            System.out.println();
                            
                            //Gets user input and checks validation
                            dataChoice = checkInt(INTEGER_ERROR);
                            while ( dataChoice < 1 || dataChoice > 4 ){
                                System.out.println( "Please enter \"1\", \"2\", \"3\", or \"4\".\n" );
                                dataChoice = in.nextInt();
                            }
                            
                            switch ( dataChoice ){
                                case 1:
                                    // Prompts the User 
                                    stmt = conn.createStatement();
                                    System.out.println( "Please enter the Group Name you want to display:" );
                                    dataEntry = in.nextLine();
                                    System.out.println();
                                    
                                    // Creates SQL statement and executes it.
                                    sql = "SELECT * from writinggroups WHERE groupname =" + "\'" + dataEntry +"\'";    
                                    sql1 = "SELECT * from books where groupname =" + "\'" + dataEntry +"\'";
                                    ResultSet rs = stmt.executeQuery(sql);
                                    
                                    
                                    // Goes through the result of the SQL query
                                    while(rs.next()){
                                        // Retrieve data by their name
                                        String name = rs.getString( "groupname" );
                                        String head = rs.getString( "headwriter" );
                                        String year = rs.getString( "yearformed" );
                                        String subject = rs.getString( "subject" );
                                    
                                        // If the writng group name has matched the user's input it will display.
                                        if ( name.equals( dataEntry ) ){
                                            display = true;
                                            

                                            // Displays the header of the table once
                                            if ( displayAtt == false ){
                                                System.out.printf(writingDisplayFormat, "Group Name", "Head Writer", 
                                                        "Year Formed", "Subject" );
                                                displayAtt = true;
                                            }
                                            System.out.printf(writingDisplayFormat,
                                            dispNull( name ), dispNull( head ), dispNull( year ), dispNull( subject ) );
                                        }                                                   
                                    }
                                    displayAtt = false;
                                    rs = stmt.executeQuery(sql1);
                                    System.out.println();
                                    while(rs.next()){
                                        // Retrieve data by their name
                                        String name = rs.getString( "groupname" );
                                        String bookTitle = rs.getString( "booktitle" );
                                        String bookName = rs.getString( "publishername" );
                                        String bookYear = rs.getString( "yearpublished" );
                                        String bookPages = rs.getString( "numberpages" );
                                    
                                        // If the writng group name has matched the user's input it will display.
                                        if ( name.equals( dataEntry ) ){
                                            display = true;
                                            

                                            // Displays the header of the table once
                                            if ( displayAtt == false ){
                                                System.out.printf(bookDisplayFormat, "Group Name", "Book Title", 
                                                        "Publisher Name", "Year Published", "Number of Pages" );
                                                displayAtt = true;
                                            }
                                            System.out.printf(bookDisplayFormat,
                                            dispNull( name ), dispNull( bookTitle ), dispNull( bookName ), dispNull( bookYear ), dispNull(bookPages));
                                        }                                                   
                                    }
                                    
                                    // If it did not display anything, it will display an error message
                                    if ( display == false )
                                    {
                                        System.out.println( "Sorry, " + dataEntry + " was not in the Writing Group database" );
                                    }
                                    
                                    System.out.println();                                    
                                    break;
                                    
                                case 2:
                                    
                                    stmt = conn.createStatement();
                                    System.out.println( "Please enter the Publisher you want to display" );
                                    dataEntry = in.nextLine();
                                    System.out.println();
                                    
                                    // Creates SQL statement and executes it
                                    sql= "SELECT publishername, publisheraddress, publisherphone, publisheremail FROM publishers"
                                            + " WHERE publishername =" + "\'" + dataEntry +"\'";
                                    sql1 = "SELECT * from books where publishername =" + "\'" + dataEntry +"\'";
                                    rs = stmt.executeQuery(sql);
                                    
                                    // Goes through the result of the SQL query
                                    while(rs.next())
                                    {
                                        // Retrieve data by their name
                                        String name = rs.getString("publishername");
                                        String address = rs.getString("publisheraddress");
                                        String phone = rs.getString("publisherphone");
                                        String email = rs.getString("publisheremail");
                                    
                                        // If the publisher name has matched the user's input it will display.
                                        if ( name.equals( dataEntry ) )
                                        {
                                            display = true;
                                            
                                            // Displays the header of the table once
                                            if ( displayAtt == false )
                                            {
                                                System.out.printf(publisherDisplayFormat, "Publisher Name", "Address", 
                                                        "Phone Number", "Email" );
                                                displayAtt = true;
                                            }
                                            System.out.printf(publisherDisplayFormat,
                                                dispNull(name), dispNull(address), dispNull(phone), dispNull(email));
                                        }
                                                   
                                    }
                                    
                                    displayAtt = false;
                                    rs = stmt.executeQuery(sql1);
                                    System.out.println();
                                    
                                    while(rs.next()){
                                        // Retrieve data by their name
                                        String name = rs.getString( "groupname" );
                                        String bookTitle = rs.getString( "booktitle" );
                                        String publisherName = rs.getString( "publishername" );
                                        String bookYear = rs.getString( "yearpublished" );
                                        String bookPages = rs.getString( "numberpages" );
                                    
                                        // If the writng group name has matched the user's input it will display.
                                        if ( publisherName.equals( dataEntry ) ){
                                            display = true;
                                            

                                            // Displays the header of the table once
                                            if ( displayAtt == false ){
                                                System.out.printf(bookDisplayFormat, "Group Name", "Book Title", 
                                                        "Publisher Name", "Year Published", "Number of Pages" );
                                                displayAtt = true;
                                            }
                                            System.out.printf(bookDisplayFormat,
                                            dispNull( name ), dispNull( bookTitle ), dispNull( publisherName ), dispNull( bookYear ), dispNull(bookPages));
                                        }                                                   
                                    }
                                    
                                    // Displays the error message if it did not display anything
                                    // from the database
                                    if ( display == false )
                                    {
                                        System.out.println( "Sorry, " + dataEntry + " was not in the Publisher database" );
                                    }
                                    
                                    System.out.println();
                                    break;
                                case 3:
                                                                    	
                                    stmt = conn.createStatement();
                                    System.out.println( "Please enter the Book you want to display:" );
                                    dataEntry = in.nextLine();
                                    System.out.println();
                                    
                                    // Creates SQL statement and executes it
                                    sql= "SELECT groupname, booktitle, publishername, yearpublished, numberpages"
                                    		+ " FROM books"+ " WHERE booktitle =" + "\'" + dataEntry +"\'";
                                    sql1 = "SELECT publishers.publishername, publishers.publisheraddress,publishers.publisherphone, publishers.publisheremail FROM publishers, books"
                                            + " WHERE publishers.publishername = books.publisherName AND books.booktitle=" + "\'" + dataEntry +"\'";
                                    sql2 ="SELECT writinggroups.groupname, writinggroups.headwriter,writinggroups.yearformed,writinggroups.subject from writinggroups,books"
                                            + " WHERE writinggroups.groupname = books.groupname and books.booktitle=" + "\'" + dataEntry +"\'";
                                    
                                    rs = stmt.executeQuery(sql);
                                    
                                    // Goes through the result of the SQL query

                                    while(rs.next())
                                    {
                                        // Retrieve data by their name
                                    	String groupName = rs.getString("groupname");
                                        String bookTitle = rs.getString("booktitle");
                                        String pubName = rs.getString("publishername");
                                        String year = rs.getString("yearpublished");
                                        String pages = rs.getString("numberpages");
                                    
                                        // If the book title has matched the user's input it will display.
                                        if ( bookTitle.equals( dataEntry ) )
                                        {
                                            display = true;
                                            
                                            // Displays the header of the table once
                                            if ( displayAtt == false )
                                            {
                                                System.out.printf(bookDisplayFormat, "Group Name", "Book Title", 
                                                        "Publisher Name", "Year Published", "Number of Pages" );
                                                displayAtt = true;
                                            }
                                            
                                            System.out.printf(bookDisplayFormat,
                                                dispNull(groupName), dispNull(bookTitle), dispNull(pubName), 
                                                dispNull(year), dispNull(pages) );
                                        }
                                                   
                                    }
                                    
                                    //displayAtt = false;
                                    rs = stmt.executeQuery(sql1);
                                    System.out.println();
                                    System.out.printf(publisherDisplayFormat, "Publisher Name", "Publisher Address", 
                                                        "Publisher Phone", "Publisher Email" );
                                    while(rs.next()){
                                        // Retrieve data by their name
                                        String name = rs.getString( "publishername" );
                                        String bookTitle = rs.getString( "publisheraddress" );
                                        String publisherName = rs.getString( "publisherphone" );
                                        String bookYear = rs.getString( "publisheremail" );
                           
                                    
                                        // If the writng group name has matched the user's input it will display.
//                                        if ( publisherName.equals( dataEntry ) ){
//                                            display = true;
                                            

                                            // Displays the header of the table once
//                                            if ( displayAtt == false ){
//                                                System.out.printf(bookDisplayFormat, "Group Name", "Book Title", 
//                                                        "Publisher Name", "Year Published", "Number of Pages" );
//                                                displayAtt = true;
//                                            }
                                        System.out.printf(publisherDisplayFormat,
                                        dispNull( name ), dispNull( bookTitle ), dispNull( publisherName ), dispNull( bookYear ));
                                        //}                                                   
                                    }
                                    
                                    //displayAtt = false;
                                    rs = stmt.executeQuery(sql2);
                                    System.out.println();
                                    System.out.printf(writingDisplayFormat, "Group Name", "Head Writer", 
                                                        "Year Formed", "Subject" );
                                    while(rs.next()){
                                        // Retrieve data by their name
                                        String name = rs.getString( "groupname" );
                                        String head = rs.getString( "headwriter" );
                                        String year = rs.getString( "yearformed" );
                                        String subject = rs.getString( "subject" );
                                    
                                        // If the writng group name has matched the user's input it will display.
//                                        if ( name.equals( dataEntry ) ){
//                                            display = true;
                                            

                                            // Displays the header of the table once
//                                            if ( displayAtt == false ){
//                                                System.out.printf(writingDisplayFormat, "Group Name", "Head Writer", 
//                                                        "Year Formed", "Subject" );
//                                                displayAtt = true;
//                                            }
                                        System.out.printf(writingDisplayFormat,
                                        dispNull( name ), dispNull( head ), dispNull( year ), dispNull( subject ) );
                                        //}                                                   
                                    }
                                    
                                    // If it did not display anything, it will display an error message
                                    if ( display == false )
                                    {
                                        System.out.println( "Sorry " + dataEntry + " was not in the Book database" );
                                    }
                                    
                                    System.out.println();
                                    break;
                                
                                default:
                                    System.out.println();
                                    break;
                                    
                            }
                            
                            break;
                            
                        case 3:
                            System.out.println( "What kind of information do you wish to insert into the database?" );
                            System.out.println( "1. Insert a new book" );
                            System.out.println( "2. Insert a new publisher that will replace an old publisher"
							+ " (Doing this will update the book's publisher that is being replaced)" );
                            System.out.println( "3. Go back" ); 
                            System.out.println();

                            int insertChoice = checkInt(INTEGER_ERROR);

                            // Checks user input
                            while ( insertChoice < 1 || insertChoice > 3 ){
                                System.out.println( "Sorry you did not enter a valid option." );
                                System.out.println("Please enter \"1\", \"2\", or \"3\".");
                                insertChoice = checkInt(INTEGER_ERROR);
                            }

                            // If user wants to add a new Book
                            if ( insertChoice == 1 ){
                                boolean validBook = true;
                                boolean validPub = false;
                                boolean validWriting = false;

                                String bookTitle;
                                String pubName;
                                String writerName;
                                String insertBookSQL;

                                System.out.println( "What is the name of the book you wish to add into the database?" );
                                bookTitle = in.nextLine();
                                                
                                while ( bookTitle.length() > 40 ){
                                    System.out.println( "The name of the book you wish to add is too long" );
                                    System.out.println( "Please enter a different name for " + bookTitle );
                                    bookTitle = in.nextLine();
                                }

                                // Prompts the user to enter the publisher's name. Creates
                                // and exectures a SQL statement based on user's input
                                System.out.println( "What is the publisher of your book?" );
                                pubName = in.nextLine();


                                stmt = conn.createStatement();
                                String pubSQL = "SELECT publishername FROM publishers";
                    ResultSet rs = stmt.executeQuery( pubSQL );

                                // Goes through each publisher to see if the publisher the
                                // user entered is in the database
                                while ( rs.next() ){
                                    //Retrieve by column name
                                    String pub = rs.getString( "publishername" );
                                    if ( pub.equals ( pubName ) ){
                                        validPub = true;
                                    }
                                }

                                // If the user's publisher is not in the database, it will prompt the user
                                // if they want to add it to the database or not.
                                if ( validPub == false ){
                                    int input;
                                    System.out.println( "Sorry the publisher that you entered does not exist in the database" );
                                    System.out.println( "Do you want to add it to the database?" );
                                    System.out.println( "1. Yes " );
                                    System.out.println( "2. No") ;
                                    System.out.println();
                                    input = checkInt(INTEGER_ERROR);

                                    while ( input != 1 && input != 2 ){
                                        System.out.println( "Sorry you did not enter a valid option." );
                                        System.out.println( "Please enter again." );
                                        input = checkInt(INTEGER_ERROR);
                                    }

                                    // Procedure to add the user's publisher to the database
                                    if ( input == 1 ){
                                        String pubAddress;
                                        String pubPhone;
                                        String pubEmail;
                                        // validPub becomes true since the user's publisher will now
                                        // be in the database
                                        validPub = true;

                                        // Checks the length of the user's publisher name in order to not get
                                        // any error messages for passing the length
                                        while ( pubName.length() > 20 ){
                                            System.out.println( "Sorry the name of " + pubName + " is too long." );
                                            System.out.println( "Please enter a different name for " + pubName );
                                            pubName = in.nextLine();
                                        }

                                        // Asks the user for the address of their publisher and checks validation
                                        System.out.println( "What is the address of " + pubName + "?" );
                                        pubAddress = in.nextLine();

                                        while ( pubAddress.length() > 50 ){
                                            System.out.println( "Sorry the address of " + pubName + " is too long." );
                                            System.out.println( "Please enter a different address" );
                                            pubAddress = in.nextLine();
                                        }

                                        // Asks the user for the phone number of the publisher and checks validation
                                        System.out.println( "What is the phone number of " + pubName + "?" );
                                        pubPhone = in.nextLine();

                                        while ( pubPhone.length() > 12 ){
                                            System.out.println( "Sorry the phone number of " + pubName + " is too long." );
                                            System.out.println( "Please enter a different phone number" );
                                            pubPhone = in.nextLine();
                                        }
                                        
                                        System.out.println( "What is the email of " + pubName + "?" );
                                        pubEmail = in.nextLine();

                                        while ( pubEmail.length() > 30 )
                                        {
                                            System.out.println( "Sorry the email address of " + pubName + " is too long." );
                                            System.out.println( "Please enter a email address" );
                                            pubEmail = in.nextLine();
                                        }

                                        // Creates a SQL statement based on the user's input about the publisher
                                        // and executes it
                                        stmt = conn.createStatement();
                                        String insertPubSQL = "INSERT INTO publishers (publishername, publisheraddress, "
                                                + "publisherphone, publisheremail) " + "values ( '" + pubName + "', '" 
                                                + pubAddress +"', '" + pubPhone +  "', '" + pubEmail + "')";
                                        stmt.executeUpdate(insertPubSQL);

                                        System.out.println( "The publisher " + pubName + " has been added "
                                                + "to the database." );
                                        System.out.println();
                                    }
                                }

                                // If they decide not to add their publisher, it will display an error message
                                // and redirects them to the main menu
                                if ( validPub == false )
                                {
                                    System.out.println( "Sorry you can't continue without a publisher" );
                                    System.out.println();
                                }
                                // Continues the procedure
                                else
                                {
                                    // Prompts the user to enter the writing group's name and 
                                    // creates a SQL statement and executes it.
                                    System.out.println( "What is the writing group of your book?" );
                                    writerName = in.nextLine();
                                    stmt = conn.createStatement();
                                    String writerSQL = "SELECT groupname FROM writinggroups";
                                    rs = stmt.executeQuery( writerSQL );

                                    // Goes through each writing group to see if the 
                                    // writing group the user entered is in the database                                        
                                    while ( rs.next() ){
                                        
                                        //Retrieve by column name
                                        String writer = rs.getString( "groupname" );
                                        if ( writer.equals ( writerName ) ){
                                                validWriting = true;
                                        }
                                    }

                                    // If the user's writing group is not in the database, it will display
                                    // an error message and prompt them if they want to add it into
                                    // the database
                                    if ( validWriting == false ){
                                        int input;
                                        System.out.println( "Sorry the writing group that you entered does not exist in the database" );
                                        System.out.println( "Do you want to add it to the database?" );
                                        System.out.println( "1. Yes " );
                                        System.out.println( "2. No") ;
                                        System.out.println();
                                        input = checkInt(INTEGER_ERROR);

                                        while ( input != 1 && input != 2 ){
                                            System.out.println( "Sorry you did not enter a valid option." );
                                            System.out.println( "Please enter again." );
                                            input = checkInt(INTEGER_ERROR);
                                        }
                                        // If they said yes, it will ask the writing group's information
                                        if ( input == 1 ){
                                            validWriting = true;
                                            String headWriter;
                                            int yearFormed;
                                            String checkYear;
                                            String subject;

                                            // Checks the length of the user's writing group and asks
                                            // them to enter again in order to avoid error messages
                                            // when adding.
                                            while ( writerName.length() > 20 ){
                                                System.out.println( "Sorry the name for " + writerName + " is too long." );
                                                System.out.println( "Please enter a different name for " +writerName );
                                                writerName = in.nextLine();
                                            }

                                            // Prompts the user to enter the head writer's name for their writing group
                                            // and checks for validation.
                                            System.out.println( "Who is the headWriter for " + writerName + "?" );
                                            headWriter = in.nextLine();
                                            while ( headWriter.length() > 20 ){
                                                System.out.println( "Sorry, the name of the head writer for " + writerName + " is too long." );
                                                System.out.println( "Please enter a different name for " + headWriter );
                                                headWriter = in.nextLine();
                                            }

                                            // Prompts the user to enter the year when the writing group was formed
                                            // and checks for validation.
                                            System.out.println( "What year was " + writerName + " formed?" );
                                            yearFormed = checkInt(INTEGER_ERROR);
                                            checkYear = "" + yearFormed;
                                            while ( checkYear.length() > 4 )
                                            {
                                                System.out.println( "Sorry the year when " + writerName + " formed is too long." );
                                                System.out.println( "Please enter a different year" );
                                                yearFormed = checkInt(INTEGER_ERROR);
                                                checkYear = "" + yearFormed;
                                            }

                                            // Prompts the user to enter the subject the writing group writes
                                            // and checks for validation.
                                            System.out.println( "What subject does " + writerName + " write?" );
                                            subject = in.nextLine();
                                            while ( subject.length() > 20 ){
                                                System.out.println( "Sorry, the subject that " + writerName + " writes is too long." );
                                                System.out.println( "Please enter a different subject" );
                                                subject = in.nextLine();
                                            }

                                            // Creates a SQL statement based on user's input and executes it
                                            stmt = conn.createStatement();
                                            String insertWriterSQL = "INSERT INTO writinggroups (groupname, headwriter, "
                                                    + "yearformed, subject) values ( '" + writerName + "', '" 
                                            + headWriter +"', '" + yearFormed +  "', '" + subject + "')";
                                            stmt.executeUpdate( insertWriterSQL );

                                            System.out.println( "The writing group, " + writerName + ", has been added "
                                            + "to the database.");
                                            System.out.println();
                                        }

                                    }

                                    if ( validWriting == false ){
                                        System.out.println( "Sorry you cannot continue without a writing group \n" );
                                    }
                                    else{
                                        stmt = conn.createStatement();
                                        String bookSQL = "SELECT groupname, booktitle FROM books";
                                        rs = stmt.executeQuery( bookSQL );

                                        while ( rs.next() ){
                                            String book = rs.getString( "booktitle" );
                                            String group = rs.getString( "groupname" );
                                            if ( book.equals( bookTitle ) && group.equals( writerName ) ){
                                                validBook = false;
                                            }
                                        }

                                        if ( validBook == false){
                                            System.out.println( "Sorry the book you entered already exists" );
                                            System.out.println();
                                        }
                                        else{
                                            System.out.println( "What year was this book published? (Up to 4 digits)" );
                                            int year = checkInt(INTEGER_ERROR);
                                            String checkInput = "" + year;
                                            while ( checkInput.length() > 4 ){
                                                System.out.println( "Sorry the year you entered is not valid. Please enter again" );
                                                year = checkInt(INTEGER_ERROR);
                                                checkInput = "" + year;
                                            }

                                            System.out.println( "How many pages is your book??" );
                                            int pages = checkInt(INTEGER_ERROR);
                                            checkInput = "" + pages;
                                            while ( checkInput.length() > 3 ){
                                                System.out.println( "Sorry the number of pages you entered is too long. Please enter again" );
                                                pages = checkInt(INTEGER_ERROR);
                                                checkInput = "" + pages;
                                            }

                                            stmt = conn.createStatement();
                                            insertBookSQL = " INSERT INTO Books (groupname, booktitle, publishername, yearpublished, numberpages) "
                                                            + "values ( '" + writerName + "', '" + bookTitle +"', '" + pubName + 
                                                            "', '" + year + "', '" + pages +"' )";
                                            stmt.executeUpdate( insertBookSQL );
                                        }
                                    }
                                }
                            }

                            else if ( insertChoice == 2 ){
                            	System.out.println("Enter the name of the publisher you would like to insert:");
                                String newPublisher = in.nextLine();
                                
                                System.out.println("\nEnter the name of the publisher you would like to replace:");
                                String oldPublisher = in.nextLine();
                                
                                boolean publisherInTable = false;
                                boolean newPublisherInTable = false;
                                
                                stmt = conn.createStatement();
                                String publisherSQL = "SELECT publishername FROM publishers";
                    ResultSet rs = stmt.executeQuery( publisherSQL );
                                
                                // Goes through each book title to see if the same book title
                                while (rs.next()){
                                    //Retrieve by column name
                                    String publisher = rs.getString("publishername");

                                    if(publisher.equals(oldPublisher) && !publisherInTable) {
                                        publisherInTable = true;
                                    }

                                    if(publisher.equals(newPublisher) && !newPublisherInTable) {
                                        newPublisherInTable = true;
                                    }
                                    
                                }
                                if(!newPublisherInTable) {
                                        System.out.println("New publisher not found.");
                                        System.out.println("Insert new publisher address:");
                                        String newAddress = in.nextLine();
                                        System.out.println("Insert new publisher phone number:");
                                        String newPhone = in.nextLine();
                                        System.out.println("Insert new publisher email:");
                                        String newEmail = in.nextLine();
                                        String newSql = "INSERT INTO publishers "+
                                                "VALUES ('"+newPublisher+"', '"+newAddress+"', '"+newPhone+"', '"+newEmail+"')";
                                        stmt.executeUpdate(newSql);
                               
                                    }
                                
                                if (publisherInTable == true){
                                    //Updates books from Books table to new publisher where necessary
                                    stmt = conn.createStatement();
                                    String booksSQL = "UPDATE books " +
                                            "SET publishername = '" + newPublisher +
                                            "' WHERE publishername = '" + oldPublisher + "'";
                                    stmt.executeUpdate(booksSQL);                                  
                                    
                                    //Displays the updated Books table
                                    System.out.println("Here is the updated Books table:");
                                    displayBooks();
                                } 
                                else{
                                    System.out.println("This publisher does not exist in the table."
                                            + " You will be brought back to the main menu.");
                                }
                            }
                            break;
                            
                        case 4:
                            boolean validBook = false;
                            boolean validWriting = false;

                            String bookTitle;
                            String writerName;

                            //Prompts user for book
                            System.out.println( "What is the name of the book you want to delete from the database?" );
                            bookTitle = in.nextLine();
                            stmt = conn.createStatement();
                            String bookSQL = "SELECT booktitle FROM books";
                ResultSet rs = stmt.executeQuery( bookSQL );
                            
                            // Goes through each book title to see if the same book title
                            while (rs.next()){
                                //Retrieve by column name
                                String book = rs.getString("booktitle");

                                // Sets validBook to false if the user's book title
                                // matches with a book in the database.
                                if ( book.equals ( bookTitle) ){
                                    validBook = true;
                                }
                            }

                            // If validBook is false, it will prompt a message that the book already exists and
                            // it will finish the procedure since book is a primary unique key
                            if ( validBook == false ){
                                 System.out.println( "Sorry, the book that you entered does not exist in the database. \n" );
                            }
                            else{
                                // Prompts the user to enter the writing group's name and 
                                // creates a SQL statement and executes it.
                                System.out.println( "What is the writing group of your book?" );
                                writerName = in.nextLine();
                                stmt = conn.createStatement();
                                String groupSQL;
                                groupSQL = "SELECT groupname FROM books WHERE groupname = '" + writerName +"'";
                                rs = stmt.executeQuery( groupSQL );

                                // Goes through each writing group to see if the 
                                // writing group the user entered is in the database                                        
                                while ( rs.next() ){
                                    //Retrieve by column name
                                    String writer = rs.getString( "groupname" );
                                    if ( writer.equals ( writerName ) ){
                                        validWriting = true;
                                    }
                                }

                                if ( validWriting == false ){
                                    System.out.println( "Sorry, the writing group that you entered does not exist in the database. \n" );
                                }
                                else{
                                    stmt = conn.createStatement();
                                    String deleteSQL = "DELETE FROM books WHERE booktitle = '" 
                                            + bookTitle + "' AND groupname = '" + writerName + "'";
                                    stmt.executeUpdate( deleteSQL );

                                    System.out.println( "\nYour book " + bookTitle 
                                            + " has been deleted from the database");
                                    
                                    System.out.println("\nHere is the updated Books table: \n");
                                    displayBooks();
                                }
                            }

                            break;
                            
                        case 5: //Exits the program
                            flag = false;
                            break;
                            
                        default:
                            System.out.println("Input is invalid.");
                }
            } while (flag != false);
            //STEP 6: Clean-up environment
            stmt.close();
            conn.close();
        } catch (SQLException se) {
            //Handle errors for JDBC
            se.printStackTrace();
        } catch (Exception e) {
            //Handle errors for Class.forName
            e.printStackTrace();
        } finally {
            //finally block used to close resources
            try {
                if (stmt != null) {
                    stmt.close();
                }
            } catch (SQLException se2) {
            }// nothing we can do
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException se) {
                se.printStackTrace();
            }//end finally try
        }//end try
        System.out.println("Goodbye!");
    }//end main
    
        public static void displayWritingGroup() {
            try { 
                DB_URL = DB_URL + DBNAME + ";user=" + USER + ";password=" + PASS;
                Class.forName(JDBC_DRIVER);
        
                Connection conn = DriverManager.getConnection(DB_URL);
                Statement stmt = conn.createStatement();
                String writingGroupSQL;
                writingGroupSQL = "SELECT groupname, headwriter, yearformed, subject FROM writinggroups";
                ResultSet rs = stmt.executeQuery(writingGroupSQL);
        
                System.out.println();
                System.out.printf(writingDisplayFormat, "Group name", "Head Writer", "Year Formed", "Subject\n");
        
                while (rs.next()) {
                    String name = rs.getString("groupname");
                    String writer = rs.getString("headwriter");
                    String year = rs.getString("yearformed");
                    String subject = rs.getString("subject");
             
                    System.out.printf(writingDisplayFormat, dispNull(name), dispNull(writer), dispNull(year), dispNull(subject));
                }
                System.out.println();
        
                rs.close();
                stmt.close();
                conn.close();
            } catch (SQLException se) {
                se.printStackTrace();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        
        public static void displayPublisher() {
            try { 
                DB_URL = DB_URL + DBNAME + ";user=" + USER + ";password=" + PASS;
                Class.forName(JDBC_DRIVER);
                
                Connection conn = DriverManager.getConnection(DB_URL);
                Statement stmt = conn.createStatement();
                String publisherSQL;
                publisherSQL = "SELECT publishername, publisheraddress, publisherphone, publisheremail FROM publishers";
                ResultSet rs = stmt.executeQuery(publisherSQL);
                
                System.out.println();
                System.out.printf(publisherDisplayFormat, "Publisher Name", "Publisher Address", "Publisher Phone", "Publisher Email\n");
                
                while (rs.next()) {
                    String name = rs.getString("publishername");
                    String address = rs.getString("publisheraddress");
                    String phone = rs.getString("publisherphone");
                    String email = rs.getString("publisheremail");
                    
                    System.out.printf(publisherDisplayFormat, dispNull(name), dispNull(address), dispNull(phone), dispNull(email));
                }
                System.out.println();
                
                rs.close();
                stmt.close();
                conn.close();
            } catch (SQLException se) {
                se.printStackTrace();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        
        public static int checkInt(String errorMessage){
            Scanner in = new Scanner(System.in);
            boolean valid = false;
            int validNum = 0;

            while(!valid){
                if(in.hasNextInt()){
                    // Ensures that the user's input is an integer
                    validNum = in.nextInt();
                    valid = true;
                } else{
                    // Clear buffer of junk input
                    in.next();
                    System.out.print(errorMessage);
                }
            }
            return validNum;
        }
        
        public static void displayBooks() {
            try {
                DB_URL = DB_URL + DBNAME + ";user=" + USER + ";password=" + PASS;
                Class.forName(JDBC_DRIVER);
                
                Connection conn = DriverManager.getConnection(DB_URL);
                Statement stmt = conn.createStatement();
                String booksSQL;
                booksSQL = "Select groupname, booktitle, publishername, yearpublished, numberpages FROM books";
                ResultSet rs = stmt.executeQuery(booksSQL);
                
                System.out.println();
                System.out.printf(bookDisplayFormat, "Group Name", "Book Title", "Publisher Name", "Year Published", "Number of Pages\n");
                
                while (rs.next()) {
                    String name = rs.getString("groupname");
                    String title = rs.getString("booktitle");
                    String publisher = rs.getString("publishername");
                    String year = rs.getString("yearpublished");
                    String pages = rs.getString("numberpages");
                    
                    System.out.printf(bookDisplayFormat, dispNull(name), dispNull(title), dispNull(publisher), dispNull(year), dispNull(pages));
                }
                System.out.println();
                
                rs.close();
                stmt.close();
                conn.close();
            } catch (SQLException se) {
                se.printStackTrace();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
}//end FirstExample}
