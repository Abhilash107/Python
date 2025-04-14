# 📘 Notes: Crafting Valuable Classes & Object-Based Programming in Python

---

## 🔹 Crafting Valuable Classes

- Learn to create **custom classes** to meet application-specific needs.
- Focus on **object-oriented programming (OOP)** principles:
  - Classes
  - Objects
  - Inheritance
  - Polymorphism
- OOP supports better:
  - Design
  - Implementation
  - Testing
  - Debugging
  - Maintenance
- Sections 10.1–10.9 cover hands-on code and concepts.
- Sections 10.10–10.15 (optional): provide additional perspectives and features.

---

## 🔹 Class Libraries and Object-Based Programming

- Most Python OOP is **object-based**, meaning:
  - You **use** existing classes more often than you create new ones.
- Examples:
  - Built-ins: `int`, `str`, `list`, `dict`, etc.
  - Libraries: `Decimal`, `NumPy`, `Matplotlib`, `pandas`
- **Class libraries**:
  - Collections of reusable classes.
  - Built by Python open-source community.
  - Encourage **code reuse** (no need to reinvent the wheel).
- Benefits of open-source libraries:
  - Tested
  - Bug-free
  - Performance-optimized
  - Cross-platform
- Sources: GitHub, BitBucket, SourceForge
- Installation: `pip` or `conda`
- A key reason for Python’s popularity.

---

## 🔹 Creating Your Own Custom Classes

- Custom classes = **new data types** (e.g., `CommissionEmployee`, `Time`, `Card`)
- Most personal projects use **few** custom classes.
- Industrial applications may contain **hundreds or thousands**.
- You may contribute classes to the open-source community.
- Organizations often have open-sourcing policies.

---

## 🔹 Inheritance

- Enables **new classes** to inherit features from **existing classes**.
- Promotes **code reuse** and easier maintenance.
- Terms:
  - **Base class / Superclass**: the existing class.
  - **Derived class / Subclass**: the new class.
- You can **customize** inherited behavior as needed.
- Always try to inherit from a base class **close to your needs**.
- Know your **class libraries** to use inheritance effectively.

---

## 🔹 Polymorphism

- Lets you program “in the general” rather than “in the specific.”
- The **same method call** behaves differently based on the object’s type.
- Achieved via:
  - **Inheritance**
  - **Duck typing** (if it behaves like a duck, it *is* a duck)
- Enhances flexibility and reduces code duplication.

---

## 🔹 Case Study: Card-Shuffling-and-Dealing Simulation

- Builds on random number techniques (used in dice rolling/craps).
- Uses **Matplotlib** to display card deck:
  - Before shuffle
  - After shuffle
- Exercises include:
  - Blackjack
  - Solitaire
  - Poker hand evaluator

---

## 🔹 Data Classes (Python 3.7+)

- Allow **concise class creation**.
- Automatically generate:
  - `__init__`, `__repr__`, `__eq__`, etc.
- Saves time and reduces boilerplate.
- Gaining popularity, though adoption may take time.
- Chapter shows both traditional and new approaches.

---










































# 🔒 Encapsulation in Python

## 🧑‍💻 Client Code
- **Client code** refers to any code that uses objects of a class.
- In many OOP languages (like Java, C++), data can be made truly **private**, inaccessible outside the class.

- In Python, all data attributes are accessible. You use attribute naming conventions
to indicate that attributes should not be accessed directly from client code.
---

## 🚫 No True Private Data in Python
- Python does **not enforce private access** like other languages.
- Instead, it uses **naming conventions** to indicate intended usage.

---

## 🔤 Leading Underscore Naming Convention

| Prefix        | Meaning                             |
|---------------|--------------------------------------|
| `_attribute`  | Internal use only (non-public)       |
| `attribute`   | Public attribute (OK for client use) |

### ✅ By Convention:
- A leading underscore `_` signals: **"Don't touch this unless you know what you're doing."**
- Python will **not stop** you from accessing `_attribute`, but it's **discouraged**.

---

## 🛠️ Proper Access
- Use **methods** (like getters/setters) or **properties** to **interact with internal data**.
- This protects the class’s internal state and maintains **encapsulation**.

---

## 📌 Key Points

