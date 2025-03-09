import pytest
from utils.driver_manager import get_driver
from pages import Pages

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", 
                     help="Environment: dev/prod/browserstack")

@pytest.fixture(scope="session")
def env(request):
    """全局环境配置"""
    return request.config.getoption("--env")

@pytest.fixture(scope="function")
def platform(request):
    """动态解析平台标记"""
    # 优先从命令行参数获取（兼容性扩展）
    cli_platform = request.config.getoption("--platform", None)
    if cli_platform:
        return cli_platform
    
    # 从 pytest.mark 解析
    platform_markers = [
        marker.name for marker in request.node.iter_markers() 
        if marker.name in ("android", "ios")
    ]
    if platform_markers:
        return platform_markers[0]
    
    pytest.skip("未指定测试平台 (android/ios)")

@pytest.fixture(scope="function")
def driver(env, platform):
    """驱动初始化（每个测试函数独立实例）"""
    driver = get_driver(env, platform)
    yield driver
    driver.quit()

@pytest.fixture
def pages(driver):
    """按需初始化的页面对象"""
    return Pages(driver)