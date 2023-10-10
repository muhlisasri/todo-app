import PySimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo")
add_button = gui.Button("add")
window = gui.Window('My To-Do App', layout=[[label, input_box, add_button]])
window.read()
window.cose()
