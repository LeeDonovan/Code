Class Name
	CECS 343: Intro to Software Engineering
	Section 03/4



Professor
    Charles Siska



Project Name
    CECS343_VersionControlP3



Team Name and Members
    B2D2
    Biao Chen, Donovan Lee, Brian Tran



Intro
    -Create a repository for the given project source tree (including a “snapshot” of “all” its files) within the project
    -Enable the user to Check-in their project to save the status of it at that moment
    -Enable the user to Check-out, or download a specific version someone checked in earlier, with the help of the specific Manifest file
    -Enable the user to Add Labels for a Manifest file in a given project repo, so it will works like a nick name when user check out
    -Enable the user to List All The Labels that already assigned to the Manifest files
    -Enable the user to merge two project tree snapshots



How to Run the Program
    -In windows command line, use the cd command go to the folder that holds the project, and has the file "app.js", then type
    Node app.js
    -Then open any browser, in the url box, enter "http://localhost:3000", you will see all the functions we provide



Contents
    343-03-P2-B2D2(folder)
        App.js
	README.txt
        htmlFiles(folder)
            addLabel.html
            checkIn.html
            checkOut.html
            CreateRepo.html
            listLabels.html
            MainPage.html
        views(folder)
            listLabels.ejs


External Requirements
    Express.js
    Node.js
    Ejs


Setup and Installation
    Setup and install Node.js(windows)
        -Download Node.js: https://nodejs.org/en/
        -Install to the folder you like, but remember where you installed it.
        -Go to: My computer >> right click on any white space >> properties >> advanced system settings >> Environment Variables >> On the bottom, select “Path” >>click “Edit” >>  “New” >> put the location of your node.js (in my case it is located → D: \Programs\nodejs)
        -If it works, then go to windows command prompt and type in “node”, it should show the node version and invoke node.
    Setup and install Express.js
        In order to install express.js you need to have node.js install first
        Open cmd prompt either pressing (win + r, type cmd) or search up cmd prompt on windows search bar.
        Then in the command window type: npm install express --save
        Done
    Setup and install ejs
        In order to install ejs you need to have node.js install first
        Open up cmd prompt either pressing (win + r, type cmd) or search up cmd prompt on windows search bar.
        Then in the command window type: npm install ejs --save
        Done



Sample Invocation and results
    -Open up browser and in the url type: http://http://localhost:3000/
    You will be brought to the main page. You have a couple of different options, but the first option you want to do is click on “Create Repo Folder”, because all the other functions are depending on the fact that this process is done before them
    Create Repo
        Enter the path of your project that you want to make copies of (keep track of) into the Source Path box. Then copy and  paste the folder path that you would like to save all the copies of all of your contents into the Target Path.
        After that you will see all the contents from your source folder are copied into the target folder with special names, there will also be a manifest file that shows all of your files’ names and their corresponding Artifact ID and other informations as well
    Check in:
        Enter the path of your project that you want to make copies of (keep track of) into the Source Path box. Then copy and  paste the folder path that you already have in the create repo step for that specific project.
        After that you will see all the contents from your source folder be copied into the target folder with special names, there will also be a manifest file that shows all of your files’ names and their corresponding Artifact ID and other informations
    Check Out:
        When you want to download a specific version of a specific project, you can go to this page
        In the sourceRepoPath, enter the path you want to copy the files from, it should be the repo you created when create repo, so the files should have specific Artifact ID as their names
        In the SourceManLabel, you can either enter the actual name of a Manifest file, or its label, or nickname, which is defined in another step that we will talk about, with this file provided, the program will know which specific version of files you want to check out
        In the Target Path, it is the path you want to save the checked out files
        As a result, in your target folder, you should be able to see a folder with the same name as the repo you check out from, and inside it, it will be all the files with its original names and path at that specific moment when they are checked in
    Add Labels:
        If you want to add labels to have easy access to finding your manifest files then you would go back to MainPage and click on the “add label” link.
        You will enter the manifest file’s source path folder so it knows where to create the labels. Then add the whole manifest file name, then create one to four labels that you want the file to be associated with
        As a result, the label(s) will associate with that specific Manifest file, so when you have to provide the name of Manifest file in other steps, you can provide its labels instead, which should be shorter and easier to type
        Besides that, if you do this for the first time, a new file .manLabels.rc will be created to record the associations
    List Labels:
        The purpose of this function is to display in html format, all the man files and their corresponding labels, if you provide the repo path and submit

    Merge out:
	If you want to add merge two snapshot trees, you can use this function
	Before we start, make sure one of the snapshot you want to merge is already checked in
	Then go to the merge page, in the source path, input the path of the repo folder you checked in, in the man label, input the man label/name of the man file created during the checking in. In the target path, input the path of the project snapshot you want to merge with
	There are three possible outcomes
		All the files will be the same, then there are no collisions, you can then use the merge in link, it works exactly like check in
		Missing files in one snapshot, additional files will be copied, there is not collision, you can merge in using the merge in link
		Have file(s) with the same path but different art name (different changes to the same file in different snapshot), then the merge will have 3 copies for each collided files with different post-fix, one from common ancestor and the others two come from the two snapshot, use have to decide which one they want to keep and remove the other two copies, and rename the file without the post-fix, and the merge in
    
    Merge in:
	Only need to use this function after merge out, same function as check in



Features
    -Created clickable links for “Create Repo Folder”, “Check-in”, “Check-out”, ,“add-label”, “list-label”, "merge out" and "merge in" so the user does not need to manually type in the url links for them.
    -Users can define the project they are working on as the source, so the path to that will be the source path, and they can also decide where they are going to save the copies of their source, which is called target path. After user input “sourcePath” and “targetPath” in the create repo page, the state of the files in the source path will be copied to the target path for that specific moment and time.
    -Users are able to check in any time they want, which means they are able to save the states of their project at any moment after they already created the repo
    -Users are able to check out any version of their check-ins whenever they want, which means they can download different versions of the same project as long as they provide necessary information required, one requirement is that the create repo should already be done
    -Users are able to add labels, which means they can make nicknames for the Manifest files, which will make it much easier when they want to checkout and have to provide the Manifest files name to do that
    -Users are able to list labels, which means they can see the list of Manifest Files and their corresponding labels(nicknames), so they can just copy and paste when they need the names or labels for other functions
    -Users are able to merge two snapshot project trees, additional files will be copied, if any collision happen, they will have a chance to decide which version to keep for each collided files, and then merge in


Bugs
   We found out that we forgot to put the html files in the htmls folder in part 1 submission  last time
   Not able to send error html pages after we get inputs from the html pages, so we use the alternative of send strings not sending html files for error messages



References
    How to make an image as the background of the html page, and fill the full page
	https://www.w3schools.com/howto/howto_css_full_page.asp
    To to create directories recursively:
        https://levelup.gitconnected.com/use-node-js-to-to-create-directories-and-files-734063ce93ec
    How to loop through a dictionary in the ejs template (for listing the labels):
        https://stackoverflow.com/questions/31764552/ejs-how-to-iterate-object
    File system api
        https://nodejs.org/api/fs.html
    How to respond with a html page when user enter url
        https://codeforgeek.com/render-html-file-expressjs/
