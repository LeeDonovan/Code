CECS 326 Project 1 Multithread Programming and Synchronization

September 27, 2020

Students:ID
- Donovan Lee : 016741645
- Min Kyaw   : 018182136

How To Run Code:

    1. Unzip the package and save it to your desired location 
    1. Make sure that you are using a Linux OS to run this program
    2. Open up terminal
    3. Go to where you saved the file by doing:
        cd FileLocationPath
    4. When you get to the file's location there will be a make file that contains compiling code:
        -One for no sync: gcc -pthread main.c -o NoSync
        -One for sync: gcc -pthread -DPTHREAD_SYNC main.c -o WithSync
    5. In the terminal type in the word:
        make
    6.If make does not work then install the make package(skip this step if make works):
        sudo apt install make
    7. After compiling the file, you can now run both programs by typing these lines:
        ./NoSync anyNumber
        ./WithSync anyNumber
    
    
        
    




