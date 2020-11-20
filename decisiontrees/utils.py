"""Helpers that will be used in the project"""

import csv


def convertTypes(value):
    """Helper to convert the type into float or int.
    
    Args:
        value(str): The value that will be converted to float or int.

    Returns: 
        The converted value.
    """
    value = value.strip()
    try:
        return float(value) if '.' in value else int(value)
    except ValueError:
        return value


def loadCSV(input_file):
	"""Loads a CSV file and converts all floats and ints into basic datatypes.
    
    Args:
        input_file: The file that will be loaded.

    Returns:
        List with the converted information from the csv file.
    """
    with open(input_file, 'rt') as csv_file:
        reader = csv.reader(csv_file)

    result = [[convertTypes(item) for item in row] for row in reader]

    if result:
        return result
    
    return None


def uniqueCounts(rows):
    results = {}
    for row in rows:
        r = row[-1]
        if r not in results: results[r] = 0
        results[r] += 1

	return results


def divide_set(rows, column, value):
    splittingFunction = None
    if isinstance(value, int) or isinstance(value, float): # for int and float values
        splittingFunction = lambda row : row[column] >= value
    else: # for strings 
        splittingFunction = lambda row : row[column] == value
    list1 = [row for row in rows if splittingFunction(row)]
    list2 = [row for row in rows if not splittingFunction(row)]
    
    return (list1, list2)

