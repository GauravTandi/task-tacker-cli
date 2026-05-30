import sys, json, datetime

if "add" == sys.argv[1]:
        task = sys.argv[2]
        
        with open("tasks.json", "r") as f:
                data = json.load(f)
                now = datetime.datetime.now()
                now = now.strftime("Date %d-%m-%y / %H hr : %M min : %S sec")
                task_properties = [{
                        "id": len(data) + 1,
                        "description":task,
                        "status":"todo",
                        "createdAt":now,
                        "updatedAt":None
                }]
                task_properties = task_properties[0]
                data.append(task_properties)
                # print(data)
                print(task_properties) 

        with open("tasks.json", "w") as f:
                json.dump(data,f, indent=4)
        
        print(f"\nTask added successfully!\nTask:- {task_properties["description"]} --> (ID:{task_properties["id"]}) ")
        

elif "list" == sys.argv[1] and  2 == len(sys.argv):
        with open("tasks.json", "r") as f:
                data = json.load(f)

                print("\nHere list of all task.")
                print("---------------------")
                for task in data:
                        print(f"ID:{task["id"]}) {task["description"]}.")

elif "list" == sys.argv[1] and "done" == sys.argv[2]:
        with open("tasks.json","r") as f:
                data = json.load(f)
                print("\nHere all task that are done")
                print("----------------------------")
                for task in data:
                        if task["status"] == "done":
                                print(f"ID:{task["id"]}- {task["description"]} /-{task["status"]}")

elif "list" == sys.argv[1] and "todo" == sys.argv[2]:
        with open("tasks.json", "r") as f:
                data = json.load(f)
                print("\nHere are the all task todo")
                print("----------------------------")
                for task in data:
                        if task["status"] == "todo":
                                print(f"ID:{task["id"]}- {task["description"]} /-{task["status"]}")

elif "list" == sys.argv[1] and "in-progress" == sys.argv[2]:
        with open("tasks.json","r") as f:
                data = json.load(f)
                print("\nHere the task that in-progress")
                print("---------------------------------")
                for task in data:
                        if task["status"] == "in-progress":
                                print(f"ID:{task["id"]}- {task["description"]} /-{task["status"]}")

elif "update" == sys.argv[1]:
        num = sys.argv[2]; num = int(num)
        update_task = input("Enter update task name: ")
        now = datetime.datetime.now()
        now = now.strftime("Date %d-%m-%y / %Hhr : %Mmin : %S sec")
        with open("tasks.json","r") as f:
                data = json.load(f)
                for task in data:
                        if task["id"] == num:
                                task["description"] = update_task
                                task["updatedAT"] = now
                                print(task)
                                data[num-1] = task # this enter the update in correct index position
        with open("tasks.json","w") as f:
                json.dump(data, f, indent=4)

elif "mark" == (sys.argv[1]):
        status = sys.argv[2]
        num = sys.argv[3] ; num = int(num)
        
        with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                        if task["id"] == num:
                                task["status"] = status
                                data[num - 1] = task
        with open("tasks.json","w") as f:
                json.dump(data, f, indent=4)

elif "delete" == sys.argv[1]:
        num = sys.argv[2]; num = int(num)
        with open("tasks.json", "r") as f:
                data = json.load(f)
                all_task = []
                for task in data:
                        if task["id"] != num:
                                all_task.append(task)
                                
                data = all_task                                       
        with open("tasks.json", "w") as f:
                json.dump(data, f, indent=4)        
                
else:
        print("Try again with - add , list")