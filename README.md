# Task tacker (CLI) Project

## Task tracker is a project used to track and manage your tasks.

It is a simple command line interface(CLI) to track what you need to do, what you have done, and what you are currently working on.

## How to use
        
* Add task - python script.py add taskname   
   
    Note- do not give space in task name    
    No(task name) yes(taskname) or yes(task-name)    
    ie - no(study history) yes(study-history) or use_underscore(study_history)   
    example :-   

```bash
    python task-cli.py add gym

    Task added successfully!
    Task:- gym --> (ID:1) 
```

* Update task - python script.py update 1  
    #ID number you have to put which you want change name of task  
    example :-   
``` bash
    └─$ python task-cli.py update 1
    Enter to update task name: gym & do abs workout      

    ID:1 updated-task-name = gym & do abs workout
```

* Delete task - python script.py delete 1
```bash
        └─$ python task-cli.py delete 1

        gym and abs workout 

        Deleting....
        Deleted successfully!
```
* List all task - python script.py list  
        example:-  
``` bash
    └─$ python task-cli.py list

    Here list of all task.
    ---------------------
    ID:(1) gym & do abs workout. 
    Created:- Date 31-05-26 / 09 hr : 08 min : 36 sec  
    Update:- Date 31-05-26 / 09hr : 19min : 02 sec

    ID:(2) drink-water. Created:-Date 31-05-26 / 09 hr : 22 min : 40 sec
    ID:(3) study. Created:-Date 31-05-26 / 09 hr : 42 min : 53 sec
    ID:(4) learning_new-language. Created:-Date 31-05-26 / 10 hr : 02 min : 20 sec

```
        
* Mark task - python script.py mark done 1  
    example:-  
``` bash
    └─$ python task-cli.py mark done 1

    Task:- gym & do abs workout 
    Status = Done

```

* List done task - python script.py list done
``` bash
    └─$ python task-cli.py list done

    Here all task that are done
    ----------------------------
    ID:1- gym & do abs workout /-done
    ID:2- drink-water /-done

```
* Mark task - python script.py mark todo 1  
    By default status is todo, use when you want to change done or in-progress
   example:-  
``` bash
    └─$ python task-cli.py mark todo 1

    Task:- gym & do abs workout 
    Status = Todo
```
* List todo task - python script.py list todo 
    example:-   
``` bash
    └─$ python task-cli.py list todo  

    Here are the all task todo
    ----------------------------
    ID:1- gym & do abs workout /-todo
    ID:3- study /-todo
```
* Mark task - pyhon script.py mark in-progress 1  
    example:-  
``` bash
    └─$ python task-cli.py mark in-progress 1

    Task:- gym & do abs workout 
    Status = In-Progress

```
* List in progress task - python script.py list in-progress     
       Again # dash is important (in-progress)  
       example:-    
``` bash
    └─$ python task-cli.py list in-progress

    Here the task that are in-progress
    ---------------------------------
    ID:1- gym & do abs workout /-in-progress
    ID:4- learning_new-language /-in-progress

```
### The Project URL
https://roadmap.sh/projects/task-tracker

 


