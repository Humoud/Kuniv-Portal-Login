from splinter import Browser


print 'Starting...'

browser = Browser('firefox')        # using firefox
browser.visit("http://portal.ku.edu.kw/sisapp/faces/login.jspx")
browser.fill('username','xxxxx')    # enter student ID
browser.fill('password','yyyyy')   # enter password

browser.find_by_id('loginBtn').click()      # click login