- Encapsulation means **hiding internal data** and exposing only what’s necessary.
- Python relies on **developer discipline** via naming conventions.
- The `_` prefix is a **soft privacy** mechanism—not enforced, but respected by convention.

---

## ⏰ Coming Up: Time Class Example
In the next section, we'll define a `Time` class using these conventions and show how encapsulation works in practice.

- The use of a single leading underscore (e.g., _hour, _minute, _second) in this file is a naming convention in Python to indicate that these attributes are intended to be private and should not be accessed directly by client code.

## 10.4



## 10.5:
- Python programmers often use “private” attributes for data or utility methods that are essential to a class’s inner workings but are not part of the class’s public interface.

- Python objects’ attributes are always accessible. However, Python has a naming convention for “private” attributes.

- ***Rather than _hour, we can name the attribute __hour with two leading underscores. This convention indicates that __hour is “private” and should not be accessible to the class’s clients. To help prevent clients from accessing “private” attributes, Python renames them by preceding the attribute name with _ClassName, as in _Time__hour. This is called name mangling***

- If you try assign to __hour, as in wake_up.__hour = 100 Python raises an AttributeError, indicating that the class does not have an __hour attribute.

- Even with double-underscore (__) naming, we can still access and modify __private_data, because we know that Python renames attributes simply by prefixing their names with '_ClassName'. Demonstrate this for class PrivateData’s data attribute __private_data.


## 10.7:

# 📘 Inheritance in Object-Oriented Programming (OOP)

## 🔹 Basic Concepts

- **Inheritance** allows one class (subclass) to acquire the properties and behaviors (methods) of another class (base class).
- **Base Class**: A general class (e.g., `Loan`).
- **Subclass**: A more specific class that inherits from the base class (e.g., `CarLoan`).

> 🔸 Example: A `CarLoan` is a `Loan`, but not every `Loan` is a `CarLoan`.

---

## 🔹 General vs Specific

- Base classes are **more general**.
- Subclasses are **more specific**.
- A base class can have **many subclasses**.
- A subclass object **is an** object of its base class.

> 🔸 Example: `Vehicle` is a base class. `Car` is a subclass.
> - A `Car` **is a** `Vehicle`.
> - But not all `Vehicles` are `Cars` (they can be `Boats`, `Trucks`, etc.).

---

## 🔹 Inheritance Hierarchies

Inheritance relationships form **tree-like structures**, also called **inheritance hierarchies**.

### 🏫 CommunityMember Hierarchy

- “is a” vs. “has a”
Inheritance produces “is-a” relationships in which an object of a subclass type may also be treated as an object of the base-class type. You’ve also seen “has-a” (composition) relationships in which a class has references to one or more objects of other classes as members.


## 10.8
# 💼 Inheritance Example: Employee Hierarchy in a Payroll App

## 🔹 Real-World Scenario

In a company's payroll system:
- All employees share common features (like name, ID, etc.).
- Some employees are **commission-based**, earning a percentage of their sales.
- Others are **salaried commission-based**, earning both a base salary and a sales commission.

---

## 🔹 Base Class: CommissionEmployee

Represents general **commission-based employees**.

### Key Traits:
- Paid as a **percentage of their total sales**.
- Contains shared employee details and behavior related to commission earnings.

---

## 🔹 Subclass: SalariedCommissionEmployee

Represents a more specific type of employee:
- Inherits all features from `CommissionEmployee`.
- Additionally receives a **fixed base salary** along with commission.

### Special Behavior:
- Calculates total earnings as **base salary + commission**.
- Overrides the base class’s method to add its own logic.

---

## 🔹 Inheritance Relationship

- `SalariedCommissionEmployee` **is a** `CommissionEmployee`.
- The subclass:
  - **Reuses** the base class’s features.
  - **Extends** the functionality with additional logic.
- This models a real-world "is-a" relationship.

---

## 🔹 Key Learnings

- **Base class** captures general behavior.
- **Subclass** adds more specific behavior.
- Objects of the subclass have:
  - All features of the base class.
  - Their own additional features.
- Inheritance avoids code duplication and enhances code organization.



- *****In Python, you cannot define a setter (@property_name.setter) without first defining the corresponding getter (@property).****


- To inherit from a class, you must first import its definition (line 3). Line 6 class SalariedCommissionEmployee(CommissionEmployee): specifies that class  SalariedCommissionEmployee inherits from CommissionEmployee.

