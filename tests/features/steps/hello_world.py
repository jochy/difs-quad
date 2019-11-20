import os
import stat

from behave import *
from phantomjs_bin import executable_path
from selenium import webdriver


@given('A web browser')
def web_browser(context):
    os.chmod(executable_path, stat.S_IXUSR)
    context.driver = webdriver.PhantomJS(executable_path=executable_path)


@when('I navigate to the home page')
def nav_home(context):
    context.driver.get('http://localhost:5000')
    raise RuntimeError('')


@then('Hello world is displayed')
def check_hello_world(context):
    assert context.driver.find_element_by_id("helloworld").text == 'Hello world !'
