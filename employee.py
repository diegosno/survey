def employee_number():
    existing_employee = input(
        'Do you have an employee number? (Yes/No)\n')
    while True:
        if existing_employee.lower() in ['yes', 'no']:
            break
        else:
            print('INVALID: Value should be yes or no.\n')
            existing_employee = input().lower()


employee_number()
