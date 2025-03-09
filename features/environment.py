# environment.py
from pages import Pages
from utils.driver_manager import get_driver

def before_all(context):
    try:
        # 初始化 Appium Driver
        context.driver = get_driver('dev', 'android')  
        # 初始化顶级 Page 对象（入口）
        context.app = Pages(context.driver)
    except Exception as e:
        print(f"初始化失败: {str(e)}")
        raise

def after_all(context):
    context.driver.quit()