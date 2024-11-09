def filter_and_modify(data_list, **kwargs):
    filtered_data = [
        item for item in data_list
        if all (item.get(key) == value for key, value in kwargs.items() if key in item)] 
    for item in filtered_data:
        for key, value in kwargs.items():
            if key not in item:
                item[key] = value
    return filtered_data
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "charlie", "age": 35, "city": "New York"},
    {"name": "Diana", "age": 30, "city": "Chicago"}
]
filtered_data = filter_and_modify(data, age = 30, city = "New York", occupation = "Engineer")
print(filtered_data)