fd = open("/etc/passwd","r")
lineas = fd.readlines()
fd.close()
# lineas[:1] # ['pepepepepepepepe'] Lista
# lineas[0] # 'pepepepepepepepe' String

# Forma 1
for linea in lineas:
	pos_fin = linea.find(":")
	login = linea[:pos_fin]
	pos_com = linea.rfind(":") + 1
	shell = linea[pos_com:-1]
	print(login, shell)

# Forma 2
for linea in lineas:
	elementos = linea.split(":")
	login = elementos[0]
	shell = elementos[-1]
	shell_bueno = shell[:-1]
	print(login, shell_bueno)

# Forma 3
for linea in lineas:
	login = linea.split(':')[0]
	shell = linea.split(':')[-1][:-1]
	print(login,shell)
