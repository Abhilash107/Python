from commmissionemployee import CommissionEmployee

from decimal import Decimal

emp = CommissionEmployee('Sue', 'Jones', '333-33-3333', Decimal('10000.00'), Decimal('0.06'))
# print(emp)
# print(emp.earing())# 600.0000, it's a method
# emp.comm_rate = Decimal('0.1')
emp._comm_rate = Decimal('0.2')
# print(emp.earing())

# IMP: To ensure proper encapsulation and validation, always use the property setter (emp.comm_rate) instead of directly modifying the private attribute (emp._comm_rate).

# Q. (What Does This Code Do?) In this section’s IPython session, explain in detail what
# snippet [6] does:
# c.gross_sales = Decimal('20000.00')
# Answer: This statement creates a Decimal object and assigns it to a CommissionEmployee’s
# gross_sales property, invoking the property’s setter. The setter checks whether the
# new value is less than Decimal('0.00').

from salariedcommissionemployee import SalariedCommissionEmployee
s = SalariedCommissionEmployee('Abhilash', 'Mishra', '333-33-3333', Decimal('10000.00'), Decimal('0.06'), Decimal('3000'))
# print(s)
# print(s.earning())
# print(f'{s.earning():,.2f}')
# print(s.f_name, s.l_name, s.ssn, s.gross_sales, s.comm_rate, s.base_salary)


#Testing the “is a” Relationship
# print(issubclass(CommissionEmployee, SalariedCommissionEmployee))# false
# print(issubclass(SalariedCommissionEmployee, CommissionEmployee ))# TRUE
# print(isinstance(s, SalariedCommissionEmployee ))# TRUE
# print(isinstance(s, CommissionEmployee ))# TRUE
# print(isinstance(emp, SalariedCommissionEmployee ))# False
# Function isinstance determines whether an object has an “is a” relationship with a
# specific type. Because SalariedCommissionEmployee inherits from CommissionEmployee,
# both of the following snippets return True, confirming the “is a” relationship



employees = [emp, s]
# for e in employees:
#     print(f'{e}\n')

# CommissionEmployee: Sue Jones
# Social Security Number: 333-33-3333
# Gross Sales: 10000.00
# Commission Rate: 0.20

# SalariedCommissionEmployee: Abhilash Mishra
# Social Security Number: 333-33-3333
# Gross Sales: 10000.00
# Commission Rate: 0.06
# base salary: 3000.00


# As you can see, the correct string representation and earnings are displayed for each
# employee. This is called polymorphism—a key capability of object-oriented programming
# (OOP)

from duck import WellPaidDuck
d = WellPaidDuck()
employee_list = [emp, s, d]
for e in employee_list:
    print(f'{e}')
    print(f'{e.earning():,.2f}\n')

# OUTPUT: 
# CommissionEmployee: Sue Jones
# Social Security Number: 333-33-3333
# Gross Sales: 10000.00
# Commission Rate: 0.20
# 2,000.00

# SalariedCommissionEmployee: Abhilash Mishra
# Social Security Number: 333-33-3333
# Gross Sales: 10000.00
# Commission Rate: 0.06
# base salary: 3000.00
# 3,600.00

# I am a well-paid duck
# 1,000,000.00
