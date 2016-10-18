#!/usr/bin/env python3

from os import system
#from curses import wrapper
#from curses import textpad
import curses
import subprocess
import os
#import glob
import getpass


#log viewer bash script
script="""""""""
file="/home/$USER/.fallterm/path.txt"
read -d $'\x04' path < "$file"
echo "Please choose a log to view"
echo "---------------------------"
echo " "
select d in $(find /home/$USER/$path  -maxdepth 1 -not -name ".*" -type f| sort -r) quit; do
    		if [ "$d" != "quit" ]; then
		quit=$quit

        	less $d
	        elif [ "$d" == quit  ];then
		break 1
    		fi
	   done
"""""""""

##################################





#New log script
newfile ="""""""""""
            file="/home/$USER/.fallterm/path.txt"
            read -d $'\x04' path < "$file"
            file2="/home/$USER/.fallterm/company.txt"
            read -d $'\x04' company < "$file2"
	    now=`date +"%m_%d_%Y_%H_%M"`
	    new_file=$now
	    #touch home/$USER/$path/log_$new_file
            echo "                               $company\n" > /home/$USER/$path/log_$new_file
	    echo "Log Entry- $new_file\n" >> /home/$USER/$path/log_$new_file

	    vi /home/$USER/$path/log_$new_file

"""""""""""
#################################





#remove file script
rmfile ="""""""""
echo "Please choose a log to delete from this machine"
echo "---------------------------"
echo " "
file="/home/$USER/.fallterm/path.txt"
read -d $'\x04' path < "$file"

select d in $(find /home/$USER/$path  -maxdepth 1 -not -name ".*" -type f| sort -r ) quit; do
    		if [ "$d" != "quit" ]; then
		quit=$quit

        	rm $d

			if [ $? -eq 0 ];then
                	echo "You have successfully deleted "$d" "
                        sleep 2
                        echo "Press Enter to choose another file"
                        sleep 3

                        break
                        continue

                	fi

	        elif [ "$d" == quit  ];then
		break 1
    		fi
	   done
"""""""""
##################################
#Get the curdirpath
curdirpath="""""""""
file="/home/$USER/.fallterm/path.txt"
read -d $'\x04' path < "$file"
echo "Your current working directory is "$path""
echo "---------------------------"
ls -d /home/$USER/ */


"""""""""


#####################################
#default printer script, allows user to set the default printer
printer="""""""""

echo "Please choose a printer you would like to make default"
echo "---------------------------"
echo " "
select d in $(lpstat -a | cut -f1 -d " " ) quit; do
    		if [ "$d" != "quit" ]; then
		quit=$quit

        	lpoptions -d $d > /dev/null 2>&1
                if [ $? -eq 0 ]; then
                echo "You have successfully set $d as your default printer"
                fi
	        elif [ "$d" == quit  ];then
		break 1
    		fi
done


"""""""""


#######################################
#print file script
printfile="""""""""
echo "Please choose a log to print to the default printer"
echo "---------------------------"
echo " "
file="/home/$USER/.fallterm/path.txt"
read -d $'\x04' path < "$file"

select d in $(find /home/$USER/$path  -maxdepth 1 -not -name ".*" -type f| sort -r ) quit; do
    		if [ "$d" != "quit" ]; then
		quit=$quit
                lp $d
               	   if [ $? -eq 0 ]; then
                      echo "You have successfully sent $d to the printer"
                   fi
	        elif [ "$d" == quit  ];then
		   break 1
    		fi
done
"""""""""


#get the user currently logged in
user = (getpass.getuser())
system("[ ! -d .fallterm ] && mkdir .fallterm")# if .fallterm dir does not exist create it.
system("[ ! -f .fallterm/path.txt ] && touch .fallterm/path.txt")#create path.txt

system("[ ! -f .fallterm/company.txt ] && touch .fallterm/company.txt && echo 'Company Name' > .fallterm/company.txt")#create company.txt
system("[ ! -f .fallterm/header1.txt ] && touch .fallterm/header1.txt && echo 'Header1 Name' > .fallterm/header1.txt")#create company.txt
system("[ ! -f .fallterm/header2.txt ] && touch .fallterm/header2.txt && echo 'Header2 Name' > .fallterm/header2.txt")#create company.txt


