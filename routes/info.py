import tkinter as tk
from tkinter import font as tkfont

class Information:
    def __init__(self, root):
        self.root = root
        self.root.title("Information")
        self.root.geometry("500x350")
    
        self.title_font = tkfont.Font(size=12, weight="bold")
        self.about_font = tkfont.Font(size=10)
        
        self.pages = [
            "Page 1",
            "Page 2",
            "Page 3"
        ]
    
        self.about_content = (
            "About This Project\n\n"
        )
        
        self.current_page = 0
        self.saved_page = 0
        self.in_about = False
        
        self.create_widgets()
        self.update_content()
    
    def create_widgets(self):
        self.header_frame = tk.Frame(self.root)
        self.header_frame.pack(fill="x", padx=10, pady=10)
        
        self.about_btn = tk.Button(
            self.header_frame, 
            text="About",
            command=self.show_about
        )
        self.about_btn.pack(side="left")
        
        self.page_counter_frame = tk.Frame(self.header_frame)
        self.page_counter_frame.pack(side="left", expand=True, fill="x")

        self.left_spacer = tk.Label(self.page_counter_frame, width=1)
        self.left_spacer.pack(side="left", expand=True)
        
        self.page_label = tk.Label(
            self.page_counter_frame, 
            text=f"Page {self.current_page + 1} of {len(self.pages)}",
            font=self.title_font
        )
        self.page_label.pack(side="left")

        self.right_spacer = tk.Label(self.page_counter_frame, width=1)
        self.right_spacer.pack(side="left", expand=True)
        
        self.close_about_btn = tk.Button(
            self.header_frame, 
            text="X",
            command=self.close_about
        )
        
        self.content_label = tk.Label(
            self.root, 
            text="", 
            wraplength=450,
            justify="center",
            font=self.about_font
        )
        self.content_label.pack(expand=True, fill="both", padx=20, pady=10)

        self.nav_frame = tk.Frame(self.root)
        self.nav_frame.pack(side="bottom", fill="x", padx=10, pady=10)
        
        self.prev_btn = tk.Button(
            self.nav_frame, 
            text="<", 
            width=5,
            command=self.prev_page,
            state="disabled"
        )
        self.prev_btn.pack(side="left")
        
        self.next_btn = tk.Button(
            self.nav_frame, 
            text=">", 
            width=5,
            command=self.next_page
        )
        self.next_btn.pack(side="right")
    
    def update_content(self):
        if not self.in_about:
            self.page_label.config(text=f"Page {self.current_page + 1} of {len(self.pages)}")
            self.content_label.config(text=self.pages[self.current_page])

            self.prev_btn.config(state="normal" if self.current_page > 0 else "disabled")
            self.next_btn.config(state="normal" if self.current_page < len(self.pages) - 1 else "disabled")
    
    def show_about(self):
        self.in_about = True
        self.saved_page = self.current_page

        self.page_label.config(text="About This Project")
        self.content_label.config(text=self.about_content)

        self.close_about_btn.pack(side="right")
        self.about_btn.config(state="disabled")
        self.nav_frame.pack_forget()
    
    def close_about(self):
        self.in_about = False
        
        self.close_about_btn.pack_forget()
        self.about_btn.config(state="normal")
        self.nav_frame.pack(side="bottom", fill="x", padx=10, pady=10)
        
        self.current_page = self.saved_page
        self.update_content()
    
    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            self.update_content()
    
    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_content()


root = tk.Tk()
app = Information(root)
root.mainloop()