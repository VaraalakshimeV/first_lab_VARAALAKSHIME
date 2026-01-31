class Calculator:
    """An enhanced calculator class for various arithmetic operations."""
    
    @staticmethod
    def _validate_numbers(*args):
        """Validates that all arguments are numbers."""
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Expected number, got {type(arg).__name__}")
    
    @staticmethod
    def add_two(a, b):
        """Returns the sum of two numbers."""
        Calculator._validate_numbers(a, b)
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Returns the difference between two numbers."""
        Calculator._validate_numbers(a, b)
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Returns the product of two numbers."""
        Calculator._validate_numbers(a, b)
        return a * b
    
    @staticmethod
    def add_three(a, b, c):
        """Returns the sum of three numbers."""
        Calculator._validate_numbers(a, b, c)
        return sum([a, b, c])
    
    @staticmethod
    def divide(a, b):
        """
        Returns the division of two numbers.
        
        Parameters:
            a (int/float): Numerator
            b (int/float): Denominator
            
        Returns:
            float: a / b
            
        Raises:
            ZeroDivisionError: If b is zero
        """
        Calculator._validate_numbers(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def power(base, exponent):
        """
        Returns base raised to the power of exponent.
        
        Parameters:
            base (int/float): Base number
            exponent (int/float): Exponent
            
        Returns:
            int/float: base ^ exponent
        """
        Calculator._validate_numbers(base, exponent)
        return base ** exponent
    
    @staticmethod
    def modulo(a, b):
        """
        Returns the remainder of a divided by b.
        
        Parameters:
            a (int/float): Dividend
            b (int/float): Divisor
            
        Returns:
            int/float: a % b
        """
        Calculator._validate_numbers(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulo with zero")
        return a % b
    
    @staticmethod
    def average(*numbers):
        """
        Calculates the average of any number of values.
        
        Parameters:
            *numbers: Variable number of numeric arguments
            
        Returns:
            float: Average of all numbers
        """
        if not numbers:
            raise ValueError("At least one number required")
        Calculator._validate_numbers(*numbers)
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def percentage(value, total):
        """
        Calculates what percentage value is of total.
        
        Parameters:
            value (int/float): Part value
            total (int/float): Total value
            
        Returns:
            float: Percentage
        """
        Calculator._validate_numbers(value, total)
        if total == 0:
            raise ZeroDivisionError("Total cannot be zero")
        return (value / total) * 100
    
    @staticmethod
    def square_root(n):
        """
        Returns the square root of a number.
        
        Parameters:
            n (int/float): Number to find square root of
            
        Returns:
            float: Square root of n
        """
        Calculator._validate_numbers(n)
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return n ** 0.5
    
    @staticmethod
    def absolute(n):
        """Returns the absolute value of a number."""
        Calculator._validate_numbers(n)
        return abs(n)
    
    @staticmethod
    def min_of_list(*numbers):
        """Returns the minimum value from a list of numbers."""
        if not numbers:
            raise ValueError("At least one number required")
        Calculator._validate_numbers(*numbers)
        return min(numbers)
    
    @staticmethod
    def max_of_list(*numbers):
        """Returns the maximum value from a list of numbers."""
        if not numbers:
            raise ValueError("At least one number required")
        Calculator._validate_numbers(*numbers)
        return max(numbers)


# Example usage:
# calc = Calculator()
# result1 = calc.add_two(2, 3)           # 5
# result2 = calc.subtract(2, 3)          # -1
# result3 = calc.multiply(2, 3)          # 6
# result4 = calc.add_three(result1, result2, result3)  # 10
# result5 = calc.divide(10, 2)           # 5.0
# result6 = calc.power(2, 3)             # 8
# result7 = calc.average(1, 2, 3, 4, 5)  # 3.0
# result8 = calc.percentage(25, 10

