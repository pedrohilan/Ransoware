import os

def discover(initial_path):
	extensions = [
		'exe','dll','so','deb','vmlinuz','img', #Arquivos do Sitema
		'jpg', 'jpeg', 'png', 'bmp', 'gif', 'svg', 'psd', 'raw', #imagens
		'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape', #audios
		'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', #videos
		'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', #Microsoft office
		#OpenOffice, Adobe, Latex, Markdown, etc
		'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', 
		'yml', 'yaml', 'json', 'xml', 'csv', #dados estruturados e config
		'db', 'sql', 'dbf', 'mdb', 'iso', #banco de dados e imagens de disco
		'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', #tecnologias web
		'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', #codigo fonte c e c++
		'java', 'class', 'jar', #codigos fonte java
		'ps', 'bat', 'vb', #scripts de sistema windows
		'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', #scripts de sistema unix
		'go', 'py', 'pyc', 'bf', 'coffe', #outros tipos de codigos fonte
		'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak', #arquivos compactados e backups
	]
	
	for dirpath, dirs, files in os.walk(initial_path):
		for _file in files:
			absolute_path = os.path.abspath(os.path.join(dirpath, _file))
			ext = absolute_path.split('.')[-1]#pegar o último item do array '[-1]'

			if ext in extensions:
				yield absolute_path #'yield' da o retorno e volta a executar, diferente do 'return'
	
#isto só é executado quando executa o módulo diretamente
#o '__name__' só recebe '__main__' quando um módulo é executado diretamente, caso contrário ele recebe o nome do módulo

if __name__ == '__main__': 
	x = discover(os.getcwd()) #'getcwd' caminho atual
	for i in x:
		print(i)
