from behave import *
from selenium import webdriver
import chromedriver_binary

@given('A web browser')
def web_browser(context):
    context.driver = webdriver.Chrome()

@when('I navigate to the home page')
def nav_home(context):
    context.driver.get('http://localhost:5000')

@then('Hello world is displayed')
def check_hello_world(context):
    assert context.driver.find_element_by_id("helloworld").text == 'Hello world !'
