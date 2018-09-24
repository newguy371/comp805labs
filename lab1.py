"""
Intro to Python data structures
lab1start.py
Chris Howell
Updated 9/17/2018
"""

def squared_nums(num_list):
    """
    Squares numbers in num_list
    num_list: list of numbers
    Returns: A list of these numbers squared
    """
    result = []
	
    for num in num_list:
       num = num*num 
       result.append(num)

    return result
	
def filter_digits(any_str_list):
    """
    Removes strings in any_str_list that have digits in them
    any_str_list: list of strings
    Returns: ist of strings that do not have digits in them
    """
    result = []
	
    for word in any_str_list:
        if any(word.isdigit for word in any_str_list):
	        any_str_list.remove(word)

    return any_str_list

def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: dictionary with:
      key: string that is the name of the inventory item
      value: integer that equals the number of that item currently on hand
    Returns: updated dictionary where each inventory item is restocked
    """
    
    for key in inventory.keys():
        inventory[key] = inventory[key] + 10
    return inventory

def filter_0_items(inventory):
    """
    Removes items with value of 0 in the dictionary inventory
    inventory: dictionary with:
      key: string that is the name of the inventory item
      value: integer that equals the number of that item currently on hand
    Returns: updated inventory with any item that had 0 quantity removed
    """
    
    result = {}
    for key, val in inventory.items():    
        inventory.update(result)
        if val > 0:
            inventory.update(result)
            result[key] = inventory[key]
    return result
            
def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: dictionary of grades with:
      key: string that has the name of a student
      value: list of integer grades received in class
    Returns: dictionary that has grade average values associated with student
    names
    """
    result = {}
    avg = []
	
    for key, val in grades.items():
        grades[key] = sum(val)/len(val)
        grades.update(result)
            
if __name__ == '__main__':
    t1 = squared_nums([1, 2, 3])
    print(t1)
	
    t2 = squared_nums([5, 10, 7])
    print(t2)
	
    t3 = squared_nums([4, 12, 6])
    print(t3)

    s = filter_digits(['Hell0 World', 'Hello World'])
    print(s)
	
    s2 = filter_digits(['Good-b1y3', 'fat guy', 'sw1tcher'])
    print(s2)
	
    s3 = filter_digits(['one1',' ', '598524395823945h'])
    print(s3)

    d = restock_inventory({'pencil':10, 'pen':8, 'paper':7})
    print(d)
	
    d2 = restock_inventory({'eraser':21, 'paper clip':56, 'staples':0})
    print(d2)
	
    d3 = restock_inventory({'melons':192, 'food':13.5, 'stuff':693})
    print(d3)
	
    d = filter_0_items({'pen':8, 'eraser':0, 'paper':1})
    print(d)
	
    d2 = filter_0_items({'trains':0, 'planes':0, 'automobiles':0})
    print(d2)
	
    d3 = filter_0_items({'canyons':20, 'rivers':1, 'mountains':46})
    print(d3)

    d = average_grades({'Mike':[78, 100, 88], 'Sam':[0, 65, 80], 'Josh':[80, 80, 80]})
    print(d)