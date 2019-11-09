from selenium import webdriver

def main():
      driver_path = "C:\\Users\\***************\\chromedriver.exe"
      
      driver = webdriver.Chrome(driver_path)
      driver.get('https://web.whatsapp.com/')

      # Get the Details from the User to Perform task etc
      name = input('ENTER NAME/GROUP TO WHOME MESSAGE IS SENT  :  ')
      message = input('ENTER MESSAGE  :  ')
      count = int(input('HOW MANY TIMES DO YOU WANT TO SENT THIS MESSAGE  :  '))
      input('PRESS ANY KEY AFTER SCANNING THE QR CODE')

      User = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
      User.click()

      Message_Box = driver.find_element_by_class_name("_13mgZ")

      for i in range(count):
            Message_Box.send_keys(message)
            Button = driver.find_element_by_class_name('_3M-N-')  
            Button.click()


if __name__=="__main__":
      main()
