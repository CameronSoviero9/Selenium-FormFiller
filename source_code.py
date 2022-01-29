from selenium import webdriver      # Import the webdriver application from the Selenium library
import time                         # Useful for wait functions -- dependent on connection speed

########## CONSTANTS #########
website_location = webdriver.Chrome()       # Set to chrome for selenium acces
website_location.get('https://forms.gle/56ARW1Wugs1KXpXo8')     # Enter URL of form to fill out

your_name = 'My Name'
your_birthday = '01/01/2000'
other_language = "PHP"

########## FUNCTIONS #########
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

    # Go to the second page
    nextpage_location = website_location.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    nextpage_location.click()

    # Add in a wait so the next page has time to load
    time.sleep(2)       # 2 second wait

    # Select the programming languages
    language1_location = website_location.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')
    language1_location.click()
    language2_location = website_location.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span')
    language2_location.click()
    language3_location = website_location.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span')
    language3_location.click()

    # Select option for "Other"
    language4_location = website_location.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[6]/div/label/div/div[2]/div/span')
    language4_location.click()
    # Enter other programming language into short answer box
    languageOther_location = website_location.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[6]/div/div/div/div/div[1]/input')
    languageOther_location.send_keys(your_name)

    # Click the experience drop down menu box
    experience_location = website_location.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    experience_location.click()

    # IMPORTANT: need to add a wait to give the page time to load drop down options
    time.sleep(2)     # 2 second wait time

    # Select the experience level
    experienceLevel_location = website_location.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[5]')
    experienceLevel_location.click()

    time.sleep(2)     # 2 second wait time

    # Click Submit
    submit_location = website_location.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')
    submit_location.click()

    # Check that the submit button worked as expected
    get_confirmation = website_location.find_element_by_css_selector(".freebirdFormviewerViewResponseConfirmationMessage")
    if get_confirmation.text == "Your response has been recorded.":
        print("Test script was successful")
    else:
        print("Test script did not complete form")

########## MAIN #########
if __name__ == "__main__":
    main ()
