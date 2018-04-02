#! python3

def readFiles():
    '''
    file.read() method will return a single string of the content
    '''
    helloFile = open('hello.txt') # Read Mode
    content = helloFile.read()    # Reading content
    print(content)
    helloFile.close()             # Close the file

# readFiles()

def readLines():
    '''
    file.readlines() will return a list of string at new line '\n'
    '''
    helloFile = open('hello.txt')      # Read Mode
    content = helloFile.readlines()    # Reading content
    print(content)
    helloFile.close()                  # Close the file

# readLines()

def writeToFile():
    '''
    To Write to files, you need to use write mode, or append mode, if file does not exist, python will create it for you
    Write mode will overwite existing files and start from scratch and erase whatever you already got in that file. `open('filename', 'w')`
    Append mode will simply append(add) to the existing files and will not erase what you currently have            `open('filename', 'a')`
    '''
    helloFile = open('hello2.txt', 'w') #write mode
    helloFile.write('This is Ensign!\n')
    helloFile.close()

    helloFile1 = open('hello2.txt', 'a') #append mode
    for i in range(10):
        helloFile1.write('Im appending this line!\n')
    helloFile1.close()

# writeToFile()

def shelveFiles():
    '''
    Using Shelve files to store a list of names as binary files
    '''
    import shelve
    shelveFile = shelve.open('mydata') #opening data file and return shelve file object
    shelveFile['girls'] = ['Sophie', 'Mina', 'Julie', 'Sojin', 'Seolhyun'] #storing names
    shelveFile.close()

    shelveFile = shelve.open('mydata') # re-opening data files
    print(shelveFile['girls'])         # grab value from variable and print them

# shelveFiles()


def walkingDir():
    '''
    Walking through directory
    '''
    import os
    for folderName, subFolders, filenames in os.walk('..\..\AutomatingBoringPython'):
        print('The Folder is: '+ folderName)
        print('The Subfolder in %s are: %s' % (folderName, subFolders))
        print('The files in %s are: %s \n' % (folderName, filenames))

walkingDir()
