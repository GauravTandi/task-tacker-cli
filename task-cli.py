import sys , json

# new_task = []

if "add" == sys.argv[1]:
    task = sys.argv[2]

        # i feel like i don't need this because i already have in filesRW block
    task_properties = [{
            "id": None,
            "description":task,
            "status":(),
            "createdAt":"CT",
            "updatedAt":"UT"
            }]

    with open("tasks.json", "r") as f:
            data = json.load(f)
            task_properties = [{
                    "id": len(data) + 1,
                    "description":task,
                    "status":(),
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
