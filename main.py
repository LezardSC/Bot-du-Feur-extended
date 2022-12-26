import re
import random
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)
	
	#####################################################################################
	#Code pour le niveau du bot##########################################################
	#####################################################################################

	#####################################################################################
	#Code pour la commande insulte#######################################################
	#####################################################################################



	#####################################################################################
	#Code pour accueillir les nouveaux arrivants avec une copypasta######################
	#####################################################################################

@client.event
async def on_member_join(member):
	response = ""
	line = ""
	rand = random.randint(1, 31)
	responded = False
	channel = member.guild.system_channel  # récupère le canal de bienvenue du serveur
	if channel is not None:  # vérifie que le canal existe
					#Générer une des copypasta au pif
					if rand == 1:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A1.")
								if index != -1:
									line = line[index + len("A1."):]
									response = line
					elif rand == 2:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A2.")
								if index != -1:
									line = line[index + len("A2."):]
									response = line
					elif rand == 3:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A3.")
								if index != -1:
									line = line[index + len("A3."):]
									response = line
					elif rand == 4:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A4.")
								if index != -1:
									line = line[index + len("A4."):]
									response = line
					elif rand == 5:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A5.")
								if index != -1:
									line = line[index + len("A5."):]
									response = line
					elif rand == 6:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A6.")
								if index != -1:
									line = line[index + len("A6."):]
									response = line
					elif rand == 7:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A7.")
								if index != -1:
									line = line[index + len("A7."):]
									response = line
					elif rand == 8:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A8.")
								if index != -1:
									line = line[index + len("A8."):]
									response = line
					elif rand == 9:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A9.")
								if index != -1:
									line = line[index + len("A9."):]
									response = line
					elif rand == 10:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A10.")
								if index != -1:
									line = line[index + len("A10."):]
									response = line
					elif rand == 11:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A11.")
								if index != -1:
									line = line[index + len("A11."):]
									response = line
					elif rand == 12:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A12.")
								if index != -1:
									line = line[index + len("A12."):]
									response = line
					elif rand == 13:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A13.")
								if index != -1:
									line = line[index + len("A13."):]
									response = line
					elif rand == 14:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A14.")
								if index != -1:
									line = line[index + len("A14."):]
									response = line
					elif rand == 15:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A15.")
								if index != -1:
									line = line[index + len("A15."):]
									response = line
					elif rand == 16:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A16.")
								if index != -1:
									line = line[index + len("A16."):]
									response = line
					elif rand == 17:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A17.")
								if index != -1:
									line = line[index + len("A17."):]
									response = line
					elif rand == 18:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A18")
								if index != -1:
									line = line[index + len("A18."):]
									response = line
					elif rand == 19:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A19.")
								if index != -1:
									line = line[index + len("A19."):]
									response = line
					elif rand == 20:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A20.")
								if index != -1:
									line = line[index + len("A20."):]
									response = line
					elif rand == 21:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A21.")
								if index != -1:
									line = line[index + len("A21."):]
									response = line
					elif rand == 22:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A22.")
								if index != -1:
									line = line[index + len("A22."):]
									response = line
					elif rand == 23:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A23.")
								if index != -1:
									line = line[index + len("A23."):]
									response = line
					elif rand == 24:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A24.")
								if index != -1:
									line = line[index + len("A24."):]
									response = line
					elif rand == 25:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A25.")
								if index != -1:
									line = line[index + len("A25."):]
									response = line
					elif rand == 26:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A26.")
								if index != -1:
									line = line[index + len("A26."):]
									response = line
					elif rand == 27:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A27.")
								if index != -1:
									line = line[index + len("A27."):]
									response = line
					elif rand == 28:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A28.")
								if index != -1:
									line = line[index + len("A28."):]
									response = line
					elif rand == 29:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A29.")
								if index != -1:
									line = line[index + len("A29."):]
									response = line
					elif rand == 30:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A30.")
								if index != -1:
									line = line[index + len("A30."):]
									response = line
					elif rand == 31:
						with open("copypastas.txt", "r") as f:
							for line in f:
								index = line.find("A31.")
								if index != -1:
									line = line[index + len("A31."):]
									response = line
					if response and not responded:
						response = f"{response} {member.mention}"
						await channel.send(response)
						responded = True



