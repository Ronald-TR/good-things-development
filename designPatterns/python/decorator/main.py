from designPatterns.python.decorator.decorator import hello_decorator

def echo_name_01(name):
    return f"Your name: {name}"

# calling without sugar sintax @ for decorators
name = hello_decorator(echo_name_01)('Ronald')
print(name)

@hello_decorator
def echo_name_02(name):
    return f"Your name: {name}"

#calling with the sugar sintax, much better... right?
name = echo_name_02('Ronald')
print(name)
