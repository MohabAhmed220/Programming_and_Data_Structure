def say_my_name(first_name, last_name=" "):
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
if__name__=="__main__":
    say_my_name("John", "Doe")
    say_my_name("Jane")