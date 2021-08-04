tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def get_list_of_uncompleted_tasks(list):
    uncompleted_tasks_list = []
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks_list.append(task)
    return uncompleted_tasks_list
# print(get_list_of_uncompleted_tasks(tasks))


def get_list_of_completed_tasks(list):
    completed_task_list = []
    for task in list:
        if task["completed"] == True:
            completed_task_list.append(task)
    return completed_task_list
# print(get_list_of_completed_tasks(tasks))

def get_list_of_all_task_descriptions(list):
    descriptions = []
    for task in list:
        descriptions.append(task["description"])
    return descriptions
# print(get_list_of_all_task_descriptions(tasks))

def get_list_of_time_taken(list, time):
    tasks = []
    for task in list:
        






