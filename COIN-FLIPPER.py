import random
import time

print("  ____ ___ ___ _   _       _____ _     ___ ____  ____  _____ ____  ")
print(" / ___/ _ \_ _| \ | |     |  ___| |   |_ _|  _ \|  _ \| ____|  _ \")
print("| |  | | | | ||  \| |_____| |_  | |    | || |_) | |_) |  _| | |_) |")
print("| |__| |_| | || |\  |_____|  _| | |___ | ||  __/|  __/| |___|  _ < ")
print(" \____\___/___|_| \_|     |_|   |_____|___|_|   |_|   |_____|_| \_\")
print("                   Made by Roger Bajona") 
          


number_of_flip_coins = 10000000 #insert how many coins you wanna flip

face = 0 
cross = 0

total_throws = 0

percent_face = face / total_throws * 100 
percent_cross = cross / total_throws * 100 
      
      

while number_of_flip_coins != total_throws:
    if random.randint(1, 2) == 1:
        face += 1
        total_throws += 1 
    else:
        cross += 1 
        total_throws += 1 

print("Faces: " + face)
print("Crosses: "cross)
print("Total throws" + total_throws)
print("Percent of cross" + percent_cross)
print("Percent of faces" + percent_face)


save_question = input("Do you want to export the data?")
print("If you want to save, write #yes# otherwise write #no#")

if save_question == "yes":
    print("saving")
    file_name = input("How do you want do name your file")
    f = (file_name, "x")
    f1 = (file_name, "w") 
    f1.write("Number of faces: " face)
    f1.write("Number of crosses: " cross)
    f1.write("Total flipps :" total_throws)
    f1.write("Percent of faces: " percent_face) 
    f1.write("Percent of crosses" percent_cross) 
    f1.close
    f.close
elif save_question == "no":
    print("Data won't be saved")
else:
    print("Retry")
    
    
