# Custom exception classes

class ParsingError(Exception):
    '''Something went wrong while creating time object'''
    pass


class NullValueError(ParsingError):
    '''
    No value was passed for creation of time object
    
    Attributes:
    error_item: The item that failed validation
    error_message: Description of the validation error
    '''

    def __init__(self, error_message: str):
        self.error_message = error_message


class FormatError(ParsingError):
    '''
    Invalid format of time passed for creation of time object
    
    Attributes:
    error_item: The item that failed validation
    error_message: Description of the validation error
    '''

    def __init__(self, error_message: str, error_item: str):
        self.error_message = error_message
        self.error_item = error_item


class CalculationError(Exception):
    '''Something went wrond while performing some operation'''
    pass


class InvalidOperandError(CalculationError):
    '''
    Operation with passed operand(s) in not defined
    
    Attributes:
    error_item: The item that failed validation
    error_message: Description of the validation error
    '''

    def __init__(self, error_message: str, error_item: str):
        self.error_message = error_message
        self.error_item = error_item


class ZeroDivisionError(CalculationError):
    '''
    Dividing time by zero is not defined
    
    Attributes:
    error_item: The item that failed validation
    error_message: Description of the validation error
    '''
    
    def __init__(self, error_message: str):
        self.error_message = error_message