os.path.exists('.fallterm')
path= os.path.join('.fallterm', "path.txt")
path =open(path, 'r').read() # read the path name from file
path = path.strip('\n')# remove trailing newline

company= os.path.join('.fallterm', "company.txt")
company =open(company, 'r').read() # read the path name from file
company = company.strip('\n')#remove trailing newline


header1= os.path.join('.fallterm', "header1.txt")
header1 =open(header1, 'r').read() # read the path name from file
header1 = header1.strip('\n')#remove trailing newline

header2= os.path.join('.fallterm', "header2.txt")
header2 =open(header2, 'r').read() # read the path name from file
header2 = header2.strip('\n')#remove trailing newline

copyright ="COPYRIGHT 2075-2077 ROBCO INDUSTRIES"
server = "- Server 4 - "




def get_param(prompt_string): #function for getting user input in curses window
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     curses.echo()
     input = screen.getstr(5, 3, 60)
     return input



def execute_cmd(cmd_string):
     system("clear")
     a = system(cmd_string)
     print( "")
     if a == 0:
          print ("Command Executed successfully")
     else:
          print ("Command terminated with error, please try again\n")
     input("Press enter")
     print ("")






x = 0
selection = -1
option =0
name = user
newpath=""

###########################################################
#Begin first curses window, user selects an option from prompt using arrow keys
while selection != 7:
     graphics = [0]*8
     graphics[option] =curses.A_REVERSE
     screen = curses.initscr()
     #maxy,maxx=screen.getmaxyx()
     #center=center(maxy,maxx,company)
     #screen.resize(maxy,maxx)
     maxy,maxx = screen.getmaxyx()
     resize = curses.is_term_resized(maxy,maxx)
# Action in loop if resize is True:

     screen.nodelay(0)
     screen.clear()
     curses.noecho()
     screen.keypad(1)
     screen.clear()
     screen.border(0)
     screen.addstr(2, 30, company)
     screen.addstr(3, 30, header1)
     screen.addstr(4,30, header2 )
     screen.addstr(6,3,"Welcome ")
     screen.addstr(6,11,user)
     screen.addstr(7,3,"______________________")

     path= os.path.join('.fallterm', "path.txt")
     path =open(path, 'r').read() # read the path name from file
     path = path.strip('\n')# remove trailing newline
     screen.addstr(8,3,"Working dir: /" +path)
     screen.addstr(10, 3, "> Create a new log entry ",graphics[0])
     screen.addstr(11, 3, "> View previous entry logs ",graphics[1])
     screen.addstr(12,3, "> Delete a entry log",graphics[2])
     screen.addstr(13,3, "> Print a log entry", graphics[3])
     screen.addstr(14, 3,"> Configuration Settings",graphics[4])
     screen.addstr(15,3,"> Make a new Directory",graphics[5])
     screen.addstr(16,3,"> View disk space",graphics[6])
     screen.addstr(17, 3,"> Exit ",graphics[7])
     screen.addstr(21,3, "> ")
     #screen.refresh()
     if resize is True:
        maxy,maxx = screen.getmaxyx()
        screen.clear()
        curses.resizeterm(maxy,maxx)
        screen.refresh()

    # x = screen.getch()
     action = screen.getch()
     #screen.clear()


     if action == curses.KEY_UP:
        option = (option -1)%8
        #screen.clear()


     elif action == curses.KEY_DOWN:
        option = (option +1)%8
        #screen.clear()


     elif action ==ord('\n'):
        selection = option
        #screen.clear()



     if selection == 0:
          curses.beep()
          curses.endwin()
          system("clear")
          system("bash -c '%s' " %newfile)
          system("clear")
          screen.clear()
          selection = -1




     elif selection == 1:
         curses.beep()
         screen.addstr(7,4, "Please Choose a log you wish to view")
         print("please choose a log you wish to view")
         curses.endwin()
         #text_files = [f for f in os.listdir(path)]
         #system("python" %text_files)

         system("clear")
         system("bash -c '%s' " %script)
         screen.clear()
         selection = -1



     elif selection == 2:
         curses.beep()
         curses.endwin()
         system("clear")
         system("bash -c '%s' " %rmfile)
         screen.clear()
         selection = -1
     elif selection == 3:
         curses.endwin()
         system("clear")
         system("bash -c '%s' " %printfile)
         screen.clear()
         selection = -1


