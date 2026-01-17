#-----------------------------------
#To do list/task organiser
#started 17/12/25 finished 27/12/25
#-----------------------------------

class Task:
    def __init__(self,title,description):
        #where attributes are initialiezed/created
        self.title = title
        self.description = description
        self.completed = False
        
    #changes self.completed to done    
    def done(self):
        if self.completed == True:
            print("Task already completed")
        else:
            self.completed = True
            print("Task completed")
    #when i print the task object this is what gets displayed
    def __str__(self):
       return f"{self.title} completed = {self.completed} Description:{self.description}"
    #when the task object is being represented anywhere else this is what is shown ie lists,dictionerys
    def __repr__(self):
        return self.title


#creates taskmanger class
class TaskManager:
    def __init__(self):
        #attributes
        self.tasks = []
        
    #adds a task to self.tasks
    def add_task(self,task):
        self.tasks.append(task)
    
    #loops through self.tasks and adds incomplete tasks to a list 
    def get_incomplete_tasks(self):
        incomplete_tasks = []
        for task in self.tasks:
            if not task.completed:
                incomplete_tasks.append(task)            
        return(incomplete_tasks)
    #loops through self.tasks and adds complete tasks to a list
    def get_complete_tasks(self):
        complete_tasks = []
        for task in self.tasks:
            if task.completed:
                complete_task.append(task)
        return(complete_tasks)
    #reprsentation of taskmanger when it gets printed
    def __str__(self):
        return f"{self.tasks} completed = {self.get_complete_tasks()} incomplete = {self.get_incomplete_tasks()}"
    #reprsentation of taskmanger in lists,dictionerys etc..
    def __repr__(self):
        return str(self.tasks)

#storage for lists and tasks that are created
lists_dict = {}
tasks_dict = {}

#storge for tasks objects
tasks_full_object = []

while True:#keeps menu looking for an input
    
    
    choice = input(f"""{"-" * 50}
To create a task enter 1
To create a list enter 2
To add a task to a list enter 3
To mark a task as done enter 4
To see incomplete and complete tasks enter 5
{"-" * 50}
:""")
    
    
    match choice:
        case "1":
            name = input("Enter a name for this task")
            description = input("Describe this task")
            #creates task object name is the key to the object{name:Task}
            tasks_dict[name] = Task(name,description)
            #adds the object to a list             
            tasks_full_object.append(tasks_dict[name])        
            print(f"{name} task has been created")
        
        case "2":
            name = input("Enter the name")
            #creates a taskmanager class
            lists_dict[name] = TaskManager()
            print(f"{name} has been created")
        
        case "3":
            where_to_add = input("What list would u like to add to")
            which_task = input("which task would u like to add")
            #checks if the user has entered a task and list that actually exist
            for task_name,task_object in tasks_dict.items():
                for list_name,list_object in lists_dict.items():
                    if task_name == which_task and list_name == where_to_add:
                        #if valid inputs adds the object
                        list_object.add_task(task_object)
                        print(f"{task_name} has been added to {list_name}")
            
        case "4":
            which_task_complete = input("Which task would u like to mark as complete")
            #makes sure valid input before using method
            for task in tasks_full_object:
                if task.title == which_task_complete:
                    print(tasks)
                    task.done()
                    print(task)

        case "5":
            which_list = input("Which list would u like to see")
            #validates input before displaying list
            for List,list_object in lists_dict.items():
                if List == which_list:
                    print(list_object)
        #cathes an invalid input
        case _:
            print("Invalid option")
            
