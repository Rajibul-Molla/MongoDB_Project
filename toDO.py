from pymongo import MongoClient

url = "mongodb://localhost:27017"
client = MongoClient(url)

db = client.todo_db

task_collection = db.task


# Insert Function
def create_task(description):
    task = {
        "task": description
    }

    task_collection.insert_one(task)
    print("Task Added Successfully")


# Read Function
def read_task():
    tasks = task_collection.find()

    print("\nTasks List:")

    for i in tasks:
        print(i["task"])


# Update Function
def update_task(old_task, new_task):

    result = task_collection.update_one(
        {"task": old_task},
        {"$set": {"task": new_task}}
    )

    if result.modified_count > 0:
        print("Task Updated Successfully")
    else:
        print("Task Not Found")


# Delete Function
def delete_task(task_name):

    result = task_collection.delete_one(
        {"task": task_name}
    )

    if result.deleted_count > 0:
        print("Task Deleted Successfully")
    else:
        print("Task Not Found")


while True:

    print("\n1. Create Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        description = input("Enter your Task: ")
        create_task(description)

    elif choice == '2':
        read_task()

    elif choice == '3':

        old_task = input("Enter Old Task: ")
        new_task = input("Enter New Task: ")

        update_task(old_task, new_task)

    elif choice == '4':

        task_name = input("Enter Task Name to Delete: ")

        delete_task(task_name)

    elif choice == '5':
        break

    else:
        print("Provide a Valid Choice")