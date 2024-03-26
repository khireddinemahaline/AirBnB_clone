# AirBnb Console Project:
## First Step : The console
1. creat data model
2. manage (create, update, destroy, etc..) via the console
3. store and presist objects to (json file)
## store object
Serialization and deserialization are two important concepts in programming that allow objects to be easily stored, transmitted, and reconstructed. They’re used in various scenarios, such as storing objects in a database, sending objects over a network, or caching objects in memory
#### Files and Directory 

AirBnB_clone : the main reposotry for the project
	models : directory containt all classes and module files (object/instance)
		- base_model.py : file contain the base class of all our module
			* attributes : id , created_at , update_at
			* methods : save() , to_json()  
	test   : directory contain all unit test file 
	models/engine : diectory will contain all storage class  
		- file_storage.py (only one file for this project)
	
	= console.py >>> file the entry point of our comand interpreter




