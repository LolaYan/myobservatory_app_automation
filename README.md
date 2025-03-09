# MyObservatory Automation Testing Framework

A cross-platform automation testing framework for Android and iOS apps using ​**Appium**, ​**pytest**, ​**behave**, ​**Page Object Model**, and ​**Allure**. Designed for maintainability, scalability, and ease of use.

---

## 🚀 Features
- ​**Cross-Platform Support**: Single codebase for Android and iOS.
- ​**BDD Testing**: Write tests in Gherkin syntax with `behave`.
- ​**Page Object Model**: Separate UI interactions from test logic.
- ​**Allure Reporting**: Generate detailed HTML/JSON test reports.
- ​**Dynamic Device Management**: Automatically detect Android/iOS devices.
- ​**Multi-Environment Configs**: Manage dev/staging/prod environments via YAML.

---

## 🛠️ Prerequisites
- ​**Python 3.8+**
- ​**Node.js 14+** (for Appium)
- ​**Appium Server 2.0+**
- ​**Java JDK 8+** (for Android)
- ​**Android SDK** (for Android testing)
- ​**Xcode 13+** (for iOS testing)
- ​**Homebrew** (macOS only, for dependency management)

---

## 📥 Installation
1. ​**Clone the repository**:
   ```bash
   git clone https://github.com/LolaYan/myobservatory_app_automation
   cd myobservatory_app_automation

2. ​**​Install dependencies**:
   ```bash
   pip install -r requirements.txt

3. ​**Configure environments**:
- Update config/dev.yaml, config/staging.yaml, and config/prod.yaml with your app/device details.

4. ​**Start Appium Server**:
- When we test locally, we need start the appium server. If we need to trigger the test in Cloud Platform like browserstack, no need to do this
   ```bash
   appium

## 🧪 Installation
- ​**Run with pytest**:
   ```bash
   # Android
   pytest tests/ -m aos --env=dev
   
   # iOS
   pytest tests/ -m ios --env=dev

   # run test with debug log
   pytest tests/  -s -v 

   # run test and save allure results
   pytest tests/  -s -v --alluredir=./allure-results

- ​**Run BDD Tests with behave**:
   ```bash
   behave features/verify_nine-days_forecast_page.feature -D platform=aos

- ​**Run test in browserstack**:
   Save browserstack credentials in .env file under root folder
   BROWSERSTACK_USERNAME=your_username
   BROWSERSTACK_ACCESS_KEY=your_access_key
   Then run command below:
   ```bash
   # Android
   pytest tests/ -m aos --env=browserstack
  
- ​**Generate Allure Report**:
   ```bash
   # Collect test data
   pytest --alluredir=./allure-results
   
   # Generate HTML report
   allure generate ./allure-results -o ./allure-report --clean
   allure open ./allure-report

## 📂 Project Directory Structure

- myobservatory_app_automation/
   - allure-results/       # Allure raw test data
   - assets/               # Static resources (images/fonts)
   - config/               # Environment configurations
      * dev.yaml          # Development config
      * staging.yaml      # Staging config
      * prod.yaml         # Production config
   - features/             # BDD feature files
      * steps/            # Step definitions
         * test_nine_days_forecast_steps.py
      * environment.py    # Behave hooks
      * verify_nine-days_forecast_page.feature
   - pages/                # Page Object classes
   - screenshots/          # Test failure screenshots
   - scripts/              # Utility scripts
      * get_android_device_info.sh    # Fetch Android device info
      * test_appium_setup.py          # Validate Appium setup
   - task2/                # Task-specific modules
      * get_forecast_weather.py
   - tests/                # pytest test cases
      * test.py
   - utils/                # Helper classes
      * driver_manager.py  # Appium driver initialization
   - .gitignore            # Git ignore rules
   - conftest.py           # pytest fixtures
   - pytest.ini            # pytest configurations
   - README.md             # Project documentation
   - requirements.txt      # Python dependencies

## 🔧 Troubleshooting
- ​**Device Not Detected**:
   - Run scripts/get_android_device_info.sh (Android) or check Xcode device logs (iOS).
- ​**​Appium Connection Errors**:
   - Verify Appium server is running: appium --log-level=error
   - Check port conflicts (4723 by default).
- ​**​Allure Report Empty**:
   - Delete old data: rm -rf allure-results/
   - Ensure pytest runs with --alluredir=./allure-results.
- ​**Other checkpoints**:
   - Adjust Appium/WebDriverAgent versions according to your OS and device setup.
   - For iOS real-device testing, ensure WebDriverAgent is properly signed in Xcode.


## 📂 Run Tasks
- ​**Task-1:**:
   ```bash
   # pytest run
   pytest tests/test.py -s -v --alluredir=./allure-result

   # Behave run
   behave features/verify_nine-days_forecast_page.feature -D platform=aos

- ​**Task-2:**:
   ```bash
   python task2/get_forecast_weather.py
- **Response Demo**:
   ```bash
   Current date：2025-03-09
   Target date：20250311
   Target date humidity range：67.9-87.1%

