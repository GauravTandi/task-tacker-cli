import sys, json

if "add" == sys.argv[1]:
        task = sys.argv[2]
        
        with open("tasks.json", "r") as f:
                data = json.load(f)
                task_properties = [{
                        "id": len(data) + 1,
                        "description":task,
                        "status":"todo",
                        "createdAt":"CT",
                        "updatedAt":"UT"
                }]
                task_properties = task_properties[0]
                data.append(task_properties)
                # print(data) 

        with open("tasks.json", "w") as f:
                json.dump(data,f, indent=4)
        
        print(f"\nTask added successfully!\nTask:- {task_properties["description"]} --> (ID:{task_properties["id"]}) ")
        

elif "list" == sys.argv[1] and  2 == len(sys.argv):
        with open("tasks.json", "r") as f:
                data = json.load(f)

                print("\nLisiting all tasks")
                print("-------------------")
                for task in data:
                        print(f"ID:{task["id"]}) {task["description"]}.")

elif "list" == sys.argv[1] and "done" == sys.argv[2]:
        with open("tasks.json","r") as f:
                data = json.load(f)
                print("\nHere all task that are done")
                print("----------------------------")
                for task in data:
                        if task["status"] == "done":
                                print(f"ID:{task["id"]}- {task["description"]} /- {task["status"]}")

elif "list" == sys.argv[1] and "todo" == sys.argv[2]:
        with open("tasks.json", "r") as f:
                data = json.load(f)
                print("\nHere are the all task todo")
                print("----------------------------")
                for task in data:
                        if task["status"] == "todo":
                                print(f"ID:{task["id"]}- {task["description"]} /- {task["status"]}")

elif "update" == sys.argv[1]:
        num = sys.argv[2]; num = int(num)
        update_task = input("Enter update task name: ")

        with open("tasks.json","r") as f:
                data = json.load(f)
                for task in data:
                        if task["id"] == num:
                                task["description"] = update_task
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
                print(f"{data[0]}")
else:
        print("Try again with - add , list")