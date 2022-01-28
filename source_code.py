from selenium import webdriver      # Import the webdriver application from the Selenium library
import time                         # Useful for wait functions -- dependent on connection speed

########## CONSTANTS #########
website_location = webdriver.Chrome()       # Set to chrome for selenium acces
website_location.get('https://forms.gle/56ARW1Wugs1KXpXo8')     # Enter URL of form to fill out

your_name = 'My Name'
your_birthday = '01/01/2000'

########## Functions #########
def main():
    # Start filling out form here
    # Enter your name into the short answer box
    name_location = website_location.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_location.send_keys(your_name)

    # Enter your birthday into the data option box
    birthday_location = website_location.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    birthday_location.send_keys(your_birthday)

    # Select the bubble to indicate your gender
    gender_location = website_location.find_element_by_xpath('//*[@id="i14"]/div[3]/div')
    gender_location.click()

########## MAIN #########
if __name__ == "__main__":
    main ()