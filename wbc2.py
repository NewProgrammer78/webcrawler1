from selenium import webdriver

# Initialize the Chrome web driver, this method is outdated use Service()
driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe')

# Open a website
driver.get('https://www.youtube.com/watch?v=mJ-qvsxPHpY')

# Get the title of the webpage
page_title = driver.title
print(f"Page Title: {page_title}")

# Close the browser
driver.quit()