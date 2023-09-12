class Employee:
    company_name = "Dev.boot"
    total_employees = 0

    def __init__(self, first_name, last_name, id, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary
        Employee.total_employees += 1

    def get_name(self):
        return f"{self.first_name} {self.last_name}"


def test_create_employee(first_name, last_name, id, position, salary):
    print("-- Adding Employee --")
    emp = Employee(first_name, last_name, id, position, salary)
    print(f"Name: {emp.get_name()}")
    print(f"ID: {emp.id}")
    print(f"Position: {emp.position}")
    print(f"Salary: {emp.salary}")
    print(f"Total Employees at {Employee.company_name}: {Employee.total_employees}")
    print("=====================================")
    return emp


def main():
    employee1 = test_create_employee("John", "Cena", 1001, "Manager", 50000)
    employee2 = test_create_employee(
        "Alice", "Wendall", 1002, "Assistant Manager", 45000
    )
    employee3 = test_create_employee(
        "Emily", "Morcovich", 1003, "Marketing Manager", 55000
    )


main()
