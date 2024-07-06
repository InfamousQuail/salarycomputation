def gross_salary(salary_rate,total_working_hours,total_days_of_work_in_month,total_overtime_in_hour_in_month,total_days_of_absent):

    total_hours_worked = (total_working_hours * (total_days_of_work_in_month - total_days_of_absent)) + total_overtime_in_hour_in_month

    return total_hours_worked * salary_rate

 #example input
rate_of_pay = 500
work_hr = 8
total_days_of_work_in_month = 20
total_overtime_in_hour_in_month = 8
total_days_of_absent = 2

print(gross_salary(rate_of_pay))
