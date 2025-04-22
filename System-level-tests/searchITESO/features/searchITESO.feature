Feature: ITESO Homepage Search
  As a user
  I want to search for 'carreras' on the ITESO homepage
  So that I can see the academic programs that ITESO offers

Scenario: searching for 'carreras' on ITESO website
  Given I am on the ITESO homepage
  When I search for 'carreras'
  Then I should see results related to ITESO academic programs
