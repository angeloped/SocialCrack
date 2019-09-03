#!/usr/bin/python
import urllib2
import time
import os

logo = """
  ___           _        _   ___                 _   
 / __| ___  __ (_) __ _ | | / __| _ _  __ _  __ | |__
 \__ \/ _ \/ _|| |/ _` || || (__ | '_|/ _` |/ _|| / /
 |___/\___/\__||_|\__,_||_| \___||_|  \__,_|\__||_\_\ 
             // if there's a hint, there's a key. //

 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 + Author: Bryan Angelo Pedrosa
 + Project: BakerySec
 + Date Created: 8/12/2019
 + Description: This is a social engineering password
    cracker for testing weak and easy2guess passwords.
 + Disclaimer: This program is created for a cybersecurity
    project and should not be used illegally. I am not
    liable for any damage you commited by using this tool.
 + To victims: Please use a complex password. =D
 + How to use: "Easy, just put subject's personal info".
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 <Enter> - Leave Blank For Automatic Process.
 [0] - Create Password Hints
 [1] - Generate Password Dict File From Hints
 [2] - Online Login Cracker (soon)
 [3] - Exit
"""

"""
Disclaimer: I am not liable for damages you committed by using the BakerySec tools.
This program is my personal research project in the field of penetration testing and I do not suggest y'all to hack without consent.
"""


def browse(url="", header_d={}, uri="", data=""):
	u = urllib2.urlopen(url, data)
	u.request('POST', uri, data, headers)


def req_server(arguments={}, url=""):# for web/internet only!!
	try:
		data = urllib.urlencode(arguments)
		opener = urllib2.build_opener(urllib2.HTTPHandler())
		return opener.open(url, data=data).read()
	except Exception as err:
		return "Er"


def SoCrack_Array_Bases(key_hints):
	base = len(key_hints)
	deciminal = 0
	while True:
		other_base = []
		decimal = deciminal
		
		# generate array of password guesses
		while decimal != 0:
			other_base.insert(0, key_hints[decimal % base])
			decimal = decimal / base
		
		# if other_base item length reached the max
		if len(other_base) > base:
			break
		
		# if other_base is empty
		if len(other_base) == 0:
			other_base.append(key_hints[0])
		
		yield "".join(other_base)
		
		deciminal += 1


def fname_input():
	# enter password hint file.
	while 1:
		try:
			filename = raw_input("Enter filename: ")
		except NameError:
			filename = input("Enter filename: ")
		
		if filename == "":
			print("I can't process a blank filename for you.")
			continue
		else:
			break
	return filename


def generate_hints(filename):
	# password hint file maker
	if os.path.exists("{0}.hint".format(filename)):
		try:
			overwrite = raw_input("{0}: file already exists. Overwrite it? (Y/n)".format("{0}.hint".format(filename)))
		except NameError:
			overwrite = input("{0}: file already exists. Overwrite it? (Y/n)".format("{0}.hint".format(filename)))
		
		if overwrite.lower() in ["", "y"]:
			with open("{0}.hint".format(filename), "w") as overw_:
				overw_.write("")
		else:
			return
	
	try:
		with open("{0}.hint".format(filename), "a+") as passwd_hints:
			while 1:
				try:
					jewel_hint = raw_input(":")
				except NameError:
					jewel_hint = input(":")
				except KeyboardInterrupt:
					break
				
				# if line is blank, finish the task.
				if jewel_hint == "":
					break
				
				passwd_hints.write("{0}\n".format(jewel_hint))
	except:
		pass
	finally:
		print("\n[+] password hint file created!!! name: [\"{0}\"]".format("{0}.hint".format(filename)))


def generate_passwords(filename):
	#password_list = ""
	if os.path.exists("{0}.hint".format(filename)):
		# open password hint file
		with open("{0}.hint".format(filename)) as pwhint:
			hints = [line for line in pwhint.read().split("\n") if not line == ""]
		
		# generate password guesses file 
		try:
			with open("{0}.crk".format(filename), "a+") as gword:
				for guess in SoCrack_Array_Bases(hints):
					#print("generated guess: {0}".format(guess))
					gword.write("{0}\n".format(guess))
					#password_list += guess + "\n"
		except:
			pass
		finally:
			print("[+] password dictionary created. name: [\"{0}\"]".format("{0}.crk".format(filename)))
		
		# return output even if unnecessary.
		#return password_list
	else:
		print("[!] no hint file found.")


def auto_do():
	filename = fname_input()
	# if file doesn't exists
	if not os.path.exists("{0}.hint".format(filename)):
		generate_hints(filename)
	print("[+] generating password dictionary....")
	generate_passwords(filename)



if __name__ == "__main__":
	while 1:
		# print heading
		print(logo)
		try:
			choice = raw_input("Enter your choice: ")
		except:
			choice = input("Enter your choice: ")
		
		if choice == "":
			auto_do()
		elif choice == "0":
			filename = fname_input()
			generate_passwords(filename=filename)
		elif choice == "1":
			filename = fname_input()
			generate_hints(filename=filename)
		elif choice == "2":
			print("Online dictionary attack hasn't been made yet. Send help! :D")
		elif choice == "3":
			break
		else:
			print("\"{0}\": unknown choice.".format(choice))
		time.sleep(1.5)


"""
#browse(url="http://localhost/demologin.php")

# TO DO! WORK IN PROGRESS!

u = urllib2.urlopen('http://myserver/inout-tracker', data)
h.request('POST', '/inout-tracker/index.php', data, headers)


url = 'http://www.example.com/form'
values = {'param1' : '3','param2' : '29'}
data = urllib.urlencode(values)
req = urllib2.Request(url)
req.add_data(data)
try:
    html = urllib2.urlopen(req)
except HTTPError, e:
    ss.invalid_links += 'HTTP Error ERROR en el listado code => %s \n URL=> %s\n' % (e.code,url)
except URLError, e:
    ss.invalid_links += 'URL Error ERROR en el listado reason => %s \n URL=> %s\n' % (e.reason,url)
soup = BeautifulSoup(html)
@angeloped
"""

