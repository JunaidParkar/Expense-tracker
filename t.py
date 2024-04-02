import customtkinter as ctk
import os
from paths import routes, RouteType

router = routes("self")
window = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
js_font = ctk.FontManager.load_font(f"{os.path.join(router.getRoute(RouteType.ASSETS_FONT_DIR), "js.ttf")}")
window.geometry(f"{screen_width}x{screen_height}+0+0")
window.minsize(screen_width, screen_height)
window.maxsize(screen_width, screen_height)

headings = ["Sr no.", "Date", "Amount", "Description", "Category", "Type", ""]

# Create a frame with specified dimensions and background color
table = ctk.CTkFrame(window, width=1200, height=screen_height, bg_color="white")
table.pack()

table_heading_frame = ctk.CTkFrame(table, width=1200, height=50, fg_color="red")
table_heading_frame.place(x=0, y=0)

for i,  header in enumerate(headings):
    row_frame = ctk.CTkLabel(table_heading_frame, text=header, width=self.column_widths[i], anchor='center')
    row_frame.grid(row=0, column=i)



window.mainloop()
