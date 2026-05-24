# import required modules
import timecalc.operations as op
import timecalc.exceptions as e

# global constants
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600

# Time class definition
class Time:
    # constructor method
    def __init__(self, time_str: str=None, time_int: int=None):
        if time_int is not None:
            self.time_int = time_int
        elif time_str is not None:
            if op.is_valid(time_str):
                self.time_int = op.parse_time_str(time_str)
            else:
                raise e.FormatError("Invalid format of time passed for creation of time object", time_str)
        else:
            raise e.NullValueError("No value was passed for creation of time object")
    
    # method to get current time
    @classmethod
    def now(cls):
        curr_time = op.get_curr_time()
        return Time(curr_time)

    # method to generate random timestamp
    @classmethod
    def rand(cls):
        rand_time = op.gen_rand_time()
        return Time(rand_time)

    # addition dunder method
    def __add__(self, other):
        if type(other) is not Time:
            raise e.InvalidOperandError("Addition can be performed only between two timestamps", other)
        result = self.time_int + other.time_int
        return Time(time_int = result)

    # substraction dunder method
    def __sub__(self, other):
        if type(other) is not Time:
            raise e.InvalidOperandError("Substaction can be performed only between two timestamps", other)
        result = self.time_int - other.time_int
        return Time(time_int = result)

    # division dunder method
    def __truediv__(self, other):
        if type(other) is int:
            if other == 0:
                raise e.ZeroDivisionError("Dividing time by zero is not defined")
            result = self.time_int // other
            return Time(time_int = result)
        elif type(other) is Time:
            if other.time_int == 0:
                raise e.ZeroDivisionError("Dividing time by zero is not defined")
            result = self.time_int // other.time_int
            return result
        else:
            raise e.InvalidOperandError("Division is only defined with scalars or timestamps", other)
    
    # modulo dunder method
    def __mod__(self, other):
        if type(other) is not Time:
            raise e.InvalidOperandError("Remainder of division is defined only for two timestamps", other)
        result = self.time_int % other.time_int
        return Time(time_int = result)

    # multiplication dunder method
    def __mul__(self, other):
        if type(other) is not int:
            raise e.InvalidOperandError("Multiplication is only defined with scalars", other)
        result = self.time_int * other
        return Time(time_int = result)

    # right-shift dunder method (used find time in between two timestamps)
    def __rshift__(self, other):
        if type(other) is not Time:
            raise e.InvalidOperandError("Time can only be calculated between two timestamps", other)
        result = other.time_int - self.time_int
        return Time(time_int = result)

    # equals dunder method
    def __eq__(self, other):
        if type(other) is not Time:
            raise e.InvalidOperandError("Compaison operation is defined only between two timestamps", other)
        if self.time_int == other.time_int:
            return True
        return False

    # not-equals dunder method
    def __ne__(self, other):
        if type(other) is not Time:
            raise e.InvalidOperandError("Compaison operation is defined only between two timestamps", other)
        if self.time_int != other.time_int:
            return True
        return False

    # less-than dunder method
    def __lt__(self, other):
        if type(other) is not Time:
            raise e.InvalidOperandError("Compaison operation is defined only between two timestamps", other)
        if self.time_int < other.time_int:
            return True
        return False

    # less-than-equalto dunder method
    def __le__(self, other):
        if type(other) is not Time:
            raise e.InvalidOperandError("Compaison operation is defined only between two timestamps", other)
        if self.time_int <= other.time_int:
            return True
        return False

    # greater-than dunder method
    def __gt__(self, other):
        if type(other) is not Time:
            raise e.InvalidOperandError("Compaison operation is defined only between two timestamps", other)
        if self.time_int > other.time_int:
            return True
        return False

    # greater-than-equalto dunder method
    def __ge__(self, other):
        if type(other) is not Time:
            raise e.InvalidOperandError("Compaison operation is defined only between two timestamps", other)
        if self.time_int >= other.time_int:
            return True
        return False
    
    # represent time as string
    def __str__(self):
        return op.format_time_int(self.time_int)
