# [Files](https://automatetheboringstuff.com/chapter8/)

* Use `import os` and `os.path.join('folder1', 'folder2', 'img.png')` to join path and files name together. This works for any OS

* `os.getcwd()` method will get the current working dir

* `os.chdir()` to change working dir

* Absolute vs Relative File Path - Absolute begin with root folder while relative do not

* `.` means this dir and `..` means parent dir

* Calling `os.path.abspath(path)` will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.

* Calling `os.path.isabs(path)` will return True if the argument is an absolute path and False if it is a relative path.

* Calling `os.path.relpath(path, start)` will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path.

* Calling `os.path.dirname(path)` will return a string of everything that comes before the last slash in the path argument.

* Calling `os.path.basename(path)` will return a string of everything that comes after the last slash in the path argument.

* Calling `os.makedirs(path)` will make a dir


## Textfiles

* Plain Text Files (.txt files) vs. Binary Files (every other files, word processing, spreadsheet, exe files)


## Shelve files

* Writing and read files can only store one long string

* If you want to store variable that contain **list**, **dict**, and **other complex data structures**, you can save variable in python to Binary Shelve Files
  using Shelves modules

* You can save and make changes to Shelve files as if it was a dictionary

* They're similar to dict as they have `keys()` and `values()` methods


## Copying and Moving Files

* `shutil` module have func that let you copy, move, rename, delete etc files in your python program

* `shutil.copy(filename1, filename2)` will copy one file from one location to another location, or just copy the file and save as a different name.

* `shutil.copytree(directory1, directory2)` will copy an entire folder dir to another location (also can rename)

* `shutil.move(filename1, filename2)` will move one file from one directory to another directory.

* If you want to rename a file, just use the `shutil.move()` to move the file to the same location but with different name.


## Deleting files

* There are three way to delete a files

  1. `import os` -> `os.unlink('filename')` will perm delete file.
  2. `os.rmdir('folder')` will delete the folder that is passed in as argument (however, the folder must be empty).
  3. `import shutil` -> `shutil.rmtree('folder')` will delete the folder and all of its content. This have no safeguard so you want to be careful.

* TO prevent you from deleting the wrong files, you should do a dry run of codes that have delete function.
* Dry runs are basically just you commenting out the delete function and printing out the changes you're about to make.

* Optionally, you can also use the `send2trash` module (not preinstalled) and just send everything you want to delete to trash instead.

## Walking through directory

* Use the os module `os.walk('directory')` to walk through the folder tree and do something with the files inside. (see example code)

* `os.walk()` return's value is used in a for-loop like `for folderNames, subFolders, filesNames in os.walk('directory'):`
  1. First return value is current folder name.
  2. Second return value is all sub folder names inside current folder.
  3. All the files inside the subfolders.
