
# MongoDB Todo App

## 📌 Project Overview

This is a simple Command Line Todo Application built using Python and MongoDB.

The application allows users to:

- Create Tasks
- View Tasks
- Update Tasks
- Delete Tasks

MongoDB is used as the database and PyMongo is used to connect Python with MongoDB.

---

## 🚀 Features

- Add new tasks
- View all tasks with index numbers
- Update existing tasks
- Delete tasks
- MongoDB database integration
- Simple CLI interface

---

## 🛠️ Technologies Used

- Python
- MongoDB
- PyMongo

---

## 📂 Project Structure

```bash
MongoDB_Project/
│
├── README.md
└── toDO.py
```

---

## ⚙️ Prerequisites

Install the following before running the project:

- Python 3.x
- MongoDB
- pip

---

## 📥 Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/MongoDB_Project.git
```

### 2. Move to Project Folder

```bash
cd MongoDB_Project
```

### 3. Install Required Library

```bash
pip install pymongo
```

---

## ▶️ Run the Project

Start MongoDB server first.

Then run:

```bash
python toDO.py
```

---

## 📜 Source Code

```python
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

    for index, i in enumerate(tasks, start=1):
        print(index, ":", i["task"])


# Update Function
def update_task(index, new_task):

    tasks = list(task_collection.find())

    if index > 0 and index <= len(tasks):

        old_task = tasks[index - 1]

        task_collection.update_one(
            {"_id": old_task["_id"]},
            {"$set": {"task": new_task}}
        )

        print("Task Updated Successfully")

    else:
        print("Invalid Index")


# Delete Function
def delete_task(index):

    tasks = list(task_collection.find())

    if index > 0 and index <= len(tasks):

        task_to_delete = tasks[index - 1]

        task_collection.delete_one(
            {"_id": task_to_delete["_id"]}
        )

        print("Task Deleted Successfully")

    else:
        print("Invalid Index")


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

        read_task()

        index = int(input("Enter Task Index to Update: "))
        new_task = input("Enter New Task: ")

        update_task(index, new_task)

    elif choice == '4':

        read_task()

        index = int(input("Enter Task Index to Delete: "))

        delete_task(index)

    elif choice == '5':

        break

    else:
        print("Provide a Valid Choice")
```

---

# 🔍 Step-by-Step Explanation

## 1️⃣ Import MongoClient

```python
from pymongo import MongoClient
```

Used to connect Python with MongoDB.

---

## 2️⃣ Connect MongoDB

```python
url = "mongodb://localhost:27017"
client = MongoClient(url)
```

Connects Python to local MongoDB server.

---

## 3️⃣ Create Database

```python
db = client.todo_db
```

Creates or connects to database named `todo_db`.

---

## 4️⃣ Create Collection

```python
task_collection = db.task
```

Creates or connects to collection named `task`.

---

## 5️⃣ Create Task Function

```python
def create_task(description):
```

Used to insert new task into MongoDB.

---

## 6️⃣ Read Task Function

```python
def read_task():
```

Displays all stored tasks with indexes.

---

## 7️⃣ Update Task Function

```python
def update_task(index, new_task):
```

Updates selected task using index number.

---

## 8️⃣ Delete Task Function

```python
def delete_task(index):
```

Deletes selected task from database.

---

## 9️⃣ Main Loop

```python
while True:
```

Keeps the application running continuously until user exits.

---

## 📋 Menu Options

```text
1. Create Task
2. View Task
3. Update Task
4. Delete Task
5. Exit
```

---

## 📸 Example Output

```text
1. Create Task
2. View Task
3. Update Task
4. Delete Task
5. Exit

Enter Your Choice: 1
Enter your Task: Learn MongoDB

Task Added Successfully
```

---

## 🚀 Future Improvements

- Add task completion status
- Add due dates
- Build GUI version
- Convert to Flask web app
- Add authentication system

---

## 👨‍💻 Author

Rajibul Molla

---

## 📄 License

This project is open-source and free to use.
