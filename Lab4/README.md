# EE355 - Spring 2022 - Lab4

Name: Micah See
USC ID: 5867-4692-52

-------------------------------------------------------------------------

Please complete the Person.cpp and Date.cpp. 
You can use test_person.cpp and test_date.cpp to test your code. 

You can clone the repo with this command:
```sh
git clone <git-addr>
```


The three golden commands to make sure your code is submitted:
```sh
git add .
git commit -m "write down a comment about your version"
git push
```

-------------------------------------------------------------------------

Questions:

1. How is class composition used in this lab?

Class composition is being used in two instances in this lab.

First, the "Date" class is used for the "birthdate" data member in the Person class.

Second, the "Worker" class is used for the worker object in the Employer class.

2. Did you use the level of inheritance and friend class in this lab? If so, explain how these concepts helped to achieve the required functionalities.

I used level of inheritance to control outside access to the data members and member functions of Employer class. The Employer class inherits from the Person class using the "protected" access specifier. This prevents the information stored in the Employer class from being accessible to the public, per the specification.

I used the friend class to allow Employer class the private data members of the Worker class, specifically the salary variable. This allows the Employer class to set the salary of the Worker object stored in it.