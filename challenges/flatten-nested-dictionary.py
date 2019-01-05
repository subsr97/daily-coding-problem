"""
#173
Stripe

Write a function to flatten a nested dictionary. Namespace the keys with a period.
For example, given the following dictionary:
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""

def flattenDictionaryHelper(nestedDict, flattenedDic, currentKey):
    for key in nestedDict.keys():
        if type(nestedDict[key]) == int:
            flattenedDic[(currentKey+"."+key).strip(".")] = nestedDict[key]
        else:
            flattenedDic = flattenDictionaryHelper(nestedDict[key], flattenedDic, (currentKey+"."+key).strip('.'))
    
    return flattenedDic

def flattenDictionary(nestedDic):
    return flattenDictionaryHelper(nestedDic, dict(), "")

def main():
    nestedDictionary = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }

    flattenedDictionary = flattenDictionary(nestedDictionary)
    print(flattenedDictionary)

if __name__ == "__main__":
    main()