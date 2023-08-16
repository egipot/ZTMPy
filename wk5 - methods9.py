#Documenting with Docstrings  

# EGI NOTE1: DEFINE DOCSTRING WITHIN THE BODY OF THE CLASS or FUNCTION (which means indented once)
# EGI NOTE2: HELP COMMAND IS INDENTED AT THE LEVEL OF WHERE THE DOCSTRING REFERS TO

#The Python help function can be super helpful for easily pulling up documentation for classes and methods. We can call the help function on one of our classes, which will return some basic info about the methods defined in our class:


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

help (Apple)
# ^This outputs:
# Help on class Apple in module __main__:

#class Apple(builtins.object)
# |  Apple(color, flavor)
# |
# |  Methods defined here:
# |
# |  __init__(self, color, flavor)
# |      Initialize self.  See help(type(self)) for accurate signature.
# |
# |  __str__(self)
# |      Return str(self).
# |
# |  ----------------------------------------------------------------------
# |  Data descriptors defined here:
# |
# |  __dict__
# |      dictionary for instance variables (if defined)
# |
# |  __weakref__
# |      list of weak references to the object (if defined)



#We can add documentation to our own classes, methods, and functions using docstrings. 
# A docstring is a short text explanation of what something does. 
# You can add a docstring to a method, function, or class by first defining it, 
# then adding a description inside triple quotes.  