import tkinter as tk
from exam_frontend import api
from exam_frontend.connection_dialog import ConnectionDialog
from exam_frontend.ui import App

def main():
    root = tk.Tk()
    root.withdraw() 

    dialog = ConnectionDialog(root)
    if not dialog.confirmed:
        root.destroy()
        return
        
    
    api.BASE_URL = dialog.url
    api.HEADERS = {"X-API-Key": dialog.token}

    root.deiconify() 
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()