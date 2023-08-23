import defaults.const as const
import os

sourceDictionary = {}
destinationDictionary = {}
def checkFileContent(dir, dict):
    sourceItems = os.listdir(dir)
    for item in sourceItems:
        item_path = os.path.join(dir, item)  # Get the full path of the item

        # Check if the item is a directory
        if os.path.isdir(item_path):
            checkFileContent(item_path, dict)
        else:
            dict[item_path] = os.path.getmtime(item_path)


sourceFile =  checkFileContent(dir = const.SOURCE_PATH, dict = sourceDictionary)
destinationFile =  checkFileContent(dir = const.DESTINATION_PATH, dict = destinationDictionary)





def reduceDict(dict, name): 
    rd = {}
    for item in dict.items():
        path = item[0]
        modifiedTime = item[1]
        pathAfterSource = (path.split(f'{name}'))[1]
        rd[pathAfterSource] = modifiedTime
    return rd


reducedSourceDict =  reduceDict(dict= sourceDictionary, name = 'Source')
reducedDestDict = reduceDict(dict= destinationDictionary, name = 'Destination')


#TODO wap to check if pathAfterSource with same modifiedTime is persent on Destination or not. If not send the file or replace it in the Destination