###########################################################
#If user selects this option it opens a submenu for Configuration

     elif selection == 4:
          curses.endwin()
          option2 =0
          selection2 = -1
          while selection2 != 5:
             screen.clear()
             screen.border()
             graphics2 = [0]*6
             graphics2[option2] =curses.A_REVERSE
             screen.addstr(2, 30, company)
             screen.addstr(3, 30, header1)
             screen.addstr(4,30,  header2)
             screen.addstr(6,3,"Configuration Settings")
             screen.addstr(7,3,"______________________")
             screen.addstr(9, 3, "> Change Company name ",graphics2[0])
             screen.addstr(10,3, "> Change Header1 name",graphics2[1])
             screen.addstr(11,3, "> Change Header2 name",graphics2[2])
             screen.addstr(12,3, "> Change your working directory", graphics2[3])
             screen.addstr(13,3, "> Set your default printer", graphics2[4])
             screen.addstr(14,3, "> Go back",graphics2[5])
             screen.addstr(19,3, "> " )
             #screen.refresh()
             action2 = screen.getch()

             #curses.endwin()
             #screen.clear()

             if action2 == curses.KEY_UP:
                option2 = (option2 -1)%6
             elif action2 == curses.KEY_DOWN:
                 option2 = (option2 +1)%6
             elif action2 ==ord('\n'):
                 selection2 = option2
             if selection2 == 0: #Change company name

                 #system("echo "" > company.txt")
                 #system("vi company.txt")
                 #company= open('company.txt', 'r').read()
                 #company = company.strip('\n')
                 company = get_param("Enter the new name for your company")
                 company = company.decode('UTF-8')

                 curses.endwin()
                 execute_cmd("echo "+ company + "> .fallterm/company.txt")
                 screen.clear()
                 selection2 = -1


             elif selection2 == 1:#change header1 name
                 header1 = get_param("Enter the new name header1")
                 header1= header1.decode('UTF-8')

                 curses.endwin()
                 execute_cmd("echo "+ header1 + "> .fallterm/header1.txt")
                 curses.endwin()
                 screen.clear()
                 selection2 =-1


             elif selection2 == 2:#change header2 name
                header2 = get_param("Enter the new name header2")
                header2= header2.decode('UTF-8')

                curses.endwin()
                execute_cmd("echo "+ header2 + "> .fallterm/header2.txt")
                curses.endwin()
                screen.clear()
                selection2 =-1

             elif selection2 ==3:
                 curses.endwin()
                 system("clear")
                 system("bash -c '%s' " %curdirpath)
                 input("Please press enter to continue")
                 #execute_cmd("echo Your current working directory is /home/$USER/" +path)



                 newpath = get_param("Enter the name of the directory you wish to change your file path to")
                 newpath = newpath.decode('UTF-8')

                 curses.endwin()

                 system("bash -c echo "+ newpath + "> .fallterm/path.txt")

                 while system("cd " +newpath) !=0:
                    curses.endwin()
                    #input("please try again\n\n")
                    system ("echo That directory does not exist, please use the make a new directory program\n")
                    input()
                    newpath = get_param("Enter the name of the directory you wish to change your file path to")
                    newpath = newpath.decode('UTF-8')
                 curses.endwin()
                 system("echo "+ newpath + "> .fallterm/path.txt")
                 system("clear")
                 system("echo You successfully change your working directory to " +newpath)
                 input("Press enter")
                 selection2 = -1

             elif selection2==4:
                 curses.endwin()
                 system("clear")
                 system("bash -c '%s'" %printer)
                 selection2 = -1
          selection = -1
          curses.endwin()




     elif selection ==5:

          directory = get_param("Enter the name of the new Directory you wish to add")
          directory = directory.decode('UTF-8')
          curses.endwin()

          #a = os.mkdir(directory);
          #if a == 0:
           #  print ("Command executed correctly")
          #else:
           #  print ("Command terminated with error")
          #system("bash -c mkdir '%s' " %directory)

          execute_cmd("mkdir "+ directory)



          #system("clear")
          selection = -1

     elif selection ==6:

          curses.endwin()
          execute_cmd("df -h")
          selection = -1

curses.endwin()
