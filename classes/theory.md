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

###Class and Static Methods.
1. In addition to instance methods, python has static and class methods.
2. In class methods, the class is implicitly passed as the first argument,
whereas in static methods, neither the instance object not the class is passed.
3. Static methods are like regular functions that are grouped with the class 
namespace because they're somehow conceptually related to the class.

###Dunder dict
1. All instance attributes are stored in an instance-specific mapping object.
2. For instances, that mapping object is a plain python dictionary.
3. It is accessed using instance.__dict__ syntax.

###Class vs Instance__dict__
1. Just like instances, classes have their own attribute namespace.
2. Just as for instances, it too is accessed using __dict__.
3. Unlike instances, however, the class __  is a mappingproxy, which is a 
more restricted type of read-only dictionary where all the keys are strings.
4. The class __dict__ contains all the instance, class, and static methods we 
define, in addition to class variables.
5. It also contains some descriptors and other class dunders.
