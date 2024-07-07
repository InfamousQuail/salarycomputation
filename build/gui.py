import GrossSalary

from pathlib import Path



from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, StringVar, IntVar

import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Jonathan Macatantgay\Desktop\Salaryyy\build\assets\frame0")
# change your path depende kung saan makikita yung assets na "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#---------------------------- SEE DETAIL BUTTON --------------------------------

def toggle_details():
    if details_frame.winfo_viewable():
        details_frame.place_forget()
    else:
        details_frame.place(x=0, y=0)

#-------------------------------------------------------------------------------


#--------------------------------- FUNCTIONS -----------------------------------

def update_gross_salary(*args):
   
    gross_salary = GrossSalary.gross_salary(
        rate_of_pay_var.get(),
        work_hour_var.get(),
        total_days_of_work_var.get(),
        overtime_var.get(),
        absence_var.get()
    )
    gross_salary_var.set(gross_salary)

#-----------------------------------------------------------------------------------
    
window = Tk()

window.geometry("556x377")
window.configure(bg = "#F4EEEE")


canvas = Canvas(
    window,
    bg = "#F4EEEE",
    height = 377,
    width = 556,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

#------------------- StringVar/trace-adds ----------------------------

gross_salary_var = StringVar()
gross_salary_var.trace_add("write", update_gross_salary)

absence_var = StringVar()
absence_var.trace_add("write", update_gross_salary)

overtime_var = StringVar()
overtime_var.trace_add("write", update_gross_salary)

work_hour_var = StringVar()
work_hour_var.trace_add("write", update_gross_salary)

rate_of_pay_var = StringVar()
rate_of_pay_var.trace_add("write", update_gross_salary)

total_days_of_work_var = StringVar()
total_days_of_work_var.trace_add("write", update_gross_salary)


#-----------------------------------------------


canvas.place(x = 0, y = 0)
botimage = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    279.0,
    335.0,
    image=botimage
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    448.0,
    65.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    278.0,
    65.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    107.0,
    65.0,
    image=image_image_4
)

# ---------------------- BUTTON (SEE DETAILS) --------------------- 
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
detailbtn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=toggle_details,
    relief="flat"
)
detailbtn.place(
    x=218.0,
    y=85.0,
    width=120.0,
    height=41.0
)

# FRAME (SEE DETAILS) ----------------------------------------------------
details_frame = Frame(
    window,
    bg = "#F4EEEE",
    height = 139,
    width = 556,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")


details_frame.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("bgframe.png"))
image_1 = canvas.create_image(
    278.0,
    72.0,
    image=image_image_1
)

details_frame.place_forget()

# ----------------------- CANVA INSIDE SEE DETAIL FRAME (See Detail Button)---------------------------

details_canva = Canvas(
    details_frame,
    bg = "#F4EEEE",
    height = 139,
    width = 556,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

details_canva.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("bgframe.png"))
image_1 = details_canva.create_image(
    278.0,
    72.0,
    image=image_image_1
)

