# Request conselho grátis
	# este algoritmo busca uma frase de efeito aleatorio de uma API gratis da web

	# Dev: https://github.com/marcosvile
	# API: https://api.adviceslip.com/ by https://github.com/tomkiss
	# 

import settings
import requests
import json

def get_random_conselho():
	requisicao = requests.get('https://api.adviceslip.com/advice');

	conselho = json.loads (requisicao.text)

	print(conselho['slip']['advice'])

	return get_random_conselho