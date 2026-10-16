import csv 
def add_task():
    name=input("Yangi vazifa nomini kiriting: ")
    with open("tasks.csv", "a", newline="", encoding="utf-8") as file:
        yozish=csv.writer(file)
        yozish.writerow([3,name,"bajarilmagan"])
add_task()