EMPLOYEES = [
    {
        "name": "Jeremy Bakker",
        "animalId": 2,
        "id": 1,
        "locationId": 2
    },
    {
        "name": "Johnny Smith",
        "animalId": 1,
        "id": 2,
        "locationId": 2
    }
]


def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def delete_employee(id):
    # Initial -1 value for animal index, in case one isn't found
    employee_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
