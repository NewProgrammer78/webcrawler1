from selenium import webdriver
from selenium.webdriver.chrome.options import Options

co = webdriver.ChromeOptions()
co.add_argument("--incognito")
co.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=co)
start_url = "https://www.youtube.com/watch?v=mJ-qvsxPHpY"
links = set()

def crawl(start_link):
    driver.get(start_link)
    #driver.page_source?
    elements = find_elements(By.TAG_NAME, 'div')
    urls_to_visit = set()
    for el in elements:
        urls_to_visit.add(el.get_attribute('href'))
    for el in urls_to_visit:
        if start_url in el and el not in links:
            links.add(el)
            crawl(el)

# Call the function with the starting URL
crawl(start_url)

# Print the collected links
print("Collected links:")
for link in links:
    print(link)

# Close the Chrome driver
driver.close()

# at the end of script wait for user to supply input, delaying script exit
#raw_input("Press Enter to exit")