
# Qaundoo 
## Quality Assurance Engineer Task

The QA tech task assigned by Qaundoo is based on two parts.
                                                                                        
First task is based on UI Automation Testing and second task is based on API Automation Testing




# Tech Stack

**Programming Language:** Python

**Framework:** Selenium, Pytest, Appium

# Reason Behind Choosen Framework and Pattern(s)
The reason behind choosing pytest as automation testing framework is simply because it allows
to write consise and readable test cases, and offers scalability to support complex functional testing.

It is not only easy to use but also comes along the feature of parameterization of tests which helps
reduce code redundancy. Pytest also allows to run tests parallely reducing time taken for test cases execution.

Pytest is simple to understand and implement, in addition to this pytest documentation addresses all automation testing concerns.

# How to make the framework work and how to execute the test(s)

## Execute Task 1 - UI Automation Testing - Web

Requirements

1. Install all dependencies by using requirements.txt file, execute command below:
```
pip install -r requirements.txt
```
2. Navigate to the folder, execute command below:
```
cd ".\Task 1 - UI Automation Testing - Web"
```
3. To run the test script, execute command below:
```
pytest test_script.py
```

## Execute Task 1 - UI Automation Testing - Mobile

Requirements
1. Install Java
2. Download Command line tools from:
```
https://developer.android.com/studio
```

3. Install Appium Server GUI from:
```
https://github.com/appium/appium-desktop
```
Executing Tests
1. Start the Appium Server GUI server
2. Enable developer tools on device and connect to computer (if testing on real device)
3. Navigate to the folder, execute command below:
```
cd ".\Task 1 - UI Automation Testing - Mobile"
```
4. To run the test script, execute command below:
```
pytest test_script.py
```
## Execute Task 2 - API Testing

Requirements

1. Install all dependencies by using requirements.txt file, execute command below:
```
pip install -r requirements.txt
```
2. Navigate to the folder, execute command below:
```
cd ".\Task 2 - API Testing"
```
3. To run the test script, execute command below:
```
pytest test_api_methods.py
```

# Next Additions in test scripts
For testing login scenario, we can implement many other test cases, for example error messages displayed.
For API Testing, in addition to assertion of response code, we can also assert the response json received.

# Next possible steps for improvements

As seen in test suite for mobile automation testing, we can use pytest parameterization feature. With help of parameterization for test cases, we can avoid code redundancy in automation scripts.
As both the approaches i.e traditional and paramterize, can be seen in the test scripts, by implementing hybrid frame work, combining unittest and pytest we can seperate test cases based on scenarios in seperate files and execute the test suite. 

# Additional Note
Selection of the framework for the automation script depends on the Application Under Test. For smaller applications, we may keep all test cases in one file but for larger application our test scripts should be scalable.



    
