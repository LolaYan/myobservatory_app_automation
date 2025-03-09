Feature: Nine Forecast Weather Test
  @platform.android
  Scenario: Weather Forecast Testing in Android
    Given User open the app
    Then User should see disclaimer page
    When User clicks AGREE button in the Disclaimer page
    Then User should see the Privacy Policy Statements page
    When User clicks AGREE button in the Privacy Policy Statements page
    Then User should see the device notification Access Request page
    When User click Allow option in the device notification Access Request page
    Then User should see the Background Location Access Request page
    When User click OK button in Background Location Access Request page
    Then User should see the new Location Access page
    When User clicks While using the app button in Device Location Access page
    Then User should see the All Location Permission config page
    When User clicks Allow all the time option in All Location Permission config page
    When User clicks the Back button in All Location Permission config page
    Then User should see the Whats new page
    When User clicks the next button in whats new page
    Then User is redirected to the 2nd sub page of whats new page
    When User clicks the close button in the 2nd sub page of whats new page
    Then User should see the Home page
    When User clicks the header ham menu bar
    Then User should see dropdown options of header ham menu
    When User open the Forecast and Warning service and clicks the 9-Day Forecast option
    Then User should see the "9-Day Forecast" page

  @platform.ios
  Scenario: Weather Forecast Testing in IOS
    Given User open the app
    Then User should see ios_nextwork_access page
    When User set up ios_nextwork_access page
    Then User should see ios_language_setup page
    When User set up ios_language_setup page
    Then User should see ios_location_access page
    When User set up ios_language_setup page
    Then User should see ios_notification_access page
    When User set up ios_notification_access page
    Then User should see ios_loc_based_notification page
    When User setup ios_loc_based_notification page
    Then User should see ios_color_theme page
    When User set up ios_color_theme page
    Then User should see the Whats new page
    When User clicks the next button in whats new page
    Then User is redirected to the 2nd sub page of whats new page
    When User clicks the close button in the 2nd sub page of whats new page
    Then User should see the Home page
    When User clicks the header ham menu bar
    Then User should see dropdown options of header ham menu
    When User open the Forecast and Warning service and clicks the 9-Day Forecast option
    Then User should see the "9-Day Forecast" page