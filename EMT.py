def loadFile(filename):
    readfile = open(filename, 'r')
    variable = readfile.read()
    variable = variable.split('\n')
    readfile.close()
    return variable

def loadAll():
    global employeeIDs
    global firstNames
    global lastNames
    global names
    global socials
    global phones
    global emails
    global salaries
    global statuses
    employeeIDs = loadFile('employeeIDs.txt')
    EIDs = []
    for ID in employeeIDs:
      EIDs.append(int(ID))
    employeeIDs = EIDs
    firstNames = loadFile('firstNames.txt')
    lastNames = loadFile('lastNames.txt')
    names = loadFile('names.txt')
    socials = loadFile('socials.txt')
    phones = loadFile('phones.txt')
    emails = loadFile('emails.txt')
    salaries = loadFile('salaries.txt')
    statuses = loadFile('statuses.txt')
    return

def saveFile(variable, filename):
    linebreak = '\n'
    String = linebreak.join(str(v) for v in variable)
    savefile = open(filename, 'w')
    savefile.write(String)
    savefile.close()
    return

def saveAll():
    saveFile(firstNames, 'firstNames.txt')
    saveFile(lastNames, 'lastNames.txt')
    saveFile(names, 'names.txt')
    saveFile(employeeIDs, 'employeeIDs.txt')
    saveFile(socials, 'socials.txt')
    saveFile(phones, 'phones.txt')
    saveFile(emails, 'emails.txt')
    saveFile(salaries, 'salaries.txt')
    saveFile(statuses, 'statuses.txt')
    return

def employee_entry():
    print("New employee entry")
    add_employees = int(input("How many employees are you adding? Enter a positive number, or 0 to return to the menu: "))
    while add_employees < 0:
        add_employees = int(input("Invalid response. How many employees are you adding? "))
    while add_employees == 0:
        return
    else:
        entry = 0
        for employee in range(add_employees): #add error checkers for repeated info
            entry += 1
            previous_ID = employeeIDs[-1]
            previous_ID = employeeIDs.index(previous_ID)
            current_ID = previous_ID + 1
            employeeIDs.append(current_ID)
            print("The Employee ID for employee %d will be: " % entry, current_ID)
            current_first_name = input("Enter first name of employee %d: " % entry)
            current_first_name = current_first_name.title()
            firstNames.append(current_first_name)
            current_last_name = input("Enter last name of employee %d: " % entry)
            current_last_name = current_last_name.title()
            lastNames.append(current_last_name)
            current_name = ("%s %s" % (current_first_name, current_last_name))
            current_name_sorted = ("%s, %s" % (current_last_name, current_first_name))
            names.append(current_name_sorted)
            currentSSN = input("Enter social security number of %s: " % current_name)
            while currentSSN.isdigit() == False:
              currentSSN = input("Please enter social security number in numeric digits only. SSN: ")
            while len(currentSSN) != 9:
              currentSSN = input("Social Security numbers are 9 digits long. Please double-check your entry. SSN: ")
            socials.append(currentSSN)
            currentPhone = input("Enter phone number of %s: " % current_name)
            while currentPhone.isdigit() == False:
                currentPhone = input("Please enter phone number in numeric digits only; formatting will be applied. Phone number: ")
            currentPhoneParts = (currentPhone[0:3], currentPhone[3:6], currentPhone[6:10])
            currentPhone = '-'.join(currentPhoneParts)
            phones.append(currentPhone)
            currentEmail = input("Enter email address of %s: " % current_name)
            emails.append(currentEmail)
            currentSalary = input("Enter yearly salary of %s: $" % current_name) #add formatting to make sure the money has the right number of digits
            salaries.append(currentSalary)
            statuses.append('active')
            saveAll()
            print_employee(current_ID)
        return
        
def print_employee(employeeID):
    print("---------------------------- %s %s -----------------------------" % (firstNames[employeeID], lastNames[employeeID]))
    print("Employee ID:", employeeID)
    print("SSN:", socials[employeeID])
    print("Phone:", phones[employeeID])
    print("Email:", emails[employeeID])
    print("Salary: $%s" % salaries[employeeID])
    print("----------------------------------------------------------------------------")
    return

def print_phonebook(): 
    directory = []
    for each in range(len(statuses)):
      if statuses[each] == 'active':  
        directory.append(names[each])
      else:
        pass
    directory.sort()
    for name in range(len(directory)): #FIXME: when names are not unique, the same person gets displayed multiple times instead of each person displayed once
      currentEID = names.index(directory[name])
      print_employee(currentEID)
    return

