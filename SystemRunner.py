import os
import sys


directoryList = [r'C:\Users\IWB\Desktop\SonicKart',
                 r'C:\Users\IWB\Desktop\Spring 2022\Computer Forensics',
                 r'C:\Users\IWB\Documents',
                 r'C:\Users\IWB\Pictures',
                 r'C:\Users\IWB\Downloads',
                 r'C:\Users\IWB\Desktop\Spring 2022\Cryptography',
                 r'C:\Users\IWB\Desktop\Spring 2022\Computer Forensics\Wayne Image (4)']


def locationChecker(arg):
    answer = ''
    if arg == "1":
        answer = directoryList[0]
        os.chdir(directoryList[0])
        
        return answer
    elif arg == "2":
        answer = directoryList[1]
        os.chdir(directoryList[1])
      
        return answer
    elif arg == "3":
        answer = directoryList[2]
        os.chdir(directoryList[2])
        
        return answer    
    elif arg == "4":
        answer = directoryList[3]
        os.chdir(directoryList[3])
       
        return answer
    elif arg == "5":
        answer = directoryList[4]
        os.chdir(directoryList[4])
        
        return answer
    elif arg == "6":
        answer = directoryList[5]
        os.chdir(directoryList[5])
   
        return answer
    elif arg == "7":
        answer = directoryList[6]
        os.chdir(directoryList[6])
   
        return answer


def main():
    arg = sys.argv[1] 
    # choice = str(input(r'Give me your destination Knight Gael: '))
  
    instantTransmission = locationChecker(arg)
    print(instantTransmission)
    print("You have arrived esteemed warrior Gael")
    os.system('dir')
    print("Here are some fun things in your area::: ")
    os.system('hostname')
    os.system('ver')
    os.system('ipconfig')
    os.system('systeminfo')
    os.system('tree')
    return 0

main()