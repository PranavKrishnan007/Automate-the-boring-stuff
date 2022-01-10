import os
for folderName, subFolders, fileNames in os.walk('/Users/pranavkrishnan/desktop/math'):
    print(folderName,'foldername')
    for subFolder in subFolders:
        print(subFolder),"sub-foldername"
    for fileName in fileNames:
        print(fileName,"filename")
    print('')