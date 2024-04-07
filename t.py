import customtkinter as ctk
import os
from paths import routes, RouteType

router = routes("self")
window = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
js_font = ctk.FontManager.load_font(os.path.join(router.getRoute(RouteType.ASSETS_FONT_DIR), "js.ttf"))
window.geometry(f"{screen_width}x{screen_height}+0+0")
window.minsize(screen_width, screen_height)
window.maxsize(screen_width, screen_height)
js_font = 'Century Gothic' if not js_font else js_font

table_width = 1200
headings = ["Sr no.", "Date", "Amount", "Description", "Category", "Type", ""]
column_widths = [50, 100, 100, 500, 200, 200, 100]
# Create a frame with specified dimensions and background color
table = ctk.CTkFrame(window, width=table_width, height=screen_height)
table.pack()

table_heading_frame = ctk.CTkFrame(table, width=table_width, height=150, fg_color="red")
table_heading_frame.place(x=0, y=15)

for i, header in enumerate(headings):
    row_frame = ctk.CTkLabel(table_heading_frame, fg_color="green", text=header, width=column_widths[i], anchor='center', font=(js_font, 18, "bold"))
    row_frame.grid(row=0, column=i)

datas = [
    ("2025-04-04", "25000000000000", "Purchased PS5 for arisha shaikh for her birthday as a best birthday gift for her", "gaming", "neg"),
]

# for i, data in enumerate(datas):
#     row_frame = ctk.CTkLabel()

window.mainloop()
