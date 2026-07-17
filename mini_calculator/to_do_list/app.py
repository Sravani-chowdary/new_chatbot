import streamlit as st
import os

# -----------------------------------------
# Page Configuration
# -----------------------------------------

st.set_page_config(
    page_title="To-Do List",
    page_icon="✅",
    layout="centered"
)

st.title("✅ My To-Do List")

FILE_NAME = "tasks.txt"

# -----------------------------------------
# Load Tasks
# -----------------------------------------

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        tasks = file.read().splitlines()

    return tasks

# -----------------------------------------
# Save Tasks
# -----------------------------------------

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

# -----------------------------------------
# Add New Task
# -----------------------------------------

new_task = st.text_input("Enter a New Task")

if st.button("Add Task"):

    if new_task.strip() != "":
        tasks.append(new_task)
        save_tasks(tasks)
        st.success("Task Added Successfully!")
        st.rerun()

    else:
        st.warning("Please enter a task.")

st.divider()

# -----------------------------------------
# Display Tasks
# -----------------------------------------

st.subheader("Your Tasks")

if len(tasks) == 0:
    st.info("No tasks available.")

else:

    for index, task in enumerate(tasks):

        col1, col2 = st.columns([5,1])

        with col1:
            st.write(f"• {task}")

        with col2:
            if st.button("❌", key=index):
                tasks.pop(index)
                save_tasks(tasks)
                st.rerun()

st.divider()

# -----------------------------------------
# Clear All Tasks
# -----------------------------------------

if st.button("🗑️ Clear All Tasks"):

    save_tasks([])
    st.success("All Tasks Deleted!")
    st.rerun()