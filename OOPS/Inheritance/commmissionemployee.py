from decimal import Decimal

class CommissionEmployee:
    def __init__(self, f_name, l_name, ssn, gross_sales, comm_rate):
        self._f_name = f_name
        self._l_name = l_name
        self._ssn = ssn
        self._gross_sales = gross_sales
        self._comm_rate = comm_rate
    
    @property # getter f_name
    def f_name(self):
        return self._f_name
    
    @property # getter l_name
    def l_name(self):
        return self._l_name
    
    @property # getter ssn
    def ssn(self):
        return self._ssn
    
    @property # getter gross_sale
    def gross_sales(self):
        return self._gross_sales
    
    @gross_sales.setter
    def gross_sales(self, sales):
        if sales < Decimal('0.00'):
            raise ValueError('Gross sales must be >= 0')
        
        self._gross_sales = sales
    
    @property # getter comm_rate
    def comm_rate(self):
        return self._comm_rate
    
    @comm_rate.setter
    def comm_rate(self, rate):
        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError('Interest rate must be greater than 0 and less than 1')
        
        self._comm_rate = rate
    
    def earning(self):
        return self.gross_sales * self.comm_rate
    
    def __repr__(self):
        """Return string representation for repr()."""
        return (f'CommissionEmployee: {self.f_name} {self.l_name}\n' +
                f'Social Security Number: {self.ssn}\n' +
                f'Gross Sales: {self.gross_sales:.2f}\n' +
                f'Commission Rate: {self.comm_rate:.2f}')
    
