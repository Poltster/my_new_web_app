import streamlit as st
import functions


todos = functions.get_adatok()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo +'\n')
    functions.write_adatok(todos)

st.title("My Todo App")
st.subheader("This is my subheather")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip("\n"), key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_adatok(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input("", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

st.session_state

