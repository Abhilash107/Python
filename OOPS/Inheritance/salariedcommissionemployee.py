from decimal import Decimal
from commmissionemployee import CommissionEmployee

class SalariedCommissionEmployee(CommissionEmployee):
    def __init__(self, f_name, l_name, ssn, gross_sales, comm_rate, base_salary):
        super().__init__(f_name, l_name, ssn, gross_sales, comm_rate)
        self.base_salary = base_salary
    
    @property
    def base_salary(self):
        return self._base_salary
    
    @base_salary.setter
    def base_salary(self, salary):
        if salary < Decimal('0.0'):
            raise ValueError('Base salary must be >= to 0')
        
        self._base_salary = salary
    
    def earning(self):
        return super().earning() + self.base_salary# super
    
    def __repr__(self):
            """Return string representation for repr()."""# super
            return ('Salaried' + super().__repr__() +
            f'\nbase salary: {self.base_salary:.2f}')
    

    



# No, your code will not work as expected because the parent class (CommissionEmployee) uses f_name and l_name as the attribute names for the first and last names, but in the child class (SalariedCommissionEmployee), you are passing first_name and last_name to the parent class constructor. This mismatch will cause an error.
#The parameter names in the child class must match the parameter names expected by the parent class's __init__ method. Choose consistent naming conventions (f_name/l_name or first_ ame/last_name) across your classes to avoid confusion. If you want to use different names in the child class, you must explicitly map them when calling super().__init__()