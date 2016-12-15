import socket   #for sockets
import sys  #for exit

def avanzar(ip,n,tiempo): 
	try:
	    #create an AF_INET, STREAM socket (TCP)
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, msg:
	    #print 'Fallo al crear Socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
	    sys.exit();
	 
	 
	host = ip
	port = 80
	 
	try:
	    remote_ip = socket.gethostbyname( host )
	 
	except socket.gaierror:
	    #could not resolve
	    #print 'Hostname could not be resolved. Exiting'
	    sys.exit()
	     
	 
	#Connect to remote server
	s.connect((remote_ip , port))

	r= str(n)
	t= str(tiempo)
	comando = ("av")
	instruccion = comando + "," + r + "," + t
	s.send(instruccion)
	
	print instruccion
	s.close()


def derecha(ip,n,tiempo): 
	try:
	    #create an AF_INET, STREAM socket (TCP)
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, msg:
	    #print 'Fallo al crear Socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
	    sys.exit();
	 
	 
	host = ip
	port = 80
	 
	try:
	    remote_ip = socket.gethostbyname( host )
	 
	except socket.gaierror:
	    #could not resolve
	    #print 'Hostname could not be resolved. Exiting'
	    sys.exit()
	     
	#print 'Ip address of ' + host + ' is ' + remote_ip
	 
	#Connect to remote server
	s.connect((remote_ip , port))
	 

	r= str(n)
	t= str(tiempo)
	#while True:
	comando = ("de")
	instruccion = comando + "," + r + "," + t
	s.send(instruccion)
	print instruccion
	
	s.close()


def izquierda(ip,n,tiempo): 
	try:
	    #create an AF_INET, STREAM socket (TCP)
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, msg:
	    #print 'Fallo al crear Socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
	    sys.exit();

	 
	host = ip
	port = 80
	 
	try:
	    remote_ip = socket.gethostbyname( host )
	 
	except socket.gaierror:
	    #could not resolve
	    #print 'Hostname could not be resolved. Exiting'
	    sys.exit()
	     
	#print 'Ip address of ' + host + ' is ' + remote_ip
	 
	#Connect to remote server
	s.connect((remote_ip , port))
	 

	r= str(n)
	t= str(tiempo)
	comando = ("iz")
	instruccion = comando + "," + r + "," + t
	s.send(instruccion)	
	print instruccion
	s.close()

def reversa(ip,n,tiempo): 
	try:
	    #create an AF_INET, STREAM socket (TCP)
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, msg:
	    #print 'Fallo al crear Socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
	    sys.exit();
	 
	 
	host = ip
	port = 80
	 
	try:
	    remote_ip = socket.gethostbyname( host )
	 
	except socket.gaierror:
	    #could not resolve
	    #print 'Hostname could not be resolved. Exiting'
	    sys.exit()
	     
	#print 'Ip address of ' + host + ' is ' + remote_ip
	 
	#Connect to remote server
	s.connect((remote_ip , port))
	 

	r= str(n)
	t = str(tiempo)
	comando = ("re")
	instruccion = comando + "," + r + "," + t 
	s.send(instruccion)	
	print instruccion
	s.close()