def search_phonebook():
    search_options = {
        1: "1 - Search by Employee ID number",
        2: "2 - Search by Social Security number",
        3: "3 - Search by phone number",
        4: "4 - Search by name (format 'LastName, FirstName')",
        5: "5 - Never mind. Go back to the main menu."}
    search_loop = "y"
    while search_loop == "y":
      for option in search_options:
        print(search_options[option])
      method = int(input("How would you like to search? "))
      while method not in search_options:
        method = int(input("Response not recognized, please respond with one of the options listed above: "))
      if method == 1:
        searchEID = int(input("Enter an Employee ID number to search by: "))
        while searchEID not in employeeIDs:
            print('Employee IDs currently range from 1 to', employeeIDs[:-1])
            searchEID = input("Employee not found. Please try a different Employee ID number, or enter any letter to quit: ")
            if searchEID.isdigit() == False:
                search_loop = 'n'
                return
            else:
                searchEID = int(searchEID)
        while statuses[searchEID] != 'active':
            active = []
            for current in range(len(statuses)):
                if statuses[current] == 'active':
                    active.append(current)
                else:
                  pass
            print(active, "These are the IDs of the employees still with the company.")
            searchEID = input("That employee is no longer with the company. Please try a different Employee ID number, or enter any letter to quit: ")
            if searchEID.isdigit() == False:
                search_loop = 'n'
                return
            else:
                searchEID = int(searchEID)
        else:
            return(searchEID)
      elif method == 2:
        searchSSN = input("Enter a social security number to search by: ")
        while searchSSN.isdigit() == False:
          searchSSN = input("Please enter social security number in numeric digits only. SSN: ")
        while len(searchSSN) != 9:
          searchSSN = input("Social Security numbers are 9 digits long. Please double-check your entry. SSN: ")
        if (searchSSN in socials) and (statuses[socials.index(searchSSN)] == 'active'):
          searchEID = socials.index(searchSSN)
          return(searchEID)
        else:
          search_loop = input("Employee not found. Would you like to try searching again? y/n: ")
      elif method == 3:
        searchPhone = input("Enter a phone number to search by: ")
        while searchPhone.isdigit() == False:
          searchPhone = input("Please enter social security number in numeric digits only. SSN: ")
        searchPhoneParts = (searchPhone[0:3], searchPhone[3:6], searchPhone[6:10])
        searchPhone = '-'.join(searchPhoneParts)
        if (searchPhone in phones) and (statuses[phones.index(searchPhone)] == 'active'):
          searchEID = phones.index(searchPhone)
          return(searchEID)
        else:
          search_loop = input("Employee not found. Would you like to try searching again? y/n: ")        
      elif method == 4:
        searchName = input("Enter a name to search by (format 'LastName, FirstName'): ")
        searchName = searchName.title()
        if (searchName in names) and (statuses[names.index(searchName)] == 'active'): #figure out what to do if there's more than one by the same name?
          searchEID = names.index(searchName)
          return(searchEID)
        else:
            search_loop = input("Employee not found. Would you like to try searching again? y/n: ")
      else:
        print('Returning to previous menu.')
        search_loop = "n"
        return

def view_phonebook():
    print("There are currently %d employees in the phonebook." % statuses.count('active'))
    read = input("Do you want to view all of them? y/n: ")
    if read == 'y':
        print_phonebook()
        return
    else:
        searchID = search_phonebook()
        if searchID == None:
            return
        else:
            print_employee(searchID)
            edit = 'y'
            while edit == 'y':
                edit_options = {
                    1: "1 - Edit this employee's information",
                    2: "2 - Delete this employee",
                    3: "3 - Nothing, return to the main menu"}
                for option in edit_options:
                    print(edit_options[option])
                access = input("What would you like to do? ")
                if access == '1':
                    edit_employee(searchID)
                elif access == '2':
                    delete_employee(searchID)
                elif access == '3':
                    edit = 'n'
                    return
                else:
                    access = input("Response not recognized, please respond with one of the options listed above: ")
        return

