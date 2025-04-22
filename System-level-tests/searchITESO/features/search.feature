Feature: ITESO Homepage Search

Scenario: User searches for carreras on ITESO website
  Given the user opens the browser and navigates to 'iteso.mx'
  When the user searches for "carreras" on the ITESO homepage
  Then the user should see results related to "carreras"
