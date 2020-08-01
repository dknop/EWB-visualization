import os
import time
import selenium
from selenium import webdriver

import folium
m = folium.Map(location=[45.5236, -122.6750])
#saves map as html
def map_to_html (m, map_name, file_path =""):
    if file_path != "" and file_path[-1]!= '/':
        file_path = file_path+"/"
    path = file_path+map_name+".html"
    m.save(path)
    return path
def map_to_png(m, map_name, file_path =""):
    if file_path != "" and file_path[-1]!= '/':
        file_path = file_path+"/"
    fn = map_name+".html"
    m.save(fn)
    tmpurl='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=fn)
    delay =5
    
    browser = webdriver.Safari()
    browser.get(tmpurl)
    time.sleep(delay)
    browser.save_screenshot(file_path+map_name+'.png')
    browser.quit()