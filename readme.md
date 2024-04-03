# HW.10 StackOverflow Report Generation

This task involves creating a report from StackOverflow's 2023 survey data. The report will highlight the most popular developer activities, languages, frameworks, tools, operating systems, and industry.

You'll learn to process CSV data in Python with multi-dimensional list, use the `collections.Counter` library for item counts occurrence, and create report from the data.

No user interface is needed for this task. The report result is the return value of `generate_report` function (dictionary format).
<br>

## Requirements

1. **Read and process CSV data**: The `csv` module is used to read the StackOverflow survey data from a CSV file (`stackoverflow_survey.csv`). There are 10 fields in the CSV file, detail of each field is listed below:

    - **CodingActivities:** Developer's coding activities, what they are using coding for. `dev_activities` is a key for this field.
    
    - **LanguageHaveWorkedWith:** Programming languages that developers have worked with. `most_used_language` is a key for this field.
    
    - **LanguageWantToWorkWith:** Programming languages that developers want to work with. `most_wanted_language` is a key for this field.
    
    - **WebframeHaveWorkedWith:** Web frameworks that developers have worked with. `most_used_framework` is a key for this field.
    
    - **WebframeWantToWorkWith:** Web frameworks that developers want to work with. `most_wanted_framework` is a key for this field.
    
    - **NewCollabToolsHaveWorkedWith:** New collaboration tools that developers have worked with. `most_used_tool` is a key for this field.
    
    - **NewCollabToolsWantToWorkWith:** New collaboration tools that developers want to work with. `most_wanted_tool` is a key for this field.
    
    - **OpSysPersonal use:** Operating systems that developers use for personal use. `most_personal_operating_system` is a key for this field.
    
    - **OpSysProfessional use:** Operating systems that developers use for professional use. `most_professional_operating_system` is a key for this field.
    
    - **Industry:** Industry that developers work in. `popular_industry` is a key for this field.

<br>

2. **Data extraction and analysis**: The `collections.Counter` library is used to count the occurrences of each item in specific columns of the CSV file. **Only include three most common items in each category**.

<br>

3. **Generate report**: The `generate_report` function uses the `Counter` to extract and count data from specific columns, and then returns a dictionary containing the three most common items in each category (use key that represent each csv field as mention in point 1) as `key` and number of its occurrence as `value`.

Expected output is a dictionary with the following structure:
```python
{
  'dev_activities': {
                    'Hobby': 51942, 
                    'Professional development or self-paced learning from online courses': 26957, 
                    'Contribute to open-source projects': 18231
                  }, 
  'most_used_language': {
                    'JavaScript': 55711, 
                    'HTML/CSS': 46396, 
                    'Python': 43158
                    }, 
  'most_wanted_language': {
                    'JavaScript': 34986, 
                    'Python': 34715, 
                    'TypeScript': 32256
                    }, 
  'most_used_framework': {
                    'Node.js': 30626, 
                    'React': 29137, 
                    'jQuery': 15784}, 
  'most_wanted_framework': {
                    'React': 24100, 
                    'Node.js': 23027, 
                    'Next.js': 14129
                    }, 
  'most_used_tool': {
                    'Visual Studio Code': 63793, 
                    'Visual Studio': 24605, 
                    'IntelliJ IDEA': 23209
                  }, 
  'most_wanted_tool': {
                    'Visual Studio Code': 50588, 
                    'IntelliJ IDEA': 16887, 
                    'Visual Studio': 15755
                    }, 
  'most_personal_operating_system': {
                    'Windows': 52086, 
                    'MacOS': 28407, 
                    'Ubuntu': 23791
                    }, 
  'most_professional_operating_system': {
                    'Windows': 40917, 
                    'MacOS': 28786, 
                    'Ubuntu': 23281
                    }, 
  'popular_industry': {
                    'Information Services, IT, Software Development, or other Technology': 18159, 
                    'Financial Services': 4421, 
                    'Other': 4011
                    }
}

```

<br>

## Extra: Using the `collections.Counter` Library

The `collections.Counter` library in Python is a dictionary subclass for counting hashable objects. It's a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

### Example 1: Counting Items in a List

```python
from collections import Counter

# Create a list of items
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

# Create a Counter object from the list
counter = Counter(items)

# Print the counter
print(counter)  # Output: Counter({'banana': 3, 'apple': 2, 'orange': 1})
```

In this example, `Counter(items)` creates a `Counter` object from the list `items`. The `Counter` object is a dictionary where the keys are the unique items in the list and the values are the counts of their occurrences.

<br>

### Example 2: Counting Characters in a String

```python
from collections import Counter

# Create a string
text = "banana"

# Create a Counter object from the string
counter = Counter(text)

# Print the counter
print(counter)  # Output: Counter({'a': 3, 'n': 2, 'b': 1})
```

In this example, `Counter(text)` creates a `Counter` object from the string `text`. The `Counter` object is a dictionary where the keys are the unique characters in the string and the values are the counts of their occurrences.

<br>

### Example 3: Accessing Counts

You can access the count of a specific item using square brackets `[]`:

```python
print(counter['a'])  # Output: 3
```

This will print the count of 'a' in the `counter`.

<br>

### Example 4: Getting Most Common Items

You can also use the `most_common()` method to get a list of the elements and their counts, sorted by the count:

```python
print(counter.most_common())  # Output: [('a', 3), ('n', 2), ('b', 1)]
```

This will print a list of tuples, where each tuple contains an element and its count, sorted by the count in descending order.

<br>

### Example 5: Convert Counter to Dictionary

You can convert a `Counter` object to a dictionary using the `dict()` constructor:

```python
dict_counter = dict(counter)

print(dict_counter)  # Output: {'b': 1, 'a': 3, 'n': 2}
```
