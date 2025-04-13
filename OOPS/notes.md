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











