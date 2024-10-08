from datetime import datetime

def age_checker(DoB):
    DatetimeDoB = datetime.strptime(DoB,"%Y-%m-%d").date()
    CurrentDate = datetime.today().date()
    age = CurrentDate.year - DatetimeDoB.year - ((CurrentDate.month, CurrentDate.day) < (DatetimeDoB.month, DatetimeDoB.day))
    if age >= 16:
        return "Access granted"
    return "Access denied - You have to be 16 or older to enter"