@client.event
async def on_message(message):
	response = ""
	#####################################################################################
	#Code pour les cas spécifiques de réponses en copypasta##############################
	#####################################################################################

	# Ignorer les messages de l'utilisateur lui-même
	if message.author == client.user:
		return
	
	pattern_pâques = r"🗿"
	pattern_pétergueule = r"(?i)\bje te pète la gueule|je lui pète la gueule|je vais te pèter la gueule|je vais te peter la gueule|je te pete la gueule|je lui pete la gueule|envie de lui peter la gueule|envie de lui pèter la gueule|je vais lui exploser la gueule|je vais lui peter la gueule|je vais lui pèter la gueule[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"
	pattern_pokemonla = r"(?i)\bpokemon legend arceus|pokémon legend arceus|pokémon légend arceus|pokémon legends arceus|pokemon legends arceus[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"
	pattern_geek = r"(?i)je suis un putain de geek|je sui un putain de geek|je suis un ptn de geek|j'suis un ptn de geek|j'suis un putain de geek"
	pattern_otaku = r"(?i)otaku"
	pattern_claviercolle = r"(?i)clavier qui colle|clavier colle"
	pattern_parisnul = r"(?i)paris c'est nul|nique paris|paris on t'encule|trop nul paris|paris pire ville"
	pattern_miaou = r"(?i)\bmiaou|miaouu|miiaou[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"
	pattern_peurdequoi = r"(?i)de quoi tu as peur|c'est quoi ta phobie|t'as une peur|t'as peur de quoi|de quoi t'as peur|c'est quoi ta phobie"
	pattern_starwars = r"(?i)star wars c'est nul|nique star wars|star wars surcote|star wars surcoté|star wars surcôté|nul star wars"
	pattern_basé = r"(?i)\bbasé\b"
	pattern_crépi = r"(?i)\bcrépi\b"
	pattern_ricketmorty = r"(?i)rick et morty"
	pattern_NicolasSarkozy = r"(?i)Nicolas Sarkozy|le temps des tempêtes|le temps des tempetes"
	pattern_OSS117 = r"(?i)oss117"
	pattern_manchot = r"(?i)\bmanchot\b|\bmalte\b|maltais\b"
	pattern_académiefrançaise = r"(?i)oss117"
	pattern_combattrebébés = r"(?i)combattre des bébés|combattre des bb|combattre d bb|combattre d bébés|affronter des bébés|affronter des bb"
	pattern_waifu = r"(?i)waifu"
	pattern_mondedemerde = r"(?i)monde de merde"
	pattern_bakugo = r"(?i)bakugo"
	pattern_based = r"(?i)\bbased\b"
	pattern_préli = r"(?i)rapport sexuel|préliminaires|preliminaires"
	pattern_genshinimpact = r"(?i)genshin impact"

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if message.mention_everyone:
				index = line.find("S1.")
				if index != -1:
					line = line[index + len("S1."):]
					response = line
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

# statue de pâques
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_pâques, message.content, re.IGNORECASE):
				index = line.find("S2.")
				if index != -1:
					line = line[index + len("S2."):]
					response = line
				if response and not responded:
					await message.channel.send(response, reference=message)
					responded = True

