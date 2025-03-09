from appium.options.android import UiAutomator2Options
from appium import webdriver  
import yaml  
import os  

def get_driver(env="dev", platform="android"):  
    if not env or platform:
        env="dev"
        platform="android"

    config_path = os.path.join("config", f"{env}.yaml")  
    with open(config_path) as f:  
        config = yaml.safe_load(f)  

    if env == "browserstack":  
        caps = config["platform"]
        if platform == "android":
            caps["app"] = config["app_aos"]
        elif platform == "ios":    
            caps["app"] = config["app_ios"]
        caps["browserstack.user"] = os.getenv("BROWSERSTACK_USERNAME")  
        caps["browserstack.key"] = os.getenv("BROWSERSTACK_ACCESS_KEY")  
        return webdriver.Remote(config["browserstack"]["server"], caps)  

    elif platform == "android":  
        caps = config["android"]  
        return webdriver.Remote("http://localhost:4723", options=UiAutomator2Options().load_capabilities(caps))  

    elif platform == "ios":    
        caps = config["ios"]  
        return webdriver.Remote("http://localhost:4723", options=UiAutomator2Options().load_capabilities(caps)) 