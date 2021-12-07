# discreteMathematics
Projects made during discrete mathematics classes<br />

## Project 1 **school database**
Steps to run program.<br />
  ### 1. Download sqlite3 and add to env variables sqlite3.exe.
    $env:PATH += ';G:\SQLite3'
    & sqlite3.exe
    This commands should be adapted to the conditions 
  ### 2. Run sqlite3 in cmd
    Command which could be helpfull:
      .quit or .exit
      .tables - view for available databeses
      path to .db  file - run database
      .open
      .database - show databases in the current connection
      ATTACH DATABASE "path" AS name - adds name database to the current connection
    and all other commands.
  ### 3. Run file to generate databases without preapared question.
    Normally, like every  python file. By in the correct directory and run
      python .\schoolDatabase.py
  ### 4. Check tables which have been made.
    Run sequentially:
    - sqlite *path to .db file*<br />
    in sqlite bash
    - .tables<br />
    use command to format  output
    - .header on<br />
    - .mode  column<br />
    show tables which u want
    - SELECT * FROM *example*;<br />
    or specific  information
    - SELECT * FROM *example* WHERE id = 2;<br />
  ### 5. Run uncomment main from displayDB to the end like python scirpt
  
  More is [here](https://www.sqlitetutorial.net/sqlite-python/)
  
## Project 2
Project is working on example in main file. Example below:

  A B C - y<br />
  0 0 0 - 1  
  0 0 1 - 0  
  0 1 0 - 0  
  0 1 1 - 1  
  1 0 0 - 1   
  1 0 1 - 0  
  1 1 0 - 0  
  1 1 1 - 1  

## Project 3
Program implementing functions to build adjucent graph. It help for present graph theory.<br /> 
It has possible to design weight matrix, which present weight of every connection in design graph.
