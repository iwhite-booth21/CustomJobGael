import os
import sys
import webbrowser


directoryList = [r'C:\Users\booth\OneDrive\Desktop',
                 r'C:\Users\booth\Downloads',
                 r'"C:\Users\booth\OneDrive\Documents"',
                 r'C:\Users\booth\OneDrive\Pictures',
                 r'C:\Users\booth\Music',
                 r'C:\Users\booth\Videos',
                 r'"C:\PythonTestWorks"']


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
    # Explorer utilization of manipulating Browser
    webbrowser.open('http://google.com')
    
    return 0

main()