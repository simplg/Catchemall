#! / usr / bin / env python
import  sys
importer  inspecter

def  log ( chaîne ):
	sys . stderr . write ( "LOG:"  +  chaîne  +  " \ n " )

classe  ClassNode :
	def  __init__ ( soi , nom , parents ):
		soi . nom  =  nom
		soi . méthodes  = []
		soi . parents  =  parents


	def  addMethod ( soi , méthode ):
		soi . méthodes . append ( méthode )

 Processeur de classe :
	def  __init__ ( self , maxMethods , namesOnly ):
		soi . visité  =  set ()
		soi . modules  =  dict ()
		soi . maxMethods  =  maxMethods  si  maxMethods  ! =  Aucun  autre  - 1 + 2 ** 31
		soi . namesOnly  =  namesOnly

	def  processFiles ( soi , noms de fichiers ):
		importer le système d'  exploitation
		sys . chemin . append ( os . getcwd ())
		log ( "actuellement dans"  +  str ( os . getcwd ()))
		pour le  fichier  dans les  noms de fichiers :
			log ( "Fichier de traitement"  +  fichier )
			soi . processFile ( fichier )

	def  processFile ( soi , nom de fichier ):
		moduleName  =  nom de fichier . remplacer ( "./" , "" ). remplacer ( ".py" , "" ). remplacer ( "/" , "." )

		log ( "Fichier de traitement pour le module"  +  moduleName )
		__import__ ( moduleName , locaux (), globals ())
		soi . processModule ( sys . modules [ moduleName ])

	def  processModule ( self , module ):
		log ( "Module de traitement"  +  str ( module ))
		pour ( nom , quelque chose ) dans  inspect . getmembers ( module ):
			si  type ( quelque chose ) ==  dict :
				Continuez 

			si  repr ( quelque chose ) en  soi . visité :
				Continuez 

			soi . visité | = set ([ repr ( quelque chose )])

			si  inspecter . isclass ( quelque chose ):
				soi . processClass ( quelque chose )

			#elif inspect.ismodule (quelque chose):
			# self.processModule (quelque chose)

			sinon :
				#log (str (type (quelque chose)))
				passer  #log (str (quelque chose))

	def  processClass ( self , someClass ):
		nom  = une  classe . __Nom__
		log ( "Classe de traitement:"  +  nom  +  "dans le module"  +  someClass . __module__ )
		moduleName  = une  classe . __module__

		si  pas  moduleName  en  soi . modules :
			soi . modules [ nom_module ] =  liste ()

		classNode  =  ClassNode ( nom , someClass . __bases__ )
		soi . modules [ nom_module ]. append ( classNode )

		pour ( UnNom , quelque chose ) à  inspecter . getmembers ( someClass ):
			si  inspecter . ismethod ( quelque chose ):
				soi . processMethod ( quelque chose , classNode )

	def  processMethod ( self , someMethod , classNode ):
		log ( "Méthode de traitement:"  +  someMethod . __name__ )
		classNode . addMethod (une méthode )

	def  toDot ( self , out ):
		ligne  =  lambda  s : sortie . écrire ( s  +  " \ n " )
		dehors . écrire ( "" "
digraphe G {
		fontname = "Bitstream Vera Sans"
        fontsize = 8
		rankdir = BT
        nœud [
                fontname = "Bitstream Vera Sans"
                fontsize = 8
                shape = "record"
        ]
        bord [
                fontname = "Bitstream Vera Sans"
                fontsize = 8
        ]
"" " )

		classnameToDot  =  nom lambda  :   "Classe" + nom  

		def  isPublic ( méthode ):
			si  méthode . __nom__ . find ( "_" ) ==  0  et \
				méthode . __nom__ . rfind ( "_" ) <  len ( method . __name__ ) - 1 :
				retourne  False
			sinon :
				retourne  True

		def  writeDecl ( out , méthode , symbole ):
			dehors . écrire ( symbole  +  "" )

			dehors . write ( méthode . __nom__ )
			argspec  =  inspecter . getargspec ( méthode )
			dehors . écriture ( inspecter . formatargspec ( * ( argspec [: 2 ])) +  "\ l" )

		pour ( nom , module ) en  soi . modules . articles ():
			si  len ( module ) >  1 :
				line ( "subgraph cluster {modulename} {" . replace ( "{modulename}" ,
					nom . remplacer ( "." , "" )))
				line ( "label = \" Module "  +  nom  +  " \ " " )

			pour  c  dans le  module :
				ligne ( classnameToDot ( c . nom ) +  "[" )


				dehors . write ( "label = \" {"  +  c . nom )
				

				si  pas  auto . nomsUniquement :
					dehors . écrire ( "|" )
					
					methodsTried  =  0
					pour la  méthode  en  c . méthodes :
						si  pas  IsPublic ( méthode ):
							si les  méthodes ont essayé  <  soi-même . maxMethods :
								writeDecl ( out , méthode , "-" )
							méthodes essayées  + =  1

					dehors . écrire ( "|" )
					
					pour la  méthode  en  c . méthodes :
						if  isPublic ( méthode ):
							si les  méthodes ont essayé  <  soi-même . maxMethods :
								writeDecl ( out , méthode , "+" )
							méthodes essayées  + =  1

					si les  méthodes ont essayé  >  auto . maxMethods :
						dehors . écrire ( "........... \ l" )

				dehors . écrire ( "} \" \ n " )
				ligne ( "]" )

			si  len ( module ) >  1 :
				ligne ( "}" )

		dehors . écrire ( "" "
		bord [
                arrowhead = "vide"
        ]
		"" " )

		pour  module  en  soi . modules . valeurs ():
			pour  c  dans le  module :
				pour  parent  en  c . parents :
					ligne ( classnameToDot ( c . nom ) +  "->"  +
							classnameToDot ( parent . __name__ ))

		ligne ( "}" )

si  __name__  ==  "__main__" :
	si  len ( sys . argv ) ==  1 :
		print ( "USAGE:"  +  sys . argv [ 0 ] +  "[--names-only] [--max-methods = <n>] <pythonfiles>" )
	sinon :
		log ( "Démarrage du traitement du vecteur d'argument" )
		maxMethods  =  Aucun
		namesOnly  =  Faux
		importer  re
		deleteArgs  = []
		pour  arg  dans  sys . argv [ 1 :]:
			maxMethodsString  =  "--max-methods ="
			si  re . match ( maxMethodsString  +  "[0-9] +" , arg ):
				maxMethods  =  int ( arg [ len ( maxMethodsString ):])
				log ( "Définition des méthodes max sur"  +  str ( maxMethods ))
				deleteArgs . ajouter ( arg )

			si  arg  ==  "--names-only" :
				namesOnly  =  True
				log ( "Définition des noms uniquement sur True" )
				deleteArgs . ajouter ( arg )
				
		# Supprimer les arguments non-fichier de la liste d'arguments
		pour  arg  dans  deleteArgs :
			sys . argv . supprimer ( arg )

		proc  =  Processeur ( maxMethods  =  maxMethods , namesOnly  =  namesOnly )
		proc . processFiles ( sys . argv [ 1 :])
		proc . toDot ( sys . stdout )