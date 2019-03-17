with open('structures.txt', "r") as fichier:
	structure_niveau = []
	for ligne in fichier:
	 	ligne_niveau = []
	 	for sprite in ligne:
	 		if sprite != '\n':
	 			ligne_niveau.append(sprite)
 		structure_niveau.append(ligne_niveau)	
		
	print(structure_niveau)
	




		









    