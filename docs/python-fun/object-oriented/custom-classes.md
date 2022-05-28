Class customization is the process of defining how a class should behave for some common operations. Such operations might include:

- printing
- accessing attributes
- how instance objects are to compared to each other

## Memory allocation

The process of an application requesting and being granted memory is known as **memory allocation**.

Memory used by a Python application must be granted by the operating system. When an application requests specific amount of memory, the operating system can then choose to grant or deny the request. 

Some programming languages require the programmer to write memory allocation code; the Python runtime handles memory allocation _for_ the programmer. This saves a programmer time by not having to write out the code. 

## Derived classes

A class will commonly share attributes with another class with the freedom to maneuver in that specific classes use of the commonalities in additions and variations.

A basic example is a store might have a class called `Item` that serves as a _base class_ that more specific classes (ie clothes, produce, electronics) would all be able to use `class Item`'s attributes as they usually can all make use of attributes such as _name_ and _quantity_.

_Derived class_ refers to a class that inherits the class attributes of another class, known as a _base class_. Any class may serve as a base class; no changes to the definition of that class are required.

- The derived class is said to _inherit_ the attributes of its base class, a concept commonly called _inheritance_.
- An instance of a derived class type has access to all the attributes of the derived class as well as the class attributes of the base class by default, including the base class' methods.
- A derived class instance can simulate inheritance of instance attributes as well by calling the base class constructor manually.
- A derived class can itself serve as a base class for another class.
- A class can serve as a base class for multiple derived classes.
- A class may be derived from multiple classes.

## Overriding class methods

A derived class may define a method having the same name as a method in the base class. Such a member function _overrides_ the method of the base class. When the derived class defines the method being overwritten, that method is placed in the class's namespace. Because attribute references search the inheritance tree by starting with the derived class and then recursively searching base classes, the method called will al ways be the method defined in the instance's class.

Overriding does _not mean_ replacing the base class methods, but rather _extending_. The base class can be explicitly called at the start of the method, with the derived class then performing additional operations.

## Derivation IS A extension of the base

**Inheritance** models what is called an _is a_ relationship. This means that when you have a derived class that inherits from a base class, you created a relationship where derived _is a_ specialized version of base. 

``` mermaid
classDiagram
Base <|-- Derived : extends
```

!!! note "Inheritance relationships"
    - Classes that inherit from another are called derived classes, subclasses, or subtypes.
    - Classes from which other classes are derived are called base classes or super classes.
    - A derived class is said to derive, inherit, or extend a base class.

### Inheritance puts the "L" in SOLID

Ever heard of [_SOLID_ design principles](https://en.wikipedia.org/wiki/SOLID){:target="\_blank"}? 

In object-oriented programming, _SOLID_ is an acronym for "five design principles which are intended to make software designs more understandable, flexible, and maintainable." I'm not going to list them all out here but I left the link for a stellar description from Wikipedia. 

The "L" in SOLID stands for [Liskov substitution](https://en.wikipedia.org/wiki/Liskov_substitution_principle){:target="\_blank"} which basically states that "in a computer program, if S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desired properties of the program."

So through inheritance, we can model class hierarchies without changing the behavior of a base class by extending that base class into a subclass which _is a_ specialized version of the base class.

## Considering Scalability

So, inheritance sounds great and it totally is! I'm just sitting over here thinking about what happens in two, three, four years when a company's requirements change for employee id's, internal identity access management redefines which users will have access to particular services that the company provides, etc. If this company  initially used the inheritance model that derives from a hierarchy of base classes, updating these objects to scale with a company as it grows doesn't seem that ideal.

## Composition HAS A Component

**Composition** is an object oriented design concept that models a _has a_ relationship. 

In composition, a class known as a **composite** contains an object of another class known as a **component**. In simpler terms, a composite class **has a** component of another class. 

Like inheritance, the design principle is code reuse, but composition allows composite classes to reuse the implementation of the components it contains. The composite class doesn't inherit the component class _interface_, but it can leverage its implemenation. 

The composite relationship between two classes is considered "loosely coupled." This means that changes to the component class rarely affect the composite class, and changes to the composite class _never_ affect the component class. 

This provides better adaptability to change and allows applications to introduce new requirements without affecting existing code. 

This design approach would be a scalable alternative to the ever-intertwining inheritance design problem considered above.

``` mermaid
classDiagram
Composite *-- Component
```

Composition is represented in UML with a diamond at the composite class pointing to the component class.

!!! info "Classes that contain objects of other classes are usually referred to as composites, where classes that are used to create more complex types are referred to as components."
