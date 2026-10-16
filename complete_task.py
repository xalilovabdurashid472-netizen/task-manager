import csv

def complete_task(task_id):
    with open("tasks.csv", "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        
    for task in reader:
        if task["id"] == task_id:
            task["status"] = "bajarilgan"
           
            with open("tasks.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=reader[0].keys())
                writer.writeheader()
                writer.writerows(reader)
            return True
            
    return False

if __name__ == "__main__":
    tid = input("Vazifa ID sini kiriting: ")
    print("Vazifa bajarildi!" if complete_task(tid) else "Vazifa topilmadi!")