def gross_salary(salary_rate, total_working_hours, total_days_of_work_in_month, total_overtime_in_hour_in_month, total_days_of_absent):
    
    try:
        salary_rate = float(salary_rate)
        total_working_hours = float(total_working_hours)
        total_days_of_work_in_month = float(total_days_of_work_in_month)
        total_overtime_in_hour_in_month = float(total_overtime_in_hour_in_month)
        total_days_of_absent = float(total_days_of_absent)

        total_hours_worked = (total_working_hours * (total_days_of_work_in_month - total_days_of_absent)) + total_overtime_in_hour_in_month
        grosssalary = total_hours_worked * salary_rate

        return grosssalary
    except ValueError:
        return "Error"
