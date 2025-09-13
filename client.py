  from tkinter import *
from app import *
from tkinter import ttk


URL = "http://127.0.0.1:5000"


def hide_all(root):
    for frame in root.winfo_children():
        frame.destroy()


class Landing(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x900")
        self.configure()
        Button(self,text="Register for event",command=lambda: register_page(self)).pack(pady=50)
        Button(self,text="Admin",command= lambda: admin_page(self)).pack(pady=50)
        Button(self,text="Quit",command=self.quit).pack(pady=50)



def landing_page(root):
    lp = LandingFrame(root)

def register_page(root):
    u = User(root)

def admin_page(root):
    a = Admin(root)

class User(Frame):
    def __init__(self,root):
        super().__init__()
        self.root = root
        hide_all(self.root)
        Label(self.root,text="Milestone Engineering Day Competition").pack(padx=50,pady=50)
        reg_frame = Frame(self.root)
        reg_frame.pack(padx=50,pady=50)
        self.name = Entry(reg_frame)
        self.email = Entry(reg_frame)
        self.phone=Entry(reg_frame)
        self.event = Entry(reg_frame)
        Label(reg_frame,text="Name : ").grid(row=0,column=0,padx=20,pady=20)
        Label(reg_frame,text="Email : ").grid(row=1,column=0,padx=20,pady=20)
        Label(reg_frame,text="Phone : ").grid(row=2,column=0,padx=20,pady=20)
        Label(reg_frame,text="Event : ").grid(row=3,column=0,padx=20,pady=20)
        self.name.grid(row=0,column=1,padx=20,pady=20)
        self.email.grid(row=1,column=1,padx=20,pady=20)
        self.phone.grid(row=2,column=1,padx=20,pady=20)
        self.event.grid(row=3,column=1,padx=20,pady=20)
        Button(self.root,text="Register Now",command = self.try_register).pack(pady=20)
        Button(self.root, text="Go back to main page", command=lambda: landing_page(self.root)).pack(pady=20)

    def try_register(self):
        name = self.name.get()
        email = self.email.get()
        phone = self.phone.get()
        event = self.event.get()
       # response = requests.post(f"{URL}/register",json={"name":name,"email":email,"phone":phone,"event":event})
        data = register(name,email,phone,event)
        if data.get("status") == "success":
            Label(self.root,text="Registered Successfully").pack(pady=20)
        else:
            Label(self.root, text="Something Went Wrong").pack(pady=50)



class Admin(Frame):
    def __init__(self,root):
        super().__init__()
        self.root = root
        hide_all(self.root)
        Label(self.root,text="This is admin page").pack()
        Label(self.root,text="Choose Event").pack()
        event = Entry(self.root)
        event.pack()
        Button(self.root,text="View registrations",command=lambda: self.view(event.get())).pack()

    def view(self,event):
        rec = get_records(event)
        hide_all(self.root)
        style = ttk.Style()
        style.theme_use('clam')
        tree = ttk.Treeview(self.root, column=("Name", "Email", "Phone","Event"), show='headings', height=5)
        tree.column("# 1", anchor="center")
        tree.heading("# 1", text="Name")
        tree.column("# 2", anchor="center")
        tree.heading("# 2", text="Email")
        tree.column("# 3", anchor="center")
        tree.heading("# 3", text="Phone")
        tree.column("# 4", anchor="center")
        tree.heading("# 4", text="Event")

        # Insert the data in Treeview framee
        for i in rec:
            tree.insert('', 'end', text="1", values=i)

        tree.pack()
        Button(self.root, text="Go back to main menu",command=lambda:landing_page(self.root)).pack()



class LandingFrame(Frame):
    def __init__(self,root):
        super().__init__()
        self.root = root
        hide_all(self.root)
        Button(self.root,text="Register for event",command=lambda: register_page(self.root)).pack(pady=50)
        Button(self.root,text="Admin",command= lambda: admin_page(self.root)).pack(pady=50)
        Button(self.root, text="Quit", command=self.quit).pack(pady=50)


if __name__ == "__main__":
    l = Landing()
    l.mainloop()



