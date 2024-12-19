class Task:

    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority    
        self.is_done = False

class ToDoList: 

    def __init__(self, tasks):
        self.tasks = tasks

    def mark_task_as_done(self, title):
        task_to_mark = None
        for task in self.tasks:
            if (task.title == title):
                task_to_mark = task
                break
        if (task_to_mark):
            task_to_mark.is_done = True
            print("Task was done")
        else:
            print("Task not found")

    def add_task(self):
        title = input("Title: ")
        description = input("Description: ")
        priority = int(input("Priority: 1 - High, 2- Medium, 3 - Low: "))
        new_task = Task(title, description, priority)
        self.tasks.append(new_task)
        print("New task was Added")

    def delete_task(self, title):
        task_to_remove = None
        for task in self.tasks:
            if (task.title == title):
                task_to_remove = task
                break
        if (task_to_remove):
            self.tasks.remove(task_to_remove)
            print("Task was removed")
        else:
            print("Task not found")

    def view_all_tasks(self, should_sort = False):
        print ("TASKS LIST")
        if should_sort:
            sorted_tasks = sorted(self.tasks, key=lambda task: task.priority)
            for task in sorted_tasks:
                if (task.is_done != True):
                    print("Title: ", task.title)
                    print("Description: ", task.description)
                    print("Priority: ", task.priority)
                    print("Is Done: ", task.is_done)
                else:
                    pass
        else:
            for task in self.tasks:
                if (task.is_done != True):
                    print("Title: ", task.title)
                    print("Description: ", task.description)
                    print("Priority: ", task.priority)
                    print("Is Done: ", task.is_done)
                else:
                    pass

toDoList = ToDoList([])
toDoList.add_task()
toDoList.add_task()
toDoList.add_task()
toDoList.mark_task_as_done("Task 1")
toDoList.view_all_tasks(True)
