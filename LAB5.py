from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

# Specify the path to chromedriver
chrome_driver_path = 'DriverC\chromedriver.exe'

# Set up the Chrome service
service = Service(executable_path=chrome_driver_path)

# Initialize the WebDriver with the service
driver = webdriver.Chrome(service=service)

# Open the target webpage
driver.get("https://www.calculator.net/percent-calculator.html")

# Example Test: Calculate 10% of 50
def test_percentage_calculation(a,b,c):
    try:
        # Find input fields and buttons
        value_field = driver.find_element(By.ID, "cpar1")
        percentage_field = driver.find_element(By.ID, "cpar2")
        calculate_button = driver.find_element(By.XPATH, "//input[@value='Calculate']")

        # Input values
        value_field.clear()
        value_field.send_keys(a)
        percentage_field.clear()
        percentage_field.send_keys(b)

        # Click the calculate button
        calculate_button.click()
        valc="Result: "+c
        #Print values
        print("Value 1: "+a+" Value 2: "+b+" Expected result: "+c)

        # Check the result
        result = driver.find_element(By.CLASS_NAME, "h2result").text
        assert valc in result
        print("Test Passed: Percentage Calculation is correct.")
    except AssertionError:
        print("Test Failed: Percentage Calculation is incorrect.")

# Run the test
test_percentage_calculation("50","10","5")
test_percentage_calculation("50","15","10")
test_percentage_calculation("50","-10","5")

# Close the browser after a short wait
time.sleep(5)
driver.quit()
