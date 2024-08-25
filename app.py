from main import Freelancer
from datetime import datetime

current_date = datetime.now()



Emp_1 = Freelancer(101, "Rohit Singh", "rohituid30@gmail.com", current_date)
print(f"the id is {Emp_1.id}")
print(f"the name is {Emp_1.name}")
print(f"the email is {Emp_1.email}")
print(f"the datetime is {Emp_1.adate}")