# péter la gueule
	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_pétergueule, message.content, re.IGNORECASE):
				index = line.find("S3.")
				if index != -1:
					line = line[index + len("S3."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_pokemonla, message.content, re.IGNORECASE):
				index = line.find("S4.")
				if index != -1:
					line = line[index + len("S4."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_pokemonla, message.content, re.IGNORECASE):
				index = line.find("S4.")
				if index != -1:
					line = line[index + len("S4."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_geek, message.content, re.IGNORECASE):
				index = line.find("S5.")
				if index != -1:
					line = line[index + len("S5."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_otaku, message.content, re.IGNORECASE):
				index = line.find("S6.")
				if index != -1:
					line = line[index + len("S6."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_claviercolle, message.content, re.IGNORECASE):
				index = line.find("S7.")
				if index != -1:
					line = line[index + len("S7."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_parisnul, message.content, re.IGNORECASE):
				index = line.find("S8.")
				if index != -1:
					line = line[index + len("S8."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

# miaou
	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_miaou, message.content, re.IGNORECASE):
				index = line.find("S9.")
				if index != -1:
					line = line[index + len("S9."):]
					response = line
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_peurdequoi, message.content, re.IGNORECASE):
				index = line.find("S10.")
				if index != -1:
					line = line[index + len("S10."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_starwars, message.content, re.IGNORECASE):
				index = line.find("S11.")
				if index != -1:
					line = line[index + len("S11."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_basé, message.content, re.IGNORECASE):
				index = line.find("S12.")
				if index != -1:
					line = line[index + len("S12."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_crépi, message.content, re.IGNORECASE):
				index = line.find("S13.")
				if index != -1:
					line = line[index + len("S13."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_ricketmorty, message.content, re.IGNORECASE):
				index = line.find("S14.")
				if index != -1:
					line = line[index + len("S14."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_NicolasSarkozy, message.content, re.IGNORECASE):
				index = line.find("S15.")
				if index != -1:
					line = line[index + len("S15."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_OSS117, message.content, re.IGNORECASE):
				index = line.find("S16.")
				if index != -1:
					line = line[index + len("S16."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_manchot, message.content, re.IGNORECASE):
				index = line.find("S17.")
				if index != -1:
					line = line[index + len("S17."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_académiefrançaise, message.content, re.IGNORECASE):
				index = line.find("S18.")
				if index != -1:
					line = line[index + len("S18."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_combattrebébés, message.content, re.IGNORECASE):
				index = line.find("S19.")
				if index != -1:
					line = line[index + len("S19."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_waifu, message.content, re.IGNORECASE):
				index = line.find("S20.")
				if index != -1:
					line = line[index + len("S20."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_mondedemerde, message.content, re.IGNORECASE):
				index = line.find("S21.")
				if index != -1:
					line = line[index + len("S21."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_bakugo, message.content, re.IGNORECASE):
				index = line.find("S22.")
				if index != -1:
					line = line[index + len("S22."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_based, message.content, re.IGNORECASE):
				index = line.find("S23.")
				if index != -1:
					line = line[index + len("S23."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_préli, message.content, re.IGNORECASE):
				index = line.find("S24.")
				if index != -1:
					line = line[index + len("S24."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	rand = random.randint(1, 2)
	responded = False
	with open("copypastas.txt", "r") as f:
		# Parcourir chaque ligne du fichier
		for line in f:
			if re.search(pattern_genshinimpact, message.content, re.IGNORECASE):
				index = line.find("S25.")
				if index != -1:
					line = line[index + len("S25."):]
					response = line
					response = response.replace("\\n", "\n")
				if response and not responded and rand == 1:
					await message.channel.send(response, reference=message)
					responded = True

	#####################################################################################
	#Code pour les quoi ? Feur et équivalents############################################
	#####################################################################################

	pattern_pourfeur = r"(?i)pourquoi[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"
	pattern_defeur = r"(?i)de quoi[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"
	pattern_afeur = r"(?i)\bà quoi|\ba quoi[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"
	pattern_cestkette = r"(?i)c'est qui|\bcest qui|\bc ki[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"
	pattern_pourkette = r"(?i)pour qui|\bpr ki|\bpr qui[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"
	pattern_feur = r"(?i)quoi[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"
	pattern_dien = r"(?i)hein[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"
	pattern_kette = r"(?i)qui[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"
	pattern_stiti = r"(?i)oui[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"
	pattern_bril = r"(?i)non|nom[\s!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$"


	rand = random.randint(1, 7)
	if re.search(pattern_pourfeur, message.content, re.IGNORECASE):
		if rand == 1:
			response = "pour feur."
		elif rand == 2:
			response = "pour feur je pense."
		elif rand == 3:
			response = "sûrement pour feur"
		elif rand == 4 or rand == 5 or rand == 6:
			response = "feur"
		elif rand == 7:
			response = "FEUR"
		await message.channel.send(response, reference=message)
	
	elif re.search(pattern_defeur, message.content, re.IGNORECASE):
		if rand == 1:
			response = "de feur."
		elif rand == 2:
			response = "de feur je pense."
		elif rand == 3:
			response = "sûrement de feur"
		elif rand == 4 or rand == 5 or rand == 6:
			response = "feur"
		elif rand == 7:
			response = "FEUR"
		await message.channel.send(response, reference=message)

	elif re.search(pattern_afeur, message.content, re.IGNORECASE):
		if rand == 1:
			response = "à feur."
		elif rand == 2:
			response = "à feur je pense."
		elif rand == 3:
			response = "sûrement à feur"
		elif rand == 4 or rand == 5 or rand == 6:
			response = "feur"
		elif rand == 7:
			response = "FEUR"
		await message.channel.send(response, reference=message)

	elif re.search(pattern_cestkette, message.content, re.IGNORECASE):
		if rand == 1:
			response = "c'est kette."
		elif rand == 2:
			response = "c'est kette je pense."
		elif rand == 3:
			response = "sûrement pour kette"
		elif rand == 4 or rand == 5 or rand == 6:
			response = "kette"
		elif rand == 7:
			response = "KETTE"
		await message.channel.send(response, reference=message)

	elif re.search(pattern_pourkette, message.content, re.IGNORECASE):
		if rand == 1:
			response = "pour kette."
		elif rand == 2:
			response = "pour kette je pense."
		elif rand == 3:
			response = "sûrement pour kette"
		elif rand == 4 or rand == 5 or rand == 6:
			response = "kette"
		elif rand == 7:
			response = "KETTE"
		await message.channel.send(response, reference=message)


	elif re.search(pattern_feur, message.content, re.IGNORECASE):
		if rand >= 1 and rand <= 3:
			response = "feur"
		elif rand == 4 | rand == 5:
			response = "feur !"
		elif rand == 6:
			response = "FEUR"
		elif rand == 7:
			response = "FEUR !"
		if response:
			await message.channel.send(response, reference=message)

	elif re.search(pattern_dien, message.content, re.IGNORECASE):
		if rand == 1 and rand == 2:
			response = "dien"
		elif rand == 3:
			response = "dien !"
		elif rand == 4:
			response = "DIEN"
		elif rand == 5:
			response = "DIEN !"
		elif rand == 6:
			response = "deux"
		elif rand == 7:
			response = "DEUX"
		await message.channel.send(response, reference=message)

	elif re.search(pattern_kette, message.content, re.IGNORECASE):
		if rand >= 1 and rand <= 3:
			response = "kette"
		elif rand == 4 or rand == 5:
			response = "kette !"
		elif rand == 6:
			response = "KETTE"
		elif rand == 7:
			response = "KETTE !"
		await message.channel.send(response, reference=message)
	
	elif re.search(pattern_stiti, message.content, re.IGNORECASE):
		if rand >= 1 and rand <= 3:
			response = "stiti"
		elif rand == 4 or rand == 5:
			response = "stiti !"
		elif rand == 6:
			response = "STITI"
		elif rand == 7:
			response = "STITI !"
		await message.channel.send(response, reference=message)

	elif re.search(pattern_bril, message.content, re.IGNORECASE):
		if rand >= 1 and rand <= 3:
			response = "bril"
		elif rand == 4 or rand == 5:
			response = "bril !"
		elif rand == 6:
			response = "BRIL"
		elif rand == 7:
			response = "BRIL !"
		await message.channel.send(response, reference=message)
###########################################
load_dotenv(dotenv_path="config")
client.run(os.getenv("TOKEN"))