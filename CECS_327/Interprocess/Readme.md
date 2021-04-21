CECS 327 Interprocess Communication Assignmnet 3

April 20, 2021

Students:
- Donovan Lee
- Brian Tran

How to Run and Compile code:

    1. Download the two files and save it to your desired location.
        a. UDPClient.java
        b. UDPServer.java
    2. Open up your command prompt and search for your file location.
        a. You can do "cd FileLocationPath"
    3. In order to compile the two files do type this in your command prompt:
        a. javac UDPClient.java 
        b. javac UDPServer.java
    4. (Skip this step if you already have java SDK installed)
        a. If the lines above from Part 3 did not compile then you are missing Java SDK
            i. To check your java version just type: "java -version" in your cmd line
            ii. If no version is installed please go on the internet and look for
                java sdk.
        b. After you have downloaded Java SDK make sure to save the bin file and
            make it a environment variable
        c. After that go back to step 3 and do the same process again.
    5. After both files have been compiled please head to your router and port forward.
        a. In order to port forward you must get your router's default gateway.
            i. To get default Gateway, if your cmd prompt is still up, type "ipconfig"
            ii. Scroll down and look for Default Gateway .......... IP Address (look for a number one instead of hex decimal)
                - Ex: Good -> 192.323.321.3, Not the Right one -> 0abeascxhe
        b. Copy that Default Gateway IP address into your internet browser, then press enter.
        c. You should be brought to your router's page.
            - Make sure to hve your username and password ready to be inputted.
            - If you don't know then try admin for username, and admin for passsword as those are the defaults.
        d. Once in look for port forwarding.
        e. Once you found it set the protocol to UDP, IP address to your Public IP Address, 
            and Port number what ever you want that is in the range.
        f. Then now you have a port forward.
    5. After both files have compiled choose which file you want to run.
        a. If you want to run the server side:
            i. java UDPServer PrivateIPAddress PortNumber
            ii. java UDPClient
                - For UDPClient you will be given prompts to follow.
                - To get the Public IP Address look for a website that will get your public ip address.
    6. And now you are done setting up Server and Client Side.
    7. If you want to end the UDPClient Side just type in "quit".
        a. If you want to end the UDPServer Side hold LCTRL and press X. 