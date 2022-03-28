#ifndef PERSON_H
#define PERSON_H

#include "Date.h"
#include "fstream"
class Person {
    // Its always OK to discuss your private issues with good friends, at least in C++! 

private:
	string f_name;
	string l_name;
	Date *birthdate;

public: 
    Person();
    Person(string filename);
    Person(string f_name, string l_name, string bdate);
	void print_person();
	void set_person();
	void set_person(string filename);
    bool operator==(const Person& rhs);
    bool operator!=(const Person& rhs);
};

class Worker : public Person {
private:
    std::string id;  // fits into int! no worries!
    float salary;  // fits into int! no worries!
public:
    Worker();
    void set_worker();
    void set_id(string id);
    float get_salary();
    void print_person();

    friend class Employer;
};

//TODO: create a class Employer that meets the following requirements:
// - the class uses Person as base class
// - Employer Class information should not be accessible outside the class --- see explanation on Blackboard
// - Employer class can set and increase salary of their workers
class Employer : protected Person {
    private:
        Worker *worker;
    public:
        // Employer();
        void onboard_employee();
        void set_employee_salary(float salary);
        void print_employee();
};

#endif
