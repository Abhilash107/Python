class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def __add__(self, right):
        return Complex(self.real + right.real, self.img+ right.img)
    
    def __iadd__(self, right):
        self.real += right.real
        self.img += right.img
        return self
    
    def __sub__(self, right):
        return Complex(self.real - right.real, self.img - right.img)
    
    def __isub__(self, right):
        self.real -= right.real
        self.img -= right.img
        return self
    
    def __repr__(self):
        """Return string representation for repr()."""
        return (f'({self.real} ' +
        ('+' if self.img >= 0 else '-') +
        f' {abs(self.img)}i)')
    
    def __getitem__(self, index):
        if index == 0:
            return self.real
        elif index == 1:
            return self.img
        else:
            raise IndexError("Index out of range. Use 0 for real, 1 for imaginary.")
    
    def __imul__(self, right):
        temp_real = self.real * right.real - self.img * right.img
        temp_img = self.real * right.img + self.img * right.real
        self.real = temp_real
        self.img = temp_img
        return self




# Methods that overload binary operators must provide two parameters—the first (self) is the left operand and the second (right) is the right operand
