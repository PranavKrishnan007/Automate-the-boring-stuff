# NOTES Chapter 10

### 1. copying file from one place to another using shutil module 👌🏽
```
>>> import shutil, os
>>> from pathlib import Path
>>> p = Path.home()
>>> shutil.copy(p/'spam.txt', p/'some_folder')
PosixPath('/Users/pranavkrishnan/some_folder')
```
shutil.copy will only be able to copy 1 file but shutil.copytree can copy and entire folder (every folder and file inside it) !
```
Usage : shutil.copytree(source, destination)
```
shutil.copytree will create a new folder at the destination with all the things copied inside the source folder
<hr>

### 2. Moving and renaming files
using shutil module we can easily move files from the source to the destination. [IMP THING TO REMEMBER IF THERE IS ALREADY A FILE BY THE SAME NAME OF THAT OF THE SOURCE FILE .... THE DESTINATION FILE WILL BE OVERWRITTEN]
```
usage : shutil.move(source, destination)
```
since it's easy to overwrite stuff be careful to not make this error.
```
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
```
what this does is that it moves the file as well as renames the file while doing so
- if shutil.move doesn't find a folder at the end then it would rename the source file to the name of the file ie essentially removing the extension name. this could cause an error in the code.
- the file you're sending to /User/User_name/file_does_not_exist/somefile/destination then python will throw and exception.
<hr>

### 3. Deleting files and folders permanently
```
• Calling os.unlink(path) will delete the file at path.
• Calling os.rmdir(path) will delete the folder at path. This folder must beempty of any files or folders.
• Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.
```
since these permanently delete the file/folders so its a good idea to first check the path by printing using print(path) before using it in one of these.
<hr>

### 4. Safe deletes with send2trash module
```
>>> import send2trash
>>> baconFile = open('bacon.txt', 'a') # creates the file >>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> send2trash.send2trash('bacon.txt')
```
this is the use case ... I couldn't get it to work but will try later.

### 5. Walking a Directory Tree
``` 
this can be done using os.walk() and by passing the parameter of the path of the folder that needs to be walked.

os.walk() will return 3 values on each iteration...
• A string of the current folder’s name
• A list of strings of the folders in the current folder
• A list of strings of the files in the current folder
```

### Compressing files with zipfile module
1. Reading ZIP files
```
>>> import zipfile, os
>>> from pathlib import Path
>>> p = Path.home()
>>> exampleZip = zipfile.ZipFile(p / 'example.zip')
>>> exampleZip.namelist()
['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg'] >>> spamInfo = exampleZip.getinfo('spam.txt')
>>> spamInfo.file_size
13908
>>> spamInfo.compress_size
3828
>>> f'Compressed file is {round(spamInfo.file_size / spamInfo .compress_size, 2)}x smaller!'
)
'Compressed file is 3.63x smaller!'
>>> exampleZip.close()
```
2. Extracting from ZIP files
```
>>> import zipfile, os
>>> from pathlib import Path
>>> p = Path.home()
>>> exampleZip = zipfile.ZipFile(p / 'example.zip')
>>> exampleZip.extractall() >>> exampleZip.close()
```
can pass directory name to extractall()

3. Creating and adding to ZIP files
```
>>> import zipfile
>>> newZip = zipfile.ZipFile('new.zip', 'w')
>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED) >>> newZip.close()
```
<hr>