def edit_employee(current_ID):
    search = 'y'
    while current_ID == None:
        current_ID = int(input("Enter the Employee ID of the employee you wish to update: "))
    #while search == 'y': #FIXME: script stops responding
    #    while (current_ID in phonebook) == False:
    #        print("Employee not found. Please verify that you have the correct Employee ID, or enter 'search' to enter search mode. Enter 'quit' to return to the previous menu.")
    #        current_ID = input("Employee ID: ")
    #        if current_ID == 'search':
    #            current_ID = search_phonebook() #test
    #        elif current_ID == 'quit':
    #            search = 'n'
    #            return
    #        else:
    #            current_ID = input("Employee not found. Please verify that you have the correct Employee ID, or enter 'search' to enter search mode. Enter 'quit' to return to the previous menu. Employee ID: ")
        while (current_ID not in employeeIDs):
            print("You'd better go check the phonebook and make sure you have the right Employee ID.")
            current_ID = search_phonebook()
        while statuses[current_ID] != 'active':
            print("That employee is no longer with the company. You'd better go check the phonebook and make sure you have the right Employee ID.")
            current_ID = search_phonebook()
        print_employee(current_ID)
        confirm = str(input("Is this the employee you wish to update? y/n: "))
        while confirm != 'y':
            print("You'd better go check the phonebook and make sure you have the right Employee ID.")
            current_ID = search_phonebook()
            print_employee(current_ID)
            confirm = str(input("Is this the employee you wish to update? y/n: "))
    else:
        current_first_name = input("Update first name of employee %d: " % current_ID) #copy over changes from functionality 1
        current_first_name = current_first_name.title()
        firstNames[current_ID] = current_first_name
        current_last_name = input("Update last name of employee %d: " % current_ID)
        current_last_name = current_last_name.title()
        lastNames[current_ID] = current_last_name
        current_name = ("%s %s" % (current_first_name, current_last_name))
        current_name_sorted = ("%s, %s" % (current_last_name, current_first_name))
        names[current_ID] = current_name_sorted
        currentSSN = input("Confirm social security number of %s: " % current_name)
        while currentSSN.isdigit() == False:
          currentSSN = input("Please enter social security number in numeric digits only. SSN: ")
        while len(currentSSN) != 9:
          currentSSN = input("Social Security numbers are 9 digits long. Please double-check your entry. SSN: ")
        socials[current_ID] = currentSSN
        currentPhone = input("Update phone number of %s: " % current_name)
        while currentPhone.isdigit() == False:
          currentPhone = input("Please enter phone number in numeric digits only; formatting will be applied. Phone number: ")
        currentPhoneParts = (currentPhone[0:3], currentPhone[3:6], currentPhone[6:10])
        currentPhone = '-'.join(currentPhoneParts)
        phones[current_ID] = currentPhone
        currentEmail = input("Update email address of %s: " % current_name)
        emails[current_ID] = currentEmail
        currentSalary = input("Update yearly salary of %s: $" % current_name)
        salaries[current_ID] = currentSalary
        saveAll()
        print("This employee is now:")
        print_employee(current_ID)
        return

def delete_employee(current_ID):
    print("WARNING: Deleting an employee is irreversible. This should only be done if an employee is no longer with the company. If the former employee rejoins the company, a new Employee ID will be assigned.")
    confirmDelete = 'n'
    while current_ID == None:
        current_ID = int(input("Enter the Employee ID of the employee you wish to delete: "))
    print("You have selected:")
    print_employee(current_ID)
    confirmDelete = input("Are you absolutely certain you want to delete this employee? Type 'DELETE' to confirm. Type anything else to go back.")
    if confirmDelete == 'DELETE':
        statuses[current_ID] = 'inactive'
        saveAll()
        print("Deletion complete. Now returning to main menu.")
        return
    else:
        print("Deletion not confirmed. Now returning to main menu.")
        return

def main_menu():
    read_options = {
        1: "1 - Enter new employee information",
        2: "2 - View current employee information",
        3: "3 - Edit existing employee",
        4: "4 - Delete an employee",
        5: "5 - Export employee information into a text file",
        6: "6 - Import employee information from a text file",
        7: "7 or Q - Quit"}
    menu_loop = "y"
    while menu_loop == "y":
        for option in read_options:
            print(read_options[option])
        print(("-------------------------------------------------------------------------------------------").center(0))
        access = input("Please enter your option number: ")
        if access == '1':
            employee_entry()
        elif access == '2':
            view_phonebook()
        elif access == '3':
            edit_employee(None)
        elif access == '4':
            delete_employee(None)
        elif access == '5':
            print("Thanks for your diligence! But the export function happens automatically.")
        elif access == '6':
            print("Thanks for your diligence! But the import function happens automatically. You'll notice there are already some employees in the phonebook.")
        elif access == '7' or 'q' or 'Q':
            saveAll()
            menu_loop = "n"
            print("Now exiting system. Goodbye.")
        else:
          print("Response not recognized, please respond with one of the options listed below.")

employeeIDs = [0]
firstNames = [0]
lastNames = [0]
names = [0]
socials = [0]
phones = [0]
emails = [0]
salaries = [0]
statuses = [0]

print(("------------------------ Employee Management System ---------------------------").center(0))
loadAll()
print(('There are currently %d employees in the phonebook.' % statuses.count('active')).center(0))
print(('-------------------------------------------------------------------------------------------').center(0))
main_menu()
