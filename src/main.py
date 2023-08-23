import defaults.const as const
import os
import datetime
import json


def checkFileContent(sourceDir):
    sourceItems = os.listdir(sourceDir)
    for item in sourceItems:
        item_path = os.path.join(sourceDir, item)  # Get the full path of the item

        # Check if the item is a directory

        if os.path.isdir(item_path):
            checkFileContent(item_path)

        else:
            print(f"{item_path}  :  {os.path.getmtime(item_path)}")



checkFileContent(sourceDir = const.SOURCE_PATH)