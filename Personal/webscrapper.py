from time import sleep
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import os

driver = webdriver.Chrome()

url = 'https://www.skyscanner.com.tr/transport/flights/ista/dps/241019/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false'
sleep(10)
driver.get(url)



