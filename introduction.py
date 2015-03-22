from random import choice

names = [("Astrid",1),("Bjorn",0),("Lif",1),("Ask",0),("Embla",1),("Alfhild",1),("Sigurd",0),("Ragnar",0),("Leif",0),("Hrothgar",0),("Aslaug",1),("Helgi",0),("Helga",1)]
locations = ["Helheim","Valhalla","Midgard","Jotunheimr","Asgard","Vanaheim","Alfheim"]
occupations = ["warrior", "farmer", "elf", "jotun", "earl", "dwarf"]
moccupations = ["king", "berserker"]
foccupations = ["shieldmaiden", "valkyrie"]

def picklocation():
	print(type(locations))
	return choice(locations)

def pickperson():
	return choice(names)

def pickoccupation(sex):
	if sex == 0:
		return choice(occupations+moccupations)
	else:
		return choice(occupations+foccupations)

def introduction(name,sex):
	location = picklocation()
	occupation = pickoccupation(sex)
	return("Meet",name,", a",occupation,"from",location)

def main():
	(name,sex) = pickperson()
	print(" ".join(introduction(name,sex)))


if __name__ == "__main__":
        main()
