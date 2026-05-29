import sys , json

# new_task = []

if "add" == sys.argv[1]:
        task = sys.argv[2]

        # i feel like i don't need this because i already have in filesRW block
        task_properties = [{
                "id": None,
                "description":task,
                "status":"To-DO",
                "createdAt":"CT",
                "updatedAt":"UT"
                        }]

        with open("tasks.json", "r") as f:
                data = json.load(f)
                task_properties = [{
                        "id": len(data) + 1,
                        "description":task,
                        "status":"To-do",
                        "createdAt":"CT",
                        "updatedAt":"UT"
                }]
                task_properties = task_properties[0]
                data.append(task_properties)
                # print(data) 

        with open("tasks.json", "w") as f:
                json.dump(data,f, indent=4)
        
        print(f"Task added successfully! Task: {task_properties["description"]} (ID:{task_properties["id"]}) ")
        
                # with open("tasks.json",'x') as f:
                #     json.dump(list_of_tasks, f)

                # try:
                #     pass
                # except FileExistsError:
                #     with open("tasks.json","a") as f:
                #         data = json.load(f)
                #         # data.append(new_task)
                #         json.dump(data, f)
                #         # print(new_task)
                # # when no error
elif "list" == sys.argv[1]:
        with open("tasks.json", "r") as f:
                data = json.load(f)

                print("\nLisiting all tasks")
                print("-------------------")
                for task in data:
                        print(f"{task["id"]}) {task["description"]}.")
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