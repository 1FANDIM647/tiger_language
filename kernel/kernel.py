import random
import datetime
import colorama
from colorama import Fore, Back, Style
colorama.init()
print("\t\t\t\t\tDUNIX 1.0")
print("\t\t\tCopyright (c) Blessedsoft corparation ,2000 ©. Belguim\n")
print("\n")


print(datetime.date.today())# time now 


print("****************************************************************************************************\n")
print("\n")
print("\n")
print("\n")



print (Fore.MAGENTA + 
"""
     *    
    ***
   * * *
  * * * *
 * *  *  *
***********

"""
)

print(Fore.RED+    "FILES                | F1 |")
print(Fore.BLUE+   "SERIAL NUMBER DISK   | F2 |")
print(Fore.YELLOW+ "DISK                 | F3 |    ")
print(Fore.GREEN+  "MEMORY NTFS          | F4 | ")
print(Fore.MAGENTA+"Configuration        | F5 |")
print(Fore.GREEN+  "Ip loader on screen        ")

print(Style.RESET_ALL)



   




#to begin with we write main functions 
def measuring_of_serial_number_disk():
    number_of_serial_disk_for_random=random.randint(1,3123)
    serial_disk=3*number_of_serial_disk_for_random
    print("Serial number :",serial_disk)
 
    

# function  binary search

def binary_search(list ,item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)/2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid +1
    return None 
#each file has prioritet 
LIST_FILES_AND_THEIR_NUMBER = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

choose_command=""
while not choose_command:

    choose_command=input("Enter command (section of kernel):")
    if (choose_command == "F1"):
        print("Files:")
        print("Main folder:","HOME_ROOT")
        print("Folder which contains datas of administrator :", "HOME_ROOT|Admin")
        print("Base folder for net-functions", "HOME_ROOT|Admin|net")
        print("Base wi-fi programs in HOME_ROOT|Admin|net|net_utilits|wi-fi utilits_modules_of_hardware")
    elif (choose_command == "F2" ):
        print(" serial number of disk")
        number_simple=1
        measuring_of_serial_number_disk()


        while(number_simple<=12):


            number_simple +=2
            print("HOME_ROOT")
            print("HOME_ROOT|Admin|net")
            print("HOME_ROOT|Admin|net|net_utilits|wi-fi utilits_modules_of_hardware")
            print("HOME_ROOT|Admin|net|net_utilits|wi-fi utilits_modules_of_hardware")
            print("HOME_ROOT|Admin|net|net_utilits|wi-fi utilits_modules_of_hardware")
        def File_core ():
            HOME_ROOT = []
            USERS = [] 
            Admin=  []   
    elif (choose_command == "F3"):
        load_functions_cycle=0
        while(load_functions_cycle<=342):

            load_functions_cycle +=1
            print("load HOME_ROOT|Admin|net|wi-fi utilits_modules_of_hardware")
            print("load HOME_ROOT|Admin|net|net_utilits|")
            print("load HOME_ROOT|Admin|net|wi-fi utilits_modules_of_hardware")
            print("load HOME_ROOT|Admin|users")
            print("load HOME_ROOT|Admin|users1")
            print("load HOME_ROOT|Admin|users1 ")
            print("*******************************")
            print("load HOME_ROOT|Admin|user2|doms")
            print("ALL files loaded in Disk")
            print ("load compiler \'C\'")

    elif (choose_command =="sudo_load_files_raspberry_pi_compiler_gcc20"  ):

        num1=1
        while(num1 <=10):

            num1 +=1
            print("loading compiler")
            print("instalation is successfull")
    elif (choose_command =="F4"):
        print (Fore.MAGENTA+"section MEMORY : it shows how  kernel will split your disk NTFS" )
        NTFS_size_choose = int(input("Size your disk (bites):"))
        print(Style.RESET_ALL)
        size_of_diskService = NTFS_size_choose * 12 /100
        size_of_diskUser = NTFS_size_choose*88/100
        print("Size for service :",size_of_diskService)
        print("Size for User's files:",size_of_diskUser)
    #configuration
    elif (choose_command == "F5"):
        print("_________________________configuration__________________________")
        print("DEVICE DRIVERS :-->")
        print("POWER MANAGMENT:-->")
        #variable for watch  of drivers  names 
        configuration_choose = input("")
        if(configuration_choose == "names_drivers"):
            print("""
               Modul   Name                   Driver type       
               =====   ====                   ===========
               10000   12ker                  Kernel  
               ACPI    Driver by BlessedSoft  Kernel
               Adev    Driver by BlessedSoft  Kernel
               Amd8    Driver by AMD          Kernel
               AmdK    Driver by AMD          Kernel
            """)      
    elif (choose_command == "ip_loader_on_screen"):
       
        print("******GETTING IP*******")
        print("Where you are from")
        country_for_IP = input("I am from :")
        if (country_for_IP ==  'Belguim'):
            Belgium_ip_first_number = 91
            Belgium_ip_second_number = random.randint(12,31)
            Belgium_ip_third_number = random.randint(1,100)
            Belgium_ip_firth_number =random.randint(1,69)
            print("Your IP in Belgium :" , Belgium_ip_first_number , "." ,Belgium_ip_second_number ,".",Belgium_ip_third_number,".",Belgium_ip_firth_number)
        if (country_for_IP == 'France'):
            France_ip_first_number = 176
            France_ip_second_number = random.randint(12,31)
            France_ip_third_number = random.randint(1,100)
            France_ip_firth_number =random.randint(1,69)
            print("Your IP in Belgium :" , France_ip_first_number , "." ,France_ip_second_number ,".",France_ip_third_number,".",France_ip_firth_number)


                           



    #command for skip operation    
    elif (choose_command == "skip"):
        print("section is not choosed") 
     
command1=input("")   
if (command1 == "sudo_load_files_raspberry_pi_compiler_gcc20" ):
    num=1
    while(num <=3):
        num +=1
        print("loading compiler")
        print(Fore.GREEN+ "INSTALATION ")
        print("instalation in HOME_ROOT|USERS|ADMIN")
        print("checking of instalaition in  HOME_ROOT|USERS|ADMIN")
if(command1 == "sudo update"):
    sudo_update = 0
    while( sudo_update <= 5):
        sudo_update +=1
        print("updating HOME_ROOT|USERS|USER|Admin")
    sudo_update1= 0 
    while(sudo_update1 <= 5):
        sudo_update1 +=1
        print("uptdating ")
command2=input("")   
if (command2 == "sudo_load_files_raspberry_pi_compiler_gcc20" ):
    num=1
    while(num <=3):
        num +=1
        print("loading compiler")
        print(Fore.GREEN+ "INSTALATION ")
        print("instalation in HOME_ROOT|USERS|ADMIN")
        print("checking of instalaition in  HOME_ROOT|USERS|ADMIN")
        print(Style.RESET_ALL)
        print("instalation is successfull")   
if (command2 == "sudo create file-prioritet"):
    print("loading  branch HOME_ROOT|USERS")  
    ask_prioritet=int (input("PRIORITET OF THE FILES (0-20) : "))
    ask_file_for_prioritet = input('Name of file:')
    print (" File :",ask_file_for_prioritet,"has prioritet",ask_prioritet )


input("\n\nНажмите enter , чтобы выйти") 

               
                 
