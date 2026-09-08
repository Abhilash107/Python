class Time:
    """Class Time with read-write properties."""
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        """Return self._hour"""
        return self._hour
    
    @hour.setter
    def hour(self, hour):
        if not ( 0 <= hour < 24):
            print("Error")
        
        self._hour = hour
    
    @property
    def minute(self):
        """Return minute."""
        return self._minute
    
    @minute.setter
    def minute(self, minute):
        """set the miute"""
        if not (0 <= minute < 60):
            print("Error")
            return
        
        self._minute = minute
    
    @property
    def second(self):
        """Return the seconds."""
        return self._second
    
    @second.setter
    def second(self, second):
        """Set the second"""
        if not (0 <= second < 60):
            print("Error")
        
        self._second = second

    #Method set_time
    def set_time(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    #Special Method __repr__
    def __repr__(self):
        """Return time String."""
        return(f'Time(hour= {self.hour}, minute={self.minute}, ' + f'second={self.second})')
    

    # Special Method __str__
    # def __str__(self):
    #     """Print Time in 12-hour clock format"""
    #     return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
    #             f':{self.minute:0>2}:{self.second:0>2}' +
    #             (' AM' if self.hour < 12 else ' PM'))
    
    @property
    def time(self):
        """Return hour, minute and second as a tuple."""
        return (self.hour, self.minute, self.second)
    
    @time.setter
    def time(self, *time_tuple):
        """Set time from a tuple containing hour, minute and second."""
        self.set_time(time_tuple[0], time_tuple[1], time_tuple[2])
        
    
    
    




#The single-leading-underscore (_) naming convention indicates that client code should not access _hour directly.
# The @property decorator precedes the property’s getter method, which receives only a self parameter. scenes, a decorator adds code to the decorated function—in
# this case to make the hour function work with attribute syntax. The getter method’s name
# is the property name. This getter method returns the _hour data attribute’s value.


# A decorator of the form @property_name.setter (in this case, @hour.setter) precedes
# the property’s setter method. The method receives two parameters—self and a
# parameter (hour) representing the value being assigned to the property. If the hour parameter’s
# value is valid, this method assigns it to the self object’s _hour attribute

# Using the setter enabled us to validate __init__’s hour argument before creating and initializing
# the object’s _hour attribute, which occurs the first time the hour property’s setter
# executes as a result of line 9. A read-write property has both a getter and a setter. A readonly
# property has only a getter.


# The Python documentation indicates that __repr__ returns the “official” string representation
# of the object. Typically this string looks like a constructor expression that creates
# and initializes the object,2 as in:
# 'Time(hour=6, minute=30, second=0)'


# Python has a built-in function eval that could receive the preceding string as an argument and use
# it to create and initialize a Time object containing values specified in the string.

# __str__ special method. This method is called implicitly when you convert an object to a string with the built-in function str, such as when you print an object or call str explicitly.


#A(n) ______ property has both a getter and setter. If only a getter is provided,
# the property is a(n) ______ property, meaning that you only can get the property’s
# value.
# Answer: read-write, read-only.




