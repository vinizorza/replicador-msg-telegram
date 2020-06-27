#################################################################################################################
#                                                                                                               #
# Para usar este programa deve-se instalar a biblioteca do selenium atraves de comando: pip install selenium    #
# Versao Python: 2.7                                                                                            #
#																												#	
#################################################################################################################

# Imports
import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Constantes
CHROME_DRIVER_PATH = 'chromedriver_81.exe'
URL_TELEGRAM = 'https://web.telegram.org/'
ORIGEM = 'GafanhotoBot'
DESTINO = 'Teste'

# Abrindo URL e recuperando cache
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome(CHROME_DRIVER_PATH,options=chrome_options)
driver.get(URL_TELEGRAM)

def entrar_na_conversa(nome_chat):
	lista_chats = driver.find_elements_by_class_name('im_dialog_wrap')
	for dialogo_box in lista_chats:
		nome = dialogo_box.find_elements_by_class_name('im_dialog_peer')[0].find_element_by_tag_name('span').text
		if(nome == nome_chat):
			time.sleep(2)
			dialogo_box.click()
			break
			
def conversa_tem_notificacao(nome_chat):
	lista_chats = driver.find_elements_by_class_name('im_dialog_wrap')
	for dialogo_box in lista_chats:
		nome = dialogo_box.find_elements_by_class_name('im_dialog_peer')[0].find_element_by_tag_name('span').text
		qnt_notificacao = dialogo_box.find_elements_by_class_name('im_dialog_meta')[0].find_element_by_tag_name('span').text
		if(nome == nome_chat and qnt_notificacao != ''):
			return True
			
def encaminhar_mensagem(chat_destino):
	lista_mensagem = driver.find_elements_by_class_name('im_history_message_wrap')
	time.sleep(2)
	lista_mensagem[-1].click()
	botao_encaminhar = driver.find_element_by_class_name('im_edit_forward_btn')
	if(botao_encaminhar != None):		
		time.sleep(2)
		botao_encaminhar.click()
		modal_chats = driver.find_element_by_class_name('im_dialogs_modal_list')
		lista_chats = modal_chats.find_elements_by_tag_name('span')
		for chat in lista_chats:
			if(chat.text == chat_destino):
				time.sleep(2)
				chat.click()
				botao_enviar = driver.find_element_by_class_name('im_submit_send_label')
				time.sleep(2)
				botao_enviar.click()
				break
	

# Main
while(1):
	
	if(conversa_tem_notificacao(ORIGEM)):	
		entrar_na_conversa(ORIGEM)
		encaminhar_mensagem(DESTINO)
		entrar_na_conversa(DESTINO)

	time.sleep(2)