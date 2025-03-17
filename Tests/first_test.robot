*** Settings ***
Library    ../Keywords/Common_Keywords.py
Library    ../Keywords/Home_Common_Keywords.py
Library    AsyncLibrary

#Test Setup    Async Run    Open Application
Test Teardown    Async Run    Tear Down Application

*** Test Cases ***
Check Website Opened Correctly
    [Tags]    test
    ${handle}    Async Run    Open Application
    ${handle2}    Async Run    Check Home Page Opened

Go To Bugs Form
    [Tags]    test
#    Open Application
    ${handle3}    Async Run    Open Application
    ${handle4}    Async Run    Check Home Page Opened
    ${handle5}    Async Run    Click On Bugs form