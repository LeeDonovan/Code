CECS 326 Project 4 CPU Scheduler

December 6, 2020

Students:ID
- Donovan Lee   : 016741645
- Min Kyaw      : 018182136

How to Run Code: 
    1. Unzip the package and save it to your desired location 
    2. Make sure that you are using a Linux OS to run this program
    3. Open up terminal
    4. Go to where you saved the file by doing:
        cd FileLocationPath
    5. Make sure that everything that you unzipped is in the same folder
    6. To compile any of the algorithms do:
        make rr - for round-robin scheduling
        make fcfs - for FCFS scheduling
        make priority - for priority scheduling
    7. Then to run the files that you compiled:
        ./fcfs schedule.txt
        ./rr rr-schedule.txt
        ./priority pri-schedule.txt
        (any of the schedule.txt files will work with the program)