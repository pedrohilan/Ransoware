def change_files(filename, cryptoFn, block_size=16):

	with open(filename, 'r+b') as _file: #'r+b' = leitura e binários
		raw_value = _file.read(block_size)
		while raw_value:
			cipher_value = cryptoFn(raw_value) #função 'cryptoFn' encriptar ou descriptar
			#compara o tamanho do bloco cifrado e plano (plain text)
			if len(raw_value) != len(cipher_value):
				raise ValueError('O valor cifrado {} tem um tamanho diferente do valor plano {}'.format(
					len(cipher_value), len(raw_value)))

			#método 'seek' trabalha com arquivos, ponteiro
			_file.seek(-len(raw_value), 1)
			_file.write(cipher_value)
			raw_value = _file.read(block_size)