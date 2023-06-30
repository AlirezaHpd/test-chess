from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  # Add this import statement
import time
import pyautogui


options = Options()
# Add any desired options specific to Firefox here, if needed

# Install and set up GeckoDriver
service = Service(executable_path=GeckoDriverManager().install())

# Create a Firefox driver instance
driver = webdriver.Firefox(service=service, options=options)

# Now you can use the Firefox driver for your automation tasks

driver.get("https://www.chess.com/")
driver.maximize_window()

# Wait for the page to load and find the login button
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Log In"))
)
# Click the login button
login_button.click()

# Wait for the login modal to appear and find the username and password fields
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
)

# Enter your username and password
username_field.send_keys("mahyar2024")
password_field.send_keys("09118760280mM")

# Submit the login form
password_field.send_keys(Keys.RETURN)
time.sleep(20)
# Wait for the "Play a Friend" link to appear and click it
play_friend_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Play a Friend"))
)
play_friend_link.click()
time.sleep(10)
# Wait for the username link to appear and click it
username_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'user-username-component.user-username-blue.user-username-link.user-tagline-username'))
)

username_link.click()

time.sleep(10)
username_link_2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'color-selector-option.color-selector-white'))
)
username_link_2.click()

time.sleep(1)
username_link_3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'ui_v5-button-component.ui_v5-button-primary.ui_v5-button-large.ui_v5-button-full'))
)
username_link_3.click()
time.sleep(20)

#pawn h2 to h4
pyautogui.moveTo(950, 788)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(946, 630)
time.sleep(2)
pyautogui.click()
time.sleep(6)
#pawn g2 to g4
pyautogui.moveTo(855, 804)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(855, 615)
time.sleep(2)
pyautogui.click()
time.sleep(6)
#pawn f2 to f4
pyautogui.moveTo(757, 801)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(760, 615)
time.sleep(2)
pyautogui.click()
time.sleep(6)
#pawn e2 to e4
pyautogui.moveTo(669, 813)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(682, 618)
time.sleep(2)
pyautogui.click()
time.sleep(6)
#pawn d2 to d4
pyautogui.moveTo(577, 803)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(592, 618)
time.sleep(1)
pyautogui.click()
time.sleep(6)
#pawn c2 to c4
pyautogui.moveTo(477, 804)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(486, 615)
time.sleep(2)
pyautogui.click()
time.sleep(6)
#pawn b2 to b4
pyautogui.moveTo(389, 795)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(396, 610)
time.sleep(2)
pyautogui.click()
time.sleep(6)
#pawn a2 to a4
pyautogui.moveTo(302, 805)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(293, 700)
time.sleep(2)
pyautogui.click()
time.sleep(6)

# pawn Beating another pawn h4 to g5
pyautogui.moveTo(949, 618)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(855, 521)
time.sleep(2)
pyautogui.click()
time.sleep(6)

#Rook  h1 to h3
pyautogui.moveTo(950, 906)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(949, 702)
time.sleep(2)
pyautogui.click()
time.sleep(6)


# Horse  g1 to f3
pyautogui.moveTo(857, 897)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(770, 705)
time.sleep(2)
pyautogui.click()
time.sleep(6)

# pawn d4 to e5
pyautogui.moveTo(569, 621)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(669, 523)
time.sleep(2)
pyautogui.click()
time.sleep(6)


# elephant f1 to e2
pyautogui.moveTo(763, 904)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(666, 789)
time.sleep(2)
pyautogui.click()
time.sleep(6)

# king e1 to f1
pyautogui.moveTo(666, 901)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(765, 909)
time.sleep(2)
pyautogui.click()
time.sleep(6)

# Queen d1 to d5
pyautogui.moveTo(572, 901)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.click(569, 523)
time.sleep(2)
pyautogui.click()
time.sleep(6)

# Queen beat queen d5 to d8
#pyautogui.click(569, 515)
#time.sleep(1)
pyautogui.click(575, 230)
time.sleep(2)
pyautogui.click()
time.sleep(6)

# Queen beat queen d8 to e8
#pyautogui.click(575, 230)
#time.sleep(1)
pyautogui.click(670, 255)
time.sleep(2)
pyautogui.click()
time.sleep(6)
# Queen beat elephant e8 to f8
#pyautogui.click(670, 255)
#time.sleep(1)
pyautogui.click(762, 247)
time.sleep(2)
pyautogui.click()
time.sleep(6)
# Queen  f8 to f7
#pyautogui.click(762, 247)
#time.sleep(1)
pyautogui.click(764, 345)
time.sleep(2)
pyautogui.click()
time.sleep(6)





# Close the browser
# driver.quit()

