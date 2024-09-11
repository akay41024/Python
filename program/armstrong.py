def is_armstrong(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        return True
    else:
        return False



print("Armstrong Number from 1 to 1000")

for i in range(1,10):
    print(i)

# All single digit number is a armstrong number so we can start from 10


for i in range(10,1001):
    if is_armstrong(i):
        print(i)


# from selenium import webdriver
# import time
# import csv

# def scrape_gmb_listings(keyword, location):
#     driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed
#     driver.get(f'https://www.google.com/search?q={keyword}+{location}&hl=en')

#     time.sleep(5)  # Let the page load

#     gmb_listings = driver.find_elements_by_class_name('VkpGBb')

#     data = []

#     for listing in gmb_listings:
#         name = listing.find_element_by_class_name('dbg0pd').text
#         address = listing.find_element_by_class_name('rllt__details').text
#         phone = listing.find_element_by_class_name('rllt__details').text
#         website = listing.find_element_by_partial_link_text('Website').get_attribute('href') if listing.find_elements_by_partial_link_text('Website') else ''

#         data.append({'Name': name, 'Address': address, 'Phone': phone, 'Website': website})

#     driver.quit()

#     return data

# def export_to_csv(data):
#     with open('gmb_listings.csv', 'w', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['Name', 'Address', 'Phone', 'Website']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()
#         for row in data:
#             writer.writerow(row)

# def main():
#     keyword = input('Enter keyword (e.g., "restaurants"): ')
#     location = input('Enter location (e.g., "New York"): ')

#     data = scrape_gmb_listings(keyword, location)
#     export_to_csv(data)
#     print('Data exported to gmb_listings.csv')

# if __name__ == "__main__":
#     main()
