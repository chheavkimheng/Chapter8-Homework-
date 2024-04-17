import csv 
from collections import Counter 
 
def return_list_row(index: int)-> list: 
         
    with open("stackoverflow_survey.csv", "r") as file: 
        reader = csv.reader(file) 
        next(reader) 
             
        data_lists = [] 
        semicolon_lists = [] 
             
        for data in reader: 
            if data[index] != "NA":  
                data_lists.append(data[index]) if ";" not in data[index] else semicolon_lists.append(data[index].split(";"))  
             
        for item in semicolon_lists: 
            data_lists += item  
             
        return data_lists 
 
def generate_report(): 
    ''' 
    Generate a report based on the data from the CSV file. 
    Returns: 
        dict: A dictionary containing the report data. The keys are: 
            - 'dev_activity': A dictionary containing the count of developers based on their activity. 
            - 'most_used_language': A dictionary containing the count of developers based on the most used language. 
            - 'most_wanted_language': A dictionary containing the count of developers based on the most wanted language. 
            - 'most_used_framework': A dictionary containing the count of developers based on the most used framework. 
            - 'most_wanted_framework': A dictionary containing the count of developers based on the most wanted framework. 
            - 'most_used_tool': A dictionary containing the count of developers based on the most used tool. 
            - 'most_wanted_tool': A dictionary containing the count of developers based on the most wanted tool. 
            - 'most_used_operating_system': A dictionary containing the count of developers based on the most used operating system. 
            - 'most_wanted_operating_system': A dictionary containing the count of developers based on the most wanted operating system. 
            - 'top_three_industry': A dictionary containing the count of developers based on the top three industries they work in. 
    ''' 
         
    category_lists = ['dev_activities', 'most_used_language', 'most_wanted_language', 'most_used_framework','most_wanted_framework', 'most_used_tool', 'most_wanted_tool', 'most_personal_operating_system', 'most_professional_operating_system', 'popular_industry'] 
    report = {category:dict(Counter(return_list_row(index)).most_common(3)) for index, category in enumerate(category_lists)} 
     
    return report 
         
print(generate_report())