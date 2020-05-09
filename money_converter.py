import random
import time
import sys
import os
clear = lambda: os.system('cls')
clear()

def End1():
	print("\n\n")
	print("      _______                 _    ______                   ")
	print("     (_______)               | |  (____  \                  ")
	print("      _   ___  ___   ___   __| |   ____)  )_   _ _____      ")
	print("     | | (_  |/ _ \ / _ \ / _  |  |  __  (| | | | ___ |     ")
	print("     | |___) | |_| | |_| ( (_| |  | |__)  ) |_| | ____|   _ ")
	print("      \_____/ \___/ \___/ \____|  |______/ \__  |_____)  (_)")
	print("                                          (____/            ")

def End2():
	print("\n\n")
	print("      _______                 _    ______                   ")
	print("     (_______)               | |  (____  \                  ")
	print("      _   ___  ___   ___   __| |   ____)  )_   _ _____      ")
	print("     | | (_  |/ _ \ / _ \ / _  |  |  __  (| | | | ___ |     ")
	print("     | |___) | |_| | |_| ( (_| |  | |__)  ) |_| | ____|   _ _ ")
	print("      \_____/ \___/ \___/ \____|  |______/ \__  |_____)  (_|_)")
	print("                                          (____/            ")

def End3():
	print("\n\n")
	print("      _______                 _    ______                   ")
	print("     (_______)               | |  (____  \                  ")
	print("      _   ___  ___   ___   __| |   ____)  )_   _ _____      ")
	print("     | | (_  |/ _ \ / _ \ / _  |  |  __  (| | | | ___ |     ")
	print("     | |___) | |_| | |_| ( (_| |  | |__)  ) |_| | ____|   _ _ _ ")
	print("      \_____/ \___/ \___/ \____|  |______/ \__  |_____)  (_|_|_)")
	print("                                          (____/            ")

def Title():
	print("      _______                            _______                                               ")
	print("     (_______)                          (_______)                              _               ")
	print("      _  _  _  ___  ____  _____ _   _    _       ___  ____ _   _ _____  ____ _| |_ _____  ____ ")
	print("     | ||_|| |/ _ \|  _ \| ___ | | | |  | |     / _ \|  _ \ | | | ___ |/ ___|_   _) ___ |/ ___)")
	print("     | |   | | |_| | | | | ____| |_| |  | |____| |_| | | | \ V /| ____| |     | |_| ____| |    ")
	print("     |_|   |_|\___/|_| |_|_____)\__  |   \______)___/|_| |_|\_/ |_____)_|      \__)_____)_|    ")
	print("                               (____/                                                          ")

def ContinuedMoney():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	Title()
	print("\n\n" +"     Converted Currency you can use:")
	print("     Peso: " + str(Peso) + " 	[1]")
	print("     USD: " + str(USD) + " 	[2]")
	print("     Euro: " + str(Euro) + " 	[3]")
	print("     Yuan: " + str(Yuan) + " 	[4]")
	print("     Pound: " + str(Pound) + " 	[5]")
	print("     Yen: " + str(Yen) + " 	[6]")
	Continue = input("     Choose an Option: ")
	if Continue == "1":
		Amount = float(Peso)
		Currency = "Peso"
		clear()
		Pesos()
	elif Continue == "2":
		Amount = float(USD)
		Currency = "USD"
		clear()
		USDs()
	elif Continue == "3":
		Amount = float(Euro)
		Currency = "Euro"
		clear()
		Euros()
	elif Continue == "4":
		Amount = float(Yuan)
		Currency = "Yuan"
		clear()
		Yuans()
	elif Continue == "5":
		Amount = float(Pound)
		Currency = "Pound"
		clear()
		Pounds()
	elif Continue == "6":
		Amount = float(Yen)
		Currency = "Yen"
		clear()
		Yens()
	else:
		print("     Invalid Input... Please try again")
		time.sleep(2)
		clear()
		ContinuedMoney()

def Currencies():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	print("\n" + "     Currencies Available:" + "\n" + "     Peso [1]" + "\n" + "     USD [2]" + "\n" + "     Euro [3]" + "\n" + "     Yuan [4]" + "\n" + "     Pound [5]" + "\n" + "     Yen [6]" + "\n")
	Convert()

def Redo2():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	Title()
	print("\n\n" + "     Amount: " + str(Amount) + "     " + "Currency: " + str(Currency) + "\n")
	print("     Conversion Rates are:")
	print("     Peso: " + str(Peso))
	print("     USD: " + str(USD))
	print("     Euro: " + str(Euro))
	print("     Yuan: " + str(Yuan))
	print("     Pound: " + str(Pound))
	print("     Yen: " + str(Yen))
	Another()

def Redo():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	Title()
	print("\n\n" + "     Enter the Amount you want to be converted: " + str(Amount))
	Currencies()

def Another():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	Another = input("\n" + "     Do you want another Conversion? [1]" + "\n" + "     Do You want to convert using a Converted Currency? [2]" + "\n" + "     Exit Money Converter? [3]" + "\n" + "     Choose an Option: ")
	if Another == "1":
		clear()
		Start()
	elif Another == "3":
		clear()
		End1()
		time.sleep(1)
		clear()
		End2()
		time.sleep(1)
		clear()
		End3()
		time.sleep(1)
		clear()
		sys.exit()
	elif Another == "2":
		clear()
		ContinuedMoney()	
	else:
		print("     Invalid Input... Please try again")
		time.sleep(2)
		clear()
		Redo2()

