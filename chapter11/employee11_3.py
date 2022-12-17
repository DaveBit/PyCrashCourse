class Employee:
    """description"""
    def __init__(self, first_name, last_name, annual_salary):
        """Initiates de class and stores the parameters as attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary)

    def give_raise(self, raise_amount=5000):
        """give a raise"""
        self.annual_salary += raise_amount

