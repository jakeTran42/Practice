from selenium import webdriver

browser = webdriver.Firefox() # Opening Browser

browser.get('https://www.reddit.com/') # Going to the reddit page

elem = browser.find_element_by_css_selector('a.skip-for-now:nth-child(3)') #finding the elemtn/button you want to click on

elem.click() # click on the returned object

elems = browser.find_elements_by_css_selector('p') #Finding a more general element

len(elems) #elems is now a list of returned elements

searchElem = browser.find_element_by_css_selector('#search > input:nth-child(1)') #finding the search bar

searchElem.send_keys('League Of Legend') #Entering input field

searchElem.submit() #submit the input field

leagueSubElem = browser.find_element_by_css_selector('div.search-result-subreddit:nth-child(2) > div:nth-child(2) > a:nth-child(2)')

leagueSubElem.click()

browser.back() #go back a page

browser.forward() #going forward

browser.refresh() #refresh page

findPost = browser.find_element_by_css_selector('#thing_t3_89vc8m > div:nth-child(5) > div:nth-child(1) > p:nth-child(1) > a:nth-child(1)')

findPost.click()

postBody = browser.find_element_by_css_selector('#form-t3_89vc8mcx3 > div:nth-child(2) > div:nth-child(1) > p:nth-child(1)')

postBody.text #Getting the text of the specific post
