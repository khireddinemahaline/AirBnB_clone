# Airbnb Clone Project
### 1. Project Overview
AirBnB Clone (the console) is the first in the serious of projects to wards a full stack AirBnB web application. This repo contains a console application that can be used to manage the various instances of class used in the AirBnB web application.
### 2. Project Phases
* Command Interpreter: Serving as the foundation, the command interpreter allows for data manipulation without a graphical interface, akin to a Shell environment. This phase is pivotal, providing developers with a platform for iterative development and debugging.
* Website (Frontend): The face of the final product, the website showcases static and dynamic content to users, offering an experience tailored to their needs.
* Data Storage: Whether through databases or files, this phase ensures the seamless storage and retrieval of crucial data objects, facilitating efficient information management.
* API Development: Acting as the bridge between the frontend and data storage, the API enables communication and interaction, empowering users to retrieve, create, delete, and update data seamlessly.
### 3. Tools and framwork
- python programming language -> devlope the backend of the website
- cmd module -> devlope the console.py file to interact with website using command line
- json module -> store data in json file
- ORM (sqlalchemy) library -> store data in database
- DBMS (mysql server) -> the database that handel the data in it
- Flask python framwork -> handel requeste response of website on the server
- API -> work as the linked betwen the frontend and the backend part
### 4. Architacteur
/test
/test_models
    /engine
    __init__.py
    test_file_storage.py
    test_db_storage.db
    __init__.py
    test_basemodel.py
    test_user.py
    test_city.py
    test_state.py
    test_place.py
    test_review.py
    test_amenity.py
/models
    __init__.py
    /engine
        __init__.py
        db_storage.py
        file_storage.py
    basemodel.py # all inhert from this class (id, calss_name, dic)
    user.py # user credantial
    city.py # the city to search for
    state.py # states in the cities
    place.py # places in states
    review.py # review and feadback
    amenity.py 


