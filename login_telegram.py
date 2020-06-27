#################################################################################################################
#                                                                                                               #
# Para usar este programa deve-se instalar a biblioteca do selenium atraves de comando: pip install selenium    #
# Versao Python: 2.7                                                                                            #
#																												#	
#################################################################################################################

# Constantes
CHROME_DRIVER_PATH = 'chromedriver_81.exe'
URL_TELEGRAM = 'https://web.telegram.org/'

# Imports
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Abrindo site e salvando cache
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome(CHROME_DRIVER_PATH,options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data") 
driver.get(URL_TELEGRAM)

time.sleep(60)  # Tempo para logar
driver.quit()