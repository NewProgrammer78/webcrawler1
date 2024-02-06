from selenium import webdriver

def collect_images_from_page(url):
    # Initialize Chrome driver
    driver = webdriver.Chrome()

    try:
        # Navigate to the specified URL
        driver.get(url)

        # Find all image elements on the page
        image_elements = driver.find_elements_by_tag_name('img')

        # Collect image sources
        image_sources = []
        for img in image_elements:
            src = img.get_attribute('src')
            if src:
                image_sources.append(src)

        # Print the collected image sources
        print("Collected image sources:")
        for src in image_sources:
            print(src)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the browser
        driver.quit()

# Example usage
if __name__ == "__main__":
    target_url = "https://example.com"  # Replace with your desired URL
    collect_images_from_page(target_url)