details_canva.create_text(
    252.0,
    77.0,
    anchor="nw",
    text="PhilHealth",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

details_canva.create_text(
    448.0,
    77.0,
    anchor="nw",
    text="Total",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

details_canva.create_text(
    64.0,
    21.0,
    anchor="nw",
    text="Loan",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

details_canva.create_text(
    56.0,
    77.0,
    anchor="nw",
    text="SSS/GSIS",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

details_canva.create_text(
    252.0,
    21.0,
    anchor="nw",
    text="PAG-IBIG",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

details_canva.create_text(
    450.0,
    21.0,
    anchor="nw",
    text="Tax",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

details_canva.create_rectangle(
    40.0,
    70.99998899175588,
    516.0,
    72.00003051757812,
    fill="#CFCFCF",
    outline="")


details_canva.create_text(
    41.0,
    43.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)


# ------------------------------ VALUES TO REFLECT -----------------------
details_canva.create_text(
    55.0,
    43.0,
    anchor="nw",
    text="1000.00",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    56.0,
    96.0,
    anchor="nw",
    text="4000.00",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    238.0,
    43.0,
    anchor="nw",
    text="2000.00",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    239.0,
    96.0,
    anchor="nw",
    text="5000.00",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    418.0,
    43.0,
    anchor="nw",
    text="3000.00",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    418.0,
    96.0,
    anchor="nw",
    text="6000.00",
    fill="#FF5757",
    font=("Outfit Bold", 16 * -1)
)

# -------------------------------------------------------------------------------

details_canva.create_text(
    41.0,
    96.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    404.0,
    43.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    404.0,
    96.0,
    anchor="nw",
    text="₱",
    fill="#FF5757",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    224.0,
    43.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    224.0,
    96.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

xbuttonimg= PhotoImage(
    file=relative_to_assets("xbutton.png"))

xbutton = Button(
    details_canva,
    image=xbuttonimg,
    borderwidth=0,
    highlightthickness=0,
    command=toggle_details,
    relief="flat"
)
xbutton.place(
    x=516.0,
    y=21.0,
    width=16.0,
    height=16.0
)

# ------------------------ NOT IMPORTANT --------------------------
canvas.create_text(
    46.0,
    34.0,
    anchor="nw",
    text="Gross Salary",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_text(
    46.0,
    140.0,
    anchor="nw",
    text="Name",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_text(
    432.0,
    140.0,
    anchor="nw",
    text="Working Days",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_text(
    49.0,
    218.0,
    anchor="nw",
    text="Rate of Pay",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_text(
    70.0,
    306.0,
    anchor="nw",
    text="Loan per Month",
    fill="#000000",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_text(
    205.0,
    306.0,
    anchor="nw",
    text="SSS/GSIS",
    fill="#000000",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_text(
    329.0,
    306.0,
    anchor="nw",
    text="PAG-IBIG",
    fill="#000000",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_text(
    447.0,
    306.0,
    anchor="nw",
    text="PhilHealth",
    fill="#000000",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_text(
    175.0,
    218.0,
    anchor="nw",
    text="Work Hours",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_text(
    304.0,
    218.0,
    anchor="nw",
    text="Total OT Hours",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_text(
    431.0,
    218.0,
    anchor="nw",
    text="Days of Absence",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_text(
    218.0,
    34.0,
    anchor="nw",
    text="Deductions",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_text(
    389.0,
    34.0,
    anchor="nw",
    text="Net Salary",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)

canvas.create_rectangle(
    40.0,
    190.00000425054495,
    516.0,
    191.0000457763672,
    fill="#CFCFCF",
    outline="")

canvas.create_rectangle(
    40.0,
    352.9999889917559,
    516.0,
    354.0000305175781,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    40.0,
    269.99998899175586,
    516.0,
    271.0000305175781,
    fill="#CFCFCF",
    outline="")

canvas.create_text(
    47.0,
    52.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 24 * -1)
)

canvas.create_text(
    47.0,
    327.0,
    anchor="nw",
    text="₱",
    fill="#FF5757",
    font=("Outfit Bold", 16 * -1)
)

canvas.create_text(
    45.0,
    243.0,
    anchor="nw",
    text="₱",
    fill="#545454",
    font=("Outfit Bold", 16 * -1)
)

canvas.create_text(
    219.0,
    52.0,
    anchor="nw",
    text="₱",
    fill="#FF5757",
    font=("Outfit Bold", 24 * -1)
)

canvas.create_text(
    390.0,
    52.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 24 * -1)
)
# -----------------------------------------------------------


# ---------------------- IMPORTANT --------------------------


gross_salary_label = Label(
    canvas,
    background= "#FFFFFF",
    textvariable=gross_salary_var,
    font=("Outfit Bold", 24 * -1),
    
)

gross_salary_label.place(
    x=69.0,
    y=50.0
)

#---------------------------------------------------------------


canvas.create_text(
    241.0,
    52.0,
    anchor="nw",
    text="41.00",     # <<< DEDUCTION VALUE (placeholder)
    fill="#FF5757",
    font=("Outfit Bold", 24 * -1)
)

canvas.create_text(
    412.0,
    52.0,
    anchor="nw", 
    text="71.00",     # <<< NET SALARY VALUE (placeholder)
    fill="#000000",
    font=("Outfit Bold", 24 * -1)
)

# ---------------------- NOT IMPORTANT STUFF ---------------------------
canvas.create_text(
    110.0,
    243.0,
    anchor="nw",
    text="/hr",
    fill="#545454",
    font=("Outfit Bold", 16 * -1)
)

canvas.create_text(
    220.0,
    243.0,
    anchor="nw",
    text="hr/day",
    fill="#545454",
    font=("Outfit Bold", 16 * -1)
)

canvas.create_text(
    353.0,
    243.0,
    anchor="nw",
    text="hr(s)",
    fill="#545454",
    font=("Outfit Bold", 16 * -1)
)

canvas.create_text(
    478.0,
    243.0,
    anchor="nw",
    text="day(s)",
    fill="#545454",
    font=("Outfit Bold", 16 * -1)
)

canvas.create_text(
    478.0,
    162.0,
    anchor="nw",
    text="days",
    fill="#545454",
    font=("Outfit Bold", 16 * -1)
)

# ---------------------------------------------------------------------------


# LOAN INPUT ---------------------------------------------------------------

loan = Entry(
    bd=0,
    bg="#FFDE59",
    fg="#FF5757",
    highlightthickness=0,
    font=("Outfit Bold", 16 * -1),
    justify='left'
)
loan.place(
    x=62.0,
    y=328.0,
    width=110.0,
    height=16.0
)

# ABSENCE INPUT ----------------------------------------------------




total_days_of_absent = Entry(
    canvas,
    textvariable=absence_var,
    bd=0,
    bg="#F4EEEE",
    fg="#000716",
    highlightthickness=0,
    font=("Outfit Bold", 19 * -1),
    justify="center"
)

total_days_of_absent.place(
    x=436.0,
    y=243.0,
    width=37.0,
    height=18.0
)

# OVER-TIME HOUR INPUT ------------------------------------------------------




total_overtime_in_hour_in_month = Entry(
    window,
    textvariable=overtime_var,
    bd=0,
    bg="#F4EEEE",
    fg="#000716",
    highlightthickness=0,
    font=("Outfit Bold", 19 * -1),
    justify="center"
)
total_overtime_in_hour_in_month.place(
    x=312.0,
    y=243.0,
    width=37.0,
    height=18.0
)

# WORK HOUR INPUT ------------------------------------------------------




total_working_hours = Entry(
    window,
    textvariable=work_hour_var,
    bd=0,
    bg="#F4EEEE",
    fg="#000716",
    highlightthickness=0,
    font=("Outfit Bold", 19 * -1),
    justify="center"
)
total_working_hours.place(
    x=179.0,
    y=243.0,
    width=37.0,
    height=18.0
)

# RATE OF PAY INPUT -----------------------------------------------------------




salary_rate = Entry(
    window,
    textvariable=rate_of_pay_var,
    bd=0,
    bg="#F4EEEE",
    fg="#000716",
    highlightthickness=0,
    font=("Outfit Bold", 19 * -1),
    justify="center"
)

salary_rate.place(
    x=58.0,
    y=243.0,
    width=50.0,
    height=18.0
)

# WORKING DAY INPUT ---------------------------------------------------------




total_days_of_work_in_month = Entry(
    window,
    textvariable=total_days_of_work_var,
    bd=0,
    bg="#F4EEEE",
    fg="#000716",
    highlightthickness=0,
    font=("Outfit Bold", 19 * -1)
)
total_days_of_work_in_month.place(
    x=445.0,
    y=162.0,
    width=25.0,
    height=22.0
)

# NAME INPUT ----------------------------------------------------------------

name = Entry(
    bd=0,
    bg="#F4EEEE",
    fg="#000716",
    highlightthickness=0,
    font=("Outfit Bold", 19 * -1)
)
name.place(
    x=59.0,
    y=162.0,
    width=250.0,
    height=22.0
)


# checkbox  ------------------------------------------------------------------

checkbox_varGsis = tk.BooleanVar()
checkbox_varPagibig = tk.BooleanVar()
checkbox_varPhilhealth = tk.BooleanVar()

# Callback functions
def on_check1():
    print("CheckboxGsis is checked" if checkbox_varGsis.get() else "CheckboxGsis is unchecked")

def on_check2():
    print("CheckboxPagibig is checked" if checkbox_varPagibig.get() else "CheckboxPagibig is unchecked")

def on_check3():
    print("CheckboxPhilhealth is checked" if checkbox_varPhilhealth.get() else "CheckboxPhilhealth is unchecked")

# Checkbuttons
checkboxGsis = tk.Checkbutton(window,variable=checkbox_varGsis,background="#FFDE59", foreground= "#FF5757", command=on_check1)
checkboxGsis.place(
    x=221.0, 
    y=330.0,
    width=15.0, 
    height=15.0
)

checkboxPagibig = tk.Checkbutton(window,variable=checkbox_varPagibig, background="#FFDE59", foreground= "#FF5757", command=on_check2)
checkboxPagibig.place(
    x=346.0,
    y=330.0,
    width=15.0,
    height=15.0,
)

checkboxPhilhealth = tk.Checkbutton(window,variable=checkbox_varPhilhealth, background="#FFDE59", foreground= "#FF5757", command=on_check3)
checkboxPhilhealth.place(
    x=464.0,
    y=330.0,
    width=15.0,
    height=15.0,
)



window.resizable(False, False)
window.mainloop()