- Each subclass __init__ must explicitly call its base class’s __init__ to initialize the data attributes inherited from the base class. This call should be the first statement in the subclass’s __init__ method.

- The notation super().__init__ uses the built-in function super to locate and call the base class’s __init__ method, passing the five arguments that initialize the inherited data attributes.

- **No, your code will not work as expected because the parent class (CommissionEmployee) uses f_name and l_name as the attribute names for the first and last names, but in the child class (SalariedCommissionEmployee), you are passing first_name and last_name to the parent class constructor. This mismatch will cause an error**

- **The parameter names in the child class must match the parameter names expected by the parent class's __init__ method. Choose consistent naming conventions (f_name/l_name or first_ ame/last_name) across your classes to avoid confusion. If you want to use different names in the child class, you must explicitly map them when calling super().__init__().**

- SalariedCommissionEmployee. The new version obtains the portion of the earnings based on commission alone by calling CommissionEmployee’s earnings method with the expression super().earnings()

- By having SalariedCommissionEmployee’s earnings method invoke CommissionEmployee’s
earnings method to calculate part of a SalariedCommissionEmployee’s earnings,
we avoid duplicating the code and reduce code-maintenance problems.



- **Function isinstance determines whether an object has an “is a” relationship with a specific type. Because SalariedCommissionEmployee inherits from CommissionEmployee, both of the following snippets return True, confirming the “is a” relationship**


# 🧠 Understanding Inheritance and Method Overriding

## 🔹 Key Concept

**Inheritance with method overriding** helps you build new software components based on existing ones, but tailored to your app's needs.

---

## 🔹 Object-Based Programming (OBP)

In the Python world, many powerful libraries already exist. In OBP, your programming style usually involves:

1. Knowing which libraries are available.
2. Finding the right classes.
3. Creating objects from those classes.
4. Calling their methods (sending messages).

This is called **object-based programming** because you're using existing classes and combining them (composition), without changing them.

---

## 🔹 Object-Oriented Programming (OOP)

You move from OBP to **OOP** when you:

- Use **inheritance** to create new classes from existing ones.
- **Override methods** to customize behavior.
- Possibly use **polymorphism** (same method, different behavior depending on object).

Even if you're just composing objects from inherited classes, it still counts as object-oriented programming.

---

## 🔹 Summary

| Term | Description |
|------|-------------|
| **OBP** | Use and combine existing class objects. |
| **OOP** | Extend existing classes using inheritance and override methods to fit your needs. |


# 🦆 Duck Typing and Polymorphism in Python

## 🔹 Traditional OOP Languages

In most object-oriented languages:
- **Polymorphism** requires **inheritance** (an “is-a” relationship).
- Objects must be instances of a subclass to be processed polymorphically.

---
## 10.09 Python's Flexibility: Duck Typing

Python allows **polymorphic behavior** without inheritance through a concept called **duck typing**.

> **"If it looks like a duck and quacks like a duck, it must be a duck."**

### What it means:
- Python doesn't check an object's **type**.
- It only checks whether the object has the **method or attribute** you're trying to use.
- If the method exists and can be called correctly, it works — regardless of the class type.

## 10.10 Operator Overloading
What Is It?
Operator overloading allows custom classes to use Python’s built-in operators (+, *, [], etc.) in intuitive ways.

Everyday Uses:
Operator	Built-in Behaviors
- +	Adds numbers, joins strings/lists, adds to each NumPy array element
- []	Access elements in lists, tuples, strings, dictionaries
- *	Multiplies numbers, repeats sequences, scales NumPy arrays
Behind the Scenes:
Operators map to special methods in a class:

Operator	Special Method
+	__add__(self, other)
*	__mul__(self, other)
[]	__getitem__(self, key)
==	__eq__(self, other)
By overriding these in your class, you define how your object interacts with each operator.

🔹 Why Use Operator Overloading?
Makes custom classes easier to use

Enables intuitive syntax

Increases code readability

Integrates well with Python style

✅ Summary
Concept	Key Idea
Inheritance	Reuse and customize behavior across related classes
OBP	Use existing objects via composition
OOP	Extend existing classes with inheritance and overriding
Duck Typing	Behavior-based object handling without inheritance
Operator Overloading	Define custom operator behavior for your classes




