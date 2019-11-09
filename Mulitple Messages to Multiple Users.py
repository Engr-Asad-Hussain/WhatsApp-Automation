from selenium import webdriver

def main():
      driver_path = "C:\\Users\\*************\\chromedriver.exe"
      driver = webdriver.Chrome(driver_path)
      driver.get('https://web.whatsapp.com/')

      # Get the Data from the User to Print etc
      members = int(input('HOW MANY MEMBERS/CHAT/GROUPS DO YOU WANT TO SEND MESSAGE\n Example 1,2,3,..  :  '))
      print()
      List_Of_Members = []
      for i in range(members):
            name = input('ENTER ' + str(i+1) +' NAME/GROUP TO WHOME MESSAGE IS SENT  :  ')
            List_Of_Members.append(name)
      print()      
      message = input('ENTER MESSAGE  :  ')
      print()
      count = int(input('HOW MANY TIMES DO YOU WANT TO SENT THIS MESSAGE\n Example 1,2,3,...  :  '))
      print()
      input('PRESS ANY KEY AFTER SCANNING THE QR CODE')


      for objects in List_Of_Members:
            User = driver.find_element_by_xpath('//span[@title = "{}"]'.format(objects))
            User.click()

            Message_Box = driver.find_element_by_class_name("_13mgZ")

            for i in range(count):
                  Message_Box.send_keys(message)
                  Button = driver.find_element_by_class_name('_3M-N-')  
                  Button.click()


if __name__=="__main__":
      main()

