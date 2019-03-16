"""
#222
Quora

Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

"""


def standardize(path):
    dirs = path.split("/")

    standardDirs = []

    for directory in dirs:
        if directory == "..":
            if len(standardDirs) > 1:
                standardDirs.pop()
        elif directory != ".":
            standardDirs.append(directory)

    return "/".join(standardDirs)


def main():
    print(standardize("/usr/bin/../bin/./scripts/../"))
    print(standardize("/usr/bin/../bin/./scripts/../../../../"))
    print(standardize("/home/local/domain/./username/foo/.././asd\\ asd\\ \\<.txt/"))


if __name__ == "__main__":
    main()
