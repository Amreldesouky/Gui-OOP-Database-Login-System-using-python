import mysql.connector
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='mydatabase'
)

my_cursor = mydb.cursor()

fileName = ''
img = ''
window = tk.Tk()
window.geometry('400x200+400+300')
window.title("Save Data")

def upload_image():
    global fileName, img
    fileName = filedialog.askopenfilename(
        filetypes=[("png file", "*.png"), ("JPG file", "*.jpg"), ("JPEG file", "*.JPEG")]
    )

    if fileName:
        img = Image.open(fileName)
        img = img.resize((100, 100))
        img = ImageTk.PhotoImage(img)
        label = tk.Label(image=img, width=100, height=100)
        label.grid(row=3, column=1)

def convertToBinary(filename):
    with open(filename, 'rb') as file:
        bd = file.read()
    return bd

choices = ['Add', 'Check']

def submit(edit, edit1, edit2):
    sql = "INSERT INTO student (user, password, name, pic) values (%s,%s,%s,%s)"
    pic = convertToBinary(fileName)
    data = (edit.get(), edit1.get(), edit2.get(), pic)
    try:
        my_cursor.execute(sql, data)
        mydb.commit()
        messagebox.showinfo('Message', 'Done!')
    except mysql.connector.Error as err:
        messagebox.showinfo('Message', f"Error : {err}")

def check(edit,edit1):
    usr = edit.get()
    pas = edit1.get()
    sql = f"SELECT * FROM student WHERE user='{usr}' AND password='{pas}'"
    my_cursor.execute(sql)
    result = my_cursor.fetchone()
    if result:

        messagebox.showinfo('Message', f"Name : {result[2]} \n Username : {result[0]} \n password : {result[1]} \n ")
    else:
        messagebox.showinfo('Message', "Wrong data !!!!")
        
    

def ad_ch():
    selected = selected_choice.get()
    button.grid_forget()
    option_menu.grid_remove()
    if selected == 'Add':
        # Create Entry widgets before calling submit
        label = tk.Label(text='Enter username : ', width=15)
        label.grid(row=0, column=0)
        edit = tk.Entry(width=30)
        edit.grid(row=0, column=1)

        label1 = tk.Label(text='password : ', width=15)
        label1.grid(row=1, column=0)
        edit1 = tk.Entry(width=30)
        edit1.grid(row=1, column=1)

        label2 = tk.Label(text='Enter Name : ', width=15)
        label2.grid(row=2, column=0)
        edit2 = tk.Entry(width=30)
        edit2.grid(row=2, column=1)
        
        button1 = tk.Button(text='Upload image', command=upload_image, bg="#581845", fg='white')
        button1.grid(row=0, column=2)
        
        # Submit button with direct call (variables defined earlier)
        button2 = tk.Button(text='Submit', command=lambda: submit(edit, edit1, edit2))
        button2.grid(row=4, column=1)
          # Now variables are defined
    else:
        label = tk.Label(text='Enter username : ', width=15)
        label.grid(row=0, column=0)
        edit = tk.Entry(width=30)
        edit.grid(row=0, column=1)

        label1 = tk.Label(text='password : ', width=15)
        label1.grid(row=1, column=0)
        edit1 = tk.Entry(width=30)
        edit1.grid(row=1, column=1)
        
        button2 = tk.Button(text='Check', command=lambda: check(edit, edit1) )
        button2.grid(row=4, column=1)
        




selected_choice = tk.StringVar(window)
selected_choice.set(choices[0])
option_menu = tk.OptionMenu(window, selected_choice, *choices)
option_menu.grid(row=0, column=0)

button = tk.Button(text='select', command=ad_ch)
button.grid(row=4, column=1)

window['bg'] = '#B2BEB5'
# window.iconbitmap('C:\\Users\\Amr\\Desktop\\INSTANT\\project_1\\GUI_Python\\images\\10207manstudentlightskintone_110568.ico')  # Replace with your icon path
window.mainloop()





















# try:
#     my_cursor.execute()
#     #result = my_cursor.fetchall()
#     mydb.commit()
#     print("Record inserted successfully")
# except mysql.connector.Error as err:
#     print("Error:", err)
# finally:
#      my_cursor.close()
#      mydb.close()  # Always close connections to avoid resource leaks