## ⚠️ Operator Overloading Restrictions

Although Python allows operator overloading, there are **important restrictions**:

1. **Operator Precedence**  
   - Cannot be changed through overloading.
   - Use parentheses `()` to control evaluation order.

2. **Operator Associativity**  
   - Left-to-right or right-to-left grouping (associativity) **cannot** be changed.

3. **Arity (Number of Operands)**  
   - You cannot change a binary operator (like `+`) into a unary one (like `-x`), or vice versa.

4. **No New Operators**  
   - You can only overload **existing Python operators**.
   - Cannot invent your own symbols (e.g., `%%+>` is invalid).

5. **Built-in Type Behavior is Fixed**  
   - You **cannot** change how built-in types (e.g., `int`, `str`) behave with operators.
   - Example: You can't make `5 + 2` return `1`.

6. **Custom Classes Only**  
   - Operator overloading applies only to:
     - Custom class objects
     - OR custom class + built-in type (e.g., `Vector + 5`)



- **Python prohibits you from creating new operators, and operator overloading cannot change how an operator works with built-in types.**





## 10.11 📌 Exception Class Hierarchy and Custom Exceptions in Python
🔷 Core Concepts
All exceptions in Python are objects of classes that inherit from the base class BaseException.

These classes are defined in the exceptions module (built-in).

🔹 Primary Subclasses of BaseException:
Class	Description
SystemExit	Terminates program execution without producing a traceback.
KeyboardInterrupt	Triggered by user interrupt (e.g., Ctrl + C).
GeneratorExit	Raised when a generator is closed.
Exception	Base class for most common exception types.
📌 Common Subclasses of Exception:
ZeroDivisionError

NameError

ValueError

TypeError

IndexError

KeyError

RuntimeError

AttributeError

StatisticsError (from statistics module)

🧲 Catching Exceptions
You can catch exceptions by their type, or use a base class to catch multiple types.

Catching Exception catches all its subclasses.

❗ Avoid placing a handler for Exception before more specific handlers—others become unreachable.

🧩 Custom Exceptions
Use existing exceptions where possible.

Define custom exceptions only when:

Existing ones don't describe the situation well.

You want to handle them differently.

Custom exceptions should inherit from Exception.

✅ Self Check
Fill-In: Most exceptions inherit from **Exception** and are defined in module **exceptions**.

True/False: You should generally use a new exception class when raising exceptions.
Answer: ❌ False — Prefer existing exception classes.


## 10.14 to be done:::::



## 10.16 Time Series and Simple Linear Regression


📊 Time Series & Simple Linear Regression in Python
🔷 What Are Time Series?
A time series is a sequence of values (observations) associated with points in time.

🔸 Examples:
Daily stock prices

Hourly temperature readings

Flight path coordinates over time

Annual crop yields

Quarterly company profits

Twitter stream (timestamped tweets)

🔹 Types of Time Series
Type	Description
Univariate	One observation per time point (e.g., avg January temp per year)
Multivariate	Multiple observations per time point (e.g., temp, humidity, pressure)
📌 Common Time Series Tasks
Task	Description
Time Series Analysis	Discover patterns (e.g., seasonality) in historical data
Time Series Forecasting	Use past data to predict future trends
📈 Predicting with Simple Linear Regression
We’ll predict average January high temperatures in NYC using data from 1895 to 2018.

➕ Independent Variable
Year (e.g., 1895, 1896, …)

➕ Dependent Variable
Avg January high temperature in that year

✅ Goal
Fit a regression line to model the relationship between year and temperature.

📉 Example of a Linear Relationship
Fahrenheit to Celsius conversion:

python
Copy
Edit
c = 5 / 9 * (f - 32)
📊 Plotting with pandas and matplotlib
Store data as [(f, c), ...] in a DataFrame

Use .plot(style='.-') for a dotted line graph

Customize labels (e.g., set y-axis to 'Celsius')

🛠 Tools & Libraries
Library	Use
pandas	DataFrame operations
matplotlib	Visualization backend
seaborn	Enhanced visualizations
scikit-learn	(In ML chapter) regression modeling
RNNs (Deep Learning)	(In DL chapter) for complex time series









