# Module requirements

Maintainability: Scripts are affected by changes on all levels of system abstraction and therefore needs to be maintained faster than the SUT.
Reusability: Setting the SUT into a specific state often requires the same or similar scenarios to be performed. Reusing code is therefore efficient to mitigate development cost.
Modularity: Reuse by copying and pasting code leads to multiple maintenance and therefore code should be broken out into modules that are then reused in other scripts.
Readability: This quality relates to complexity of the scripts, where complexit should be mitigated as much as possible. For instance by avoiding branches, loops, etc.
Synchronization: One of the main challenges with automated test scripts are their asynchronous execution against the SUT. Solving this with dynamic wait statements is necessary but also difficult. Avoid static waits since they make your scripts slow and less tolerant of delays.


# Deliverables:

The assignment should be submitted as a single library (.zip) that includes the following:
10 test scripts (i.e., test scenarios) in any programming language that uses Selenium WebDriver (using an xUnit framework is optional)
A link to the publicly available web application (i.e., so that anyone can run the tests) that was used when creating the tests