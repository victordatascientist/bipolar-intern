from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime, time, os

td = datetime.date.today()

# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-minimized') #maximized
wd = webdriver.Chrome(r'C:\Users\admin\chromedriver.exe',options=CO)

# Format for printing output
print ("Connecting to Authentic News source, Please wait .....\n")
news_site = "https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"

print ("Date:",td.strftime("%b-%d-%Y"))
print ("--------------------------------------------------------------------------------------------")
print ("       >>>>>>>>>>>>>>>>>>> INDIA's TOP 5 NEWS HEADLINES on CORONAVIRUS <<<<<<<<<<<<<<       ")
print ("--------------------------------------------------------------------------------------------\n")

wd.get(news_site)
wd.implicitly_wait(wait_imp)
cov_news = wd.find_elements_by_tag_name('h3')

# To get top 5 news headlines
n_ind = 0
for news in cov_news:
    print ('>> '+ news.text, end='\n')
    n_ind += 1
    if n_ind > 4:  # Increase the number to get more top newsheadlines --> Replace 4 by any other value
        break
print ('\n')

# For Coronavirus stats
site2 = "https://www.worldometers.info/coronavirus/country/india/"
site3 = "https://www.mohfw.gov.in/"
site4 = "https://www.grainmart.in/news/coronavirus-covd-19-live-cases-tracker-john-hopkins/" #Johns Hopkins stats

print ("--------------------------------------------------------------------------------------------")
print ("                Getting CORONAVIRUS stats from various sources (India)                      ")
print ("--------------------------------------------------------------------------------------------\n")
print ("Source Name  --   Total Case  --  Recovered  --  Death")
print ("___________       __________      _________      ______      Please wait .. while collecting data")

wd.get(site2)
wd.implicitly_wait(wait_imp)
c2 = wd.find_elements_by_class_name("maincounter-number")
total_2 = c2[0].text
Death_2 = c2[1].text
Recovered_2 = c2[2].text
print ("Worldometers       {}           {}           {} ".format(total_2,Recovered_2,Death_2))

wd.get(site3)
wd.implicitly_wait(wait_imp)
total_3 = wd.find_element_by_xpath("/html/body/div/div/section[1]/div/div/div/div/ul/li[1]/strong")
Death_3 = wd.find_element_by_xpath("/html/body/div/div/section[1]/div/div/div/div/ul/li[3]/strong")
Recovered_3 = wd.find_element_by_xpath("/html/body/div/div/section[1]/div/div/div/div/ul/li[2]/strong")
print ("Government         {}            {}           {} ".format(total_3.text,Recovered_3.text,Death_3.text))

wd.get(site4)
wd.implicitly_wait(wait_imp)
total_4 = wd.find_element_by_xpath("/html/body/div/div[1]/div/div/div/main/div/div/figure/table/tbody/tr[1]/td[2]/strong")
Death_4 = wd.find_element_by_xpath("/html/body/div/div[1]/div/div/div/main/div/div/figure/table/tbody/tr[1]/td[4]/strong")
Recovered_4 = wd.find_element_by_xpath("/html/body/div/div[1]/div/div/div/main/div/div/figure/table/tbody/tr[1]/td[5]/strong")
print ("Johns-Hopkins      {}            {}          {} \n".format(total_4.text,Recovered_4.text,Death_4.text))

wd.get("https://www.who.int/emergencies/diseases/novel-coronavirus-2019")
wd.implicitly_wait(wait_imp)
w_total = wd.find_element_by_id("confirmedCases")
w_death = wd.find_element_by_id("confirmedDeaths")
total_c = wd.find_element_by_id("involvedCountries")
print("WHO-Global         {}      No-data        {}         \n" .format(w_total.text ,w_death.text))

print ("Total Countries affected: ", total_c.text)






output

"""Connecting to Authentic News source, Please wait .....

Date: Apr-28-2020
--------------------------------------------------------------------------------------------
       >>>>>>>>>>>>>>>>>>> INDIA's TOP 5 NEWS HEADLINES on CORONAVIRUS <<<<<<<<<<<<<<       
--------------------------------------------------------------------------------------------

>> Coronavirus live updates: Karnataka govt relaxes lockdown norms in 14 districts
>> India coronavirus: The 'mystery' of low Covid-19 death rates
>> Coronavirus update: Covid-19 cases in India near 29,500. State-wise status
>> Coronavirus India lockdown Day 35 updates | Karnataka extends relaxation to 14 districts
>> Arrests in relation to Delhi riots be made in accordance with SC guidelines, says HC


--------------------------------------------------------------------------------------------
                Getting CORONAVIRUS stats from various sources (India)                      
--------------------------------------------------------------------------------------------

Source Name  --   Total Case  --  Recovered  --  Death
___________       __________      _________      ______      Please wait .. while collecting data
Worldometers       29,451           7,137           939 
Government         21632            6868           934 
Johns-Hopkins      29692            7180          945 

WHO-Global               No-data                 

Total Countries affected:  

"""
