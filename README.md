# autoTesting

Make sure to install selenium. - pip install selenium

Then make sure to download the correct driver. In this case we're working with chromedriver. Download the correct one for your machine:

https://chromedriver.storage.googleapis.com/index.html?path=104.0.5112.79/

Make sure the chromedriver is in the same folder as your python file.

In this case we use seleniumeasy website. 

There is a few steps we take in this simple code.

  1) Maximize our chrome tab
  2) Get the URL we will be working on. In our case it is: https://demo.seleniumeasy.com/basic-first-form-demo.html
  3) Find the button below the inputfield
  4) Find the inputfield and make our program write in it. In our case we write: "This is a test"
  5) Click the button so we get the result
  6) At last we use the .quit() method to close our browser and quit our chromedriver.
  
Cheatsheet link here: 
http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/
