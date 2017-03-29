*** Settings ***
Library    Selenium2Library
Resource    common_resources.robot

#Library  /home/adyachenko/IdeaProjects/PythonTest/testpage/PageObjects/


*** Test Cases ***
Procedures - Procedures list
    procedures filter  Procedures







#    Set Procedures Filter By  Name  several_script_procedure
#    Table Should be Contain Link  several_script_procedure
#    Set Procedures Filter By  Name  ${EMPTY}
#    Select in Filter Procedure by  Type  Custom
#    Table Should be Contain Link   several_script_procedure
#    Select in Filter Procedure by  Type  All
#    Select in Filter Procedure by  Status  Ready to review
#    Table Should be Contain Link   several_script_procedure
#    Select in Filter Procedure by  Status  All
#    Select in Filter Procedure by  Content type  Script
#    Table Should be Contain Link   several_script_procedure
#    Set Procedures Filter By  Created by  ${VALID_username}
#    Table Should be Contain Link   several_script_procedure
#    Set Procedures Filter By  Created by  ${EMPTY}
#    Click Link In Table  several_script_procedure
#    Click Button With Text  Edit
#    Set Procedure name As new_procedure_name
#    Click Button With Text  Save
#    Should Displayed Message  The windows procedure new_procedure_name was updated
#    Navigate Menu to  Configuration Templates  Procedures
#    Table Should be Contain Link  new_procedure_name
#
#
