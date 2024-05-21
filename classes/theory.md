###What classes are?
1. A class is a blueprint that represents a type of object.
2. Even the simples class has state and behaviour.
3. Calling the class creates instances (or objects) of the class.

###Class State
1. We traditionally define a class state in the class body.
2. Class state is stored in a mappingproxy object and retrieved using
__dict__ attribute.
3. Class state is shared and acessible by all instances of that class.

###Methods and Behaviours
1. We add behaviours to a class by defining methods in the class body.
2. These functions are special in that they always have at least one parameter.
3. That parameter is by convention called self.
4. Whe functions are defined within the body of a class, they become bound (or
attached) to instances of that class.

###Instance and Attributes
1. Attributes are simply variables associated with objects.
2. Instance attributes could be set before or after the instance object is returned.
3. That's said, it's a best practice to set them in __init__, a special method which
exists specifically for this purpose.

###Alternatively: getattr() and setattr()
1. In addition to the traditional dot access syntax, attributes could also be 
read and set using getattr() and setattr() built-in functions.
2. These methods are most useful if we're manipulating objects programmatically
and especially if we're doing so at scale.

###Revisiting self
1. self is the first argument passed to instance methods.
2. It presents the instance object to the method.
3. It is called self by convention only, and self is neither a reserved keyword
nor does it have any special meaning in python.
