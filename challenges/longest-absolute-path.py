"""
#17
Google

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.

"""

def currentPathLength(pathStack):
    return sum([len(x) for x in pathStack])

def longestAbsolutePath(fileSystemString):
    entities = fileSystemString.split("\n")
    
    if len(entities) == 0:
        print("")
        return

    pathStack = []

    rootFolder = entities.pop(0)
    pathStack.append(rootFolder)

    longestPath = rootFolder
    longestPathLength = len(rootFolder)

    currentDepth = 0

    for entity in entities:
        currentEntityDepth = entity.count("\t")
        entity = entity.strip("\t")
        if "." in entity:
            # Entity is a file
            if currentEntityDepth != currentDepth + 1:
                differenceInDepth = abs(currentDepth - currentEntityDepth)
                for _ in range(differenceInDepth):
                    pathStack.pop()
                    currentDepth -= 1
            
            # Uncomment to print every absolute path
            # print("\\"+"\\".join(pathStack)+"\\"+entity)
            
            if currentPathLength(pathStack) + len(entity) > longestPathLength:
                longestPath = "\\".join(pathStack) + "\\" + entity
                longestPathLength = len(longestPath)
            
        else:
            # Entity is a dir
            if currentEntityDepth != currentDepth + 1:
                differenceInDepth = abs(currentDepth - currentEntityDepth)
                for _ in range(differenceInDepth+1):
                    pathStack.pop()
                    currentDepth -= 1
            
            pathStack.append(entity)
            currentDepth += 1


    return "\\" + longestPath.replace("\t","")

def main():
    print(longestAbsolutePath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
    print(longestAbsolutePath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
    print(longestAbsolutePath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tparent\n\t\tsubdir2\n\t\t\tsubsubdir2\n\t\t\t\tfile2.ext\n\t\tchild.as"))
    
    """
    dir
    subdir1
        file1.ext
        subsubdir1
    parent
        subdir2
            subsubdir2
                file2.ext
        child.txt
    """

if __name__ == "__main__":
    main()
