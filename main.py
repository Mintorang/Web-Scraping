try:

    # This script uses Selenium to web scrape Ebay for a user-specified item

    # Imports used for the file
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    # Sets the browser that will be used, which in this case is Chrome
    driver = webdriver.Chrome()

    # Declares the lists and dictionary that needs to be used for the script to function
    ebay_links = []
    item_content = {}
    ebay_prices  = []

    # Get User_input for the item the user is searching for
    user_input = input("What do you want to search for?  ")
    # Open ebay.co.uk and enter user_input in the search box
    driver.get("https://www.ebay.co.uk")
    ebay_search_box = driver.find_element(By.NAME, "_nkw")
    ebay_search_box.click()
    ebay_search_box.send_keys(f"{user_input}")
    ebay_search_box.send_keys(Keys.ENTER)


    # Stores all the links on the web page, which are still in HTML format, in a variable called links (this variable is a list)
    links = driver.find_elements(By.CLASS_NAME, "s-item__link")


    # Loops the links var and takes out the href from the link tag in html. Append the links to another list called: ebay_links
    for link in links:
        new_link = link.get_attribute("href")
        ebay_links.append(new_link)


    # Loops thorough every link in ebay_links, to get the price and description. Updates item_content dictionary with all the necessary details. 
    for link in ebay_links:
        driver.get(link)
        price = driver.find_element(By.CLASS_NAME,"x-price-primary")
        description = driver.find_element(By.CLASS_NAME, "x-item-title__mainTitle")
        ebay_prices.append(float(price.text.replace("£", "").replace("each", "")))
        ebay_prices.sort()
        item_content.update({f"{price.text}": [f"{link}", f"{description.text}"]})
        for new_s, new_val in item_content.items():

            # print first key
            print(new_s, new_val)

            # after getting first key break loop
            break


    # Prints the dictionary full of details about the item
    print(item_content)

    # Quits the chromedriver and concludes the program
    driver.quit()

except:
    print("There was an error with the program. Please search for a different item")
