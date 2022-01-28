from selenium import webdriver      # import the webdriver application from the Selenium library
import time                         # useful for wait functions -- dependent on connection speed

########## CONSTANTS #########
website_location = webdriver.Chrome()       # set to chrome for selenium acces
website_location.get('https://forms.gle/56ARW1Wugs1KXpXo8')     # enter URL of form to fill out

your_name = 'My Name'

########## Functions #########
def main():
    # Start filling out form here
    email_location = website_location.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email_location.send_keys(your_name)

########## MAIN #########
if __name__ == "__main__":
    main ()