# import json
#
## /home/ubuntu/.m2/repository/org/json/json/20160212/json-20160212.jar
# with open('cucumber.json', 'r') as json_file:
#     data = json.load(json_file)
#
# # Process the parsed data
# i = 0
#
#
# # item is one object here
# for item in data:
#     # Access JSON elements
#     #print(item)
#     i += 1
#
# print(i)




# import os
# import json
# import glob
# import shutil
# import random
# from datetime import datetime
#
# def summarizeJsonFiles(dirPath):
#     counter = 0
#     allFeaturesSummaryJson = []
#     summaryArrJson = []
#
#     numberOfFeatures = 0
#     totalNumberScenarioInFeatures = 0
#     totalFailedScenariosInFeature = 0
#     totalFailedScenariosInFeatures = 0
#     totalScenarios = 0
#     featureName = ""
#     folderParentName = ""
#     teamName = ""
#     isFailedBeforeScenarios = False
#
#     files = glob.glob(os.path.join(dirPath, "*.json"))
#
#     # Verify duplicate file
#     for i in range(len(files)):
#         for j in range(i + 1, len(files)):
#             if files[i] == files[j]:
#                 os.remove(files[j])
#
#     files = glob.glob(os.path.join(dirPath, "*.json"))
#
#     #for filePath in files: ##########################
#     filePath = 'cucumber.json'
#     print("filesLeng:", len(files))
#     if os.path.isdir(filePath):
#         print("filePath:", filePath)
#         print("fileCucumberLeng:", len(os.listdir(filePath)))
#         filePath = os.listdir(filePath)[0]
#
#     folderParentName = os.path.split(filePath)[0].split("allreports")[1].replace("\\", "")
#     numberOfFeatures += 1
#
#     try:
#         with open(filePath, "r") as file:
#             text = file.read()
#
#         j = text.index("{")
#         text = text[j:]
#         jsonData = json.loads(text)
#
#         uri = jsonData["uri"]
#         if "No feature found or dsl runner issue" in uri:
#             featureName = folderParentName
#             if "/" in featureName:
#                 featureName = featureName.split("/")[1]
#             teamName = jsonData["teamname"]
#             teamName = teamName.split("/features/")[2].split("/")[0]
#         else:
#             teamName = uri.split("/features/")[2].split("/")[0]
#             featureName = uri.split("/")[-1]
#
#         featureSummaryJson = {}
#         featureSummaryJson["FeatureName"] = featureName
#         featureSummaryJson["TeamName"] = teamName
#
#         arrElements = jsonData["elements"]
#         isStepsPassed = True
#         printMyfirstError = False
#         arrSteps = []
#         scenariosStr = ""
#         isAtLeastOnScenarioFailed = False
#
#         for element in arrElements:
#             arrSteps = []
#             printMyfirstError = False
#             isFailedBeforeScenarios = False
#             errorMsg = ""
#             scenario = element["name"]
#             elementType = element["type"]
#
#             if scenario and elementType == "scenario":
#                 totalScenarios += 1
#
#             if "before" in element and not printMyfirstError:
#                 beforeArr = element["before"]
#                 if any(step["result"]["status"] == "failed" for step in beforeArr):
#                     errorMsg = beforeArr[0]["result"]["error_message"]
#                     featureSummaryJson["Status"] = "failed"
#                     featureSummaryJson["Error"] = errorMsg
#                     printMyfirstError = True
#                     isStepsPassed = False
#                     isFailedBeforeScenarios = True
#                     isAtLeastOnScenarioFailed = True
#                     totalFailedScenariosInFeature += 1
#
#             if not printMyfirstError:
#                 for step in element.get("steps", []):
#                     statusRowData = step["result"]
#                     if statusRowData["status"] == "failed" or statusRowData["status"] == "skipped":
#                         if "before" in step:
#                             beforeArr = step["before"]
#                             if any(step["result"]["status"] == "



import os
import json
from datetime import datetime

def summarizeJsonFiles(dirPath):
    counter = 0
    allFeaturesSummaryJson = []
    summaryArrJson = []

    numberOfFeatures = 0
    totalNumberScenarioInFeatures = 0
    totalFailedScenariosInFeature = 0
    totalFailedScenariosInFeatures = 0
    totalScenarios = 0

    files = os.listdir(dirPath)
    files = [os.path.join(dirPath, file) for file in files if file.endswith(".json")] # this is empty now
    files = ["place_holder"] # todo - delete

    for filePath in files:
        filePath = 'cucumber.json' ## change
        print("folder parent name: "+ os.path.split(os.path.dirname(filePath))[1])
        #folderParentName = os.path.split(os.path.dirname(filePath))[1]
        numberOfFeatures += 1

        try:
            with open(filePath, "r") as file:
                jsonData = json.load(file)
                print("jsonData")

                #uri = jsonData["uri"]
                uri = "file:src/test/resources/features/Dispatch_Console/SchedulingInspector.feature"
                print(uri)
                if "No feature found or dsl runner issue" in uri:
                    featureName = folderParentName.split("/")[-1] # todo - ?
                    print("feature name: "+featureName)
                    teamName = jsonData["teamname"].split("/features/")[2]
                    print("team name: " + teamName)
                else:
                    #teamName = uri.split("/features/")[2] # out of range
                    teamName = "Dispatch_Console" # out of range
                    print("team name: "+teamName)
                    #featureName = uri.split("/")[-1]
                    featureName = "SchedulingInspector"

                featureSummaryJson = {
                    "FeatureName": featureName,
                    "TeamName": teamName
                }

                elements = jsonData["elements"]
                print("step 2")
                isStepsPassed = True
                scenariosStr = ""
                arrSteps = []

                for element in elements:
                    elementType = element["type"]
                    scenario = element["name"]
                    steps = element.get("steps", [])

                    if elementType == "scenario":
                        totalScenarios += 1

                    for step in steps:
                        stepData = {
                            "Keyword": step["keyword"],
                            "Name": step["name"],
                            "Status": step["result"]["status"],
                            "Error": step["result"].get("error_message", "")
                        }
                        arrSteps.append(stepData)

                        if stepData["Status"] == "failed":
                            isStepsPassed = False

                if not isStepsPassed:
                    totalFailedScenariosInFeature += 1

                if not isStepsPassed and arrSteps:
                    featureSummaryJson["Status"] = "failed"
                else:
                    featureSummaryJson["Status"] = "passed"

                featureSummaryJson["Scenarios"] = scenariosStr
                featureSummaryJson["Steps"] = arrSteps

                summaryArrJson.append(featureSummaryJson)

            #break ## just for example

        except Exception as e:
            print("Error:", e)


    allFeaturesSummaryJson.append({
        "NumberOfFeatures": numberOfFeatures,
        "TotalNumberScenarioInFeatures": totalNumberScenarioInFeatures,
        "TotalFailedScenariosInFeature": totalFailedScenariosInFeature,
        "TotalFailedScenariosInFeatures": totalFailedScenariosInFeatures,
        "TotalScenarios": totalScenarios,
        "SummaryArr": summaryArrJson
    })

    currentDateTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    summaryJsonFilePath = os.path.join(dirPath, "summary_" + currentDateTime + ".json")

#     with open(summaryJsonFilePath, "w") as summaryFile:
#         json.dump(allFeaturesSummaryJson, summaryFile, indent=4)
    print(allFeaturesSummaryJson)

    print("Summary file generated:", summaryJsonFilePath)

    return summaryJsonFilePath

# Example usage
directoryPath = "/"
summaryFilePath = summarizeJsonFiles(directoryPath)
