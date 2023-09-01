from translate import Translator

translator = Translator(to_lang = 'es')
try:
	with open('./text.txt', mode = 'r') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		with open('./test-es.txt', mode = 'w') as my_file2:
			my_file2.write(translation)
except FileNotFoundError as e:
	print('Check your file path silly!') 