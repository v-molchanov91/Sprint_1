class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(cls, name, hourse=None, rest_days=None, email=None):
        if self.hours is None and self.rest_days is not None:
            self.hours = (7 - self.rest_days) * 8
        return cls(name, hours, rest_days, email)

    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if self.email is None:
            self.email = f"{self.name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        hours = self.get_hours()
        return hours * self.hourly_payment
