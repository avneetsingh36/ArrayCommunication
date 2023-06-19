import datetime, math, time
from datetime import datetime

#VAR DECLARATION

counter = 0
logCounter = 10

timeStorageForReversion = [] #helps with reversing the milisecond function

#LIST 1 CONTAINS INFORMATION THAT WILL BE USED IN THE SUCCESSION --> I USED NUMBERS FROM THE FIB SEQUENCE FOR FUN

informationList = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181] 

print(f'\nHere is the contents of Array 1: \n{informationList}\n')

#LIST 2 CONTAINS THE OPERATIONS THAT WILL BE DONE TO THE VALUE OF LIST 1

operationList = []

for i in range(len(informationList)):
    counter += 1
    now = datetime.now()
    operationList.append(int(informationList[i]) - int(math.pow(counter,2)) + int(now.strftime("%f")))
    timeStorageForReversion.append(now.strftime("%f"))

print(f'\nArray 2 manipulates the contents from array by subtracting an incrementing counter and then adding the current miliseconds and here is the output:')
print(operationList)

#LIST 3 PERFORMS OPERATIONS THAT UNITE THE CONTENTS OF LISTS 1 AND 2 AND THEN MANIPUTLATE IT EVEN FURTHER

finalManipulationList = []

for i in range(len(informationList)):
    logCounter = int(str(logCounter) + '0')
    finalManipulationList.append((int(operationList[i]) - int(informationList[i])) * int(math.log(logCounter)))

print(f'\nArray 3 manipulates the contents from 1 and 2 by unionizing them and then adding a logCounter to it and here is the output:')
print(finalManipulationList)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
time.sleep(2)

#NEXT WE WILL REVERT THE TERMS OF LIST 3 BACK INTO ITS ORIGIONAL ELEMENTS

print('\n\nNow we will revert the list!\n\n')

reversionList = []

logCounter = 10
counter = 0 

for i in range(len(informationList)):
    counter += 1
    logCounter = int(str(logCounter) + '0')
    reversionList.append(int((finalManipulationList[i]) / int(math.log(logCounter)) + int(informationList[i]) - int(timeStorageForReversion[i]) + int(math.pow(counter,2))))

time.sleep(2)
print(f'\nReverted Array uncoverts everything in Array 3 back to 1 by using the contents of ARRAY 1 2 and 3 ---> here it is:')
print(reversionList) 
print("\nHere is the time Storage for Reversion:")
print(timeStorageForReversion)
print("\n")

