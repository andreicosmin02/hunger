from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import random
import time

browser = webdriver.Chrome()
url = 'https://www.instagram.com/'
browser.get(url)
time.sleep(3)
browser.implicitly_wait(10)

# accept cookies
browser.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]").click()
browser.implicitly_wait(10)
time.sleep(3)


# log in
username = ""
password = ""
browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
browser.implicitly_wait(10)

# some pop up
browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
browser.implicitly_wait(2)

# redirect to dms
browser.get('https://www.instagram.com/direct/t/119404979450910/')
browser.implicitly_wait(10)

# drag and drop the picture
JS_DROP_FILE = """
    var target = arguments[0],
        offsetX = arguments[1],
        offsetY = arguments[2],
        document = target.ownerDocument || document,
        window = document.defaultView || window;

    var input = document.createElement('INPUT');
    input.type = 'file';
    input.onchange = function () {
      var rect = target.getBoundingClientRect(),
          x = rect.left + (offsetX || (rect.width >> 1)),
          y = rect.top + (offsetY || (rect.height >> 1)),
          dataTransfer = { files: this.files };

      ['dragenter', 'dragover', 'drop'].forEach(function (name) {
        var evt = document.createEvent('MouseEvent');
        evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
        evt.dataTransfer = dataTransfer;
        target.dispatchEvent(evt);
      });

      setTimeout(function () { document.body.removeChild(input); }, 25);
    };
    document.body.appendChild(input);
    return input;
"""
message_input = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div')



images_path = 'farfurie_images/'
images = os.listdir(images_path)
for _ in range(20):
    file_input = browser.execute_script(JS_DROP_FILE, message_input, 0, 0)
    file_input.send_keys(os.getcwd() + '/' + images_path + images[random.randint(0, len(images))])
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[3]').click()

    time.sleep(1)
    
