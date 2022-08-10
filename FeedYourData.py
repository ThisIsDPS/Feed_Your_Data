import datetime
import os

def getDate():
    return datetime.datetime.now()

name = input("Enter your first name: ")

nCount_file_path = f"Ex6_nCount_{name}.txt"
NutritionData_file_path = f"Ex6_nutrition_{name}.txt"

nCount_file_exists = os.path.exists(nCount_file_path)
if nCount_file_exists==False:
    c1 = open(nCount_file_path, "w")
    count1 = c1.write("0")
    c1.close()

fCount_file_path = f"Ex6_fCount_{name}.txt"
FitnessData_file_path = f"Ex6_fitness_{name}.txt"

fCount_file_exists = os.path.exists(fCount_file_path)
if nCount_file_exists==False:
    c2 = open(fCount_file_path, "w")
    count2 = c2.write("0")
    c2.close()

choice = input("Enter N/n for nutrition or F/f for fitness:  ")
if (choice=="N") or (choice=="n"):
    nChoice = int(input("To feed your nutrition data, press 1 or To see your nutrition data, press 2 :"))
    if nChoice==1:
        nData = input("What food you ate now?\n")

        with open(NutritionData_file_path, "a") as f1:
            nDataToFile = f1.write("{ " + str(getDate()) + " }  -> " + nData +"\n")
            print("Feeded Successfully!!!")

        with open(nCount_file_path) as c1:
            nCount = int(c1.read())

        nCount+=1

        with open(nCount_file_path, "w") as c1:
            count1 = c1.write(str(nCount))

    elif nChoice==2:
        print("NUTRITION DATA:")
        with open(NutritionData_file_path) as f2:
            with open(nCount_file_path) as c1:
                nCount = int(c1.read())

            while(nCount):
                print(f2.readline(), end="") 
                nCount-=1

else:
    fChoice = int(input("To feed your fitness data, press 1 or To see your fitness data, press 2 :"))
    if fChoice==1:
        fData = input("Which exercise you did now?\n")

        with open(FitnessData_file_path, "a") as g1:
            fDataToFile = g1.write("{ " + str(getDate()) + " }  -> " + fData +"\n")
            print("Feeded Successfully!!!")

        with open(fCount_file_path) as c2:
            fCount = int(c2.read())

        fCount+=1

        with open(fCount_file_path, "w") as c2:
            count2 = c2.write(str(fCount))

    elif fChoice==2:
        print("FITNESS DATA:")
        with open(FitnessData_file_path) as g2:
            with open(fCount_file_path) as c2:
                fCount = int(c2.read())
                
            while(fCount):
                print(g2.readline(), end="") 
                fCount-=1