def Pesos():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	Title()
	print("\n\n" + "     Amount: " + str(Amount) + "     " + "Currency: Peso" + "\n")
	Peso = Amount * 1
	USD =  Amount * 0.019
	Euro = Amount * 0.017
	Yuan = Amount * 0.13
	Pound = Amount * 0.015
	Yen = Amount * 2.16
	print("     Conversion Rates are:")
	print("     Peso: " + str(Peso))
	print("     USD: " + str(USD))
	print("     Euro: " + str(Euro))
	print("     Yuan: " + str(Yuan))
	print("     Pound: " + str(Pound))
	print("     Yen: " + str(Yen))
	Another()

def USDs():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	Title()
	print("\n\n" + "     Amount: " + str(Amount) + "     " + "Currency: USD" + "\n")
	Peso = Amount * 51.88
	USD =  Amount * 1
	Euro = Amount * 0.88
	Yuan = Amount * 6.71
	Pound = Amount * 0.76
	Yen = Amount * 111.92
	print("     Conversion Rates are:")
	print("     Peso: " + str(Peso))
	print("     USD: " + str(USD))
	print("     Euro: " + str(Euro))
	print("     Yuan: " + str(Yuan))
	print("     Pound: " + str(Pound))
	print("     Yen: " + str(Yen))
	Another()

def Euros():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	Title()
	print("\n\n" + "     Amount: " + str(Amount) + "     " + "Currency: Euro" + "\n")
	Peso = Amount * 59.03
	USD =  Amount * 1.14
	Euro = Amount * 1
	Yuan = Amount * 7.63
	Pound = Amount * 0.86
	Yen = Amount * 127.33
	print("     Conversion Rates are:")
	print("     Peso: " + str(Peso))
	print("     USD: " + str(USD))
	print("     Euro: " + str(Euro))
	print("     Yuan: " + str(Yuan))
	print("     Pound: " + str(Pound))
	print("     Yen: " + str(Yen))
	Another()

def Yuans():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	Title()
	print("\n\n" + "     Amount: " + str(Amount) + "     " + "Currency: Yuan" + "\n")
	Peso = Amount * 7.74
	USD =  Amount * 0.15
	Euro = Amount * 0.13
	Yuan = Amount * 1
	Pound = Amount * 0.11
	Yen = Amount * 16.70
	print("     Conversion Rates are:")
	print("     Peso: " + str(Peso))
	print("     USD: " + str(USD))
	print("     Euro: " + str(Euro))
	print("     Yuan: " + str(Yuan))
	print("     Pound: " + str(Pound))
	print("     Yen: " + str(Yen))
	Another()

def Pounds():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	Title()
	print("\n\n" + "     Amount: " + str(Amount) + "     " + "Currency: Pound" + "\n")
	Peso = Amount * 68.53
	USD =  Amount * 1.32
	Euro = Amount * 1.16
	Yuan = Amount * 8.86
	Pound = Amount * 1
	Yen = Amount * 147.84
	print("     Conversion Rates are:")
	print("     Peso: " + str(Peso))
	print("     USD: " + str(USD))
	print("     Euro: " + str(Euro))
	print("     Yuan: " + str(Yuan))
	print("     Pound: " + str(Pound))
	print("     Yen: " + str(Yen))
	Another()

def Yens():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	Title()
	print("\n\n" + "     Amount: " + str(Amount) + "     " + "Currency: Yen" + "\n")
	Peso = Amount * 0.46
	USD =  Amount * 0.0089
	Euro = Amount * 0.0079
	Yuan = Amount * 0.060
	Pound = Amount * 0.0068
	Yen = Amount * 1
	print("     Conversion Rates are:")
	print("     Peso: " + str(Peso))
	print("     USD: " + str(USD))
	print("     Euro: " + str(Euro))
	print("     Yuan: " + str(Yuan))
	print("     Pound: " + str(Pound))
	print("     Yen: " + str(Yen))
	Another()

def Convert():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	Currency = (input("     Enter the Currency you want to be converted: "))
	if Currency == "1":
		clear()
		Pesos()
	elif Currency == "2":
		clear()
		USDs()
	elif Currency == "3":
		clear()
		Euros()
	elif Currency == "4":
		clear()
		Yuans()
	elif Currency == "5":
		clear()
		Pounds()
	elif Currency == "6":
		clear()
		Yens()
	else:
		print("     Currency is not available or found... Please try again")
		time.sleep(2)
		clear()
		Redo()
		Convert()
	
def Start():
	global Amount
	global Currency
	global Peso
	global USD
	global Euro
	global Yuan
	global Pound
	global Yen
	Title()
	Amount = input("\n\n" + "     Enter the Amount you want to be converted: ")
	try:
		float(Amount)
		if float(Amount) >= 1:
			Amount = float(Amount)
			Currencies()
		else:
			print("     Input is not a valid amount... Please try again")
			time.sleep(2)
			clear()
			Start()
	except ValueError:
		print("     Input is not a number... Please try again")
		time.sleep(2)
		clear()
		Start()

Start()
