import csv
def show_tasks():

    with open("tasks.csv","r",)as file:
        mahsulotlar=csv.DictReader(file)
        for mahsulot in mahsulotlar:

            print(mahsulot)
show_tasks()