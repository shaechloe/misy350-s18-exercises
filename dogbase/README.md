# This is Shae Muller's DogBase Application Markdown files

The DogBase database will contain two tables. The first table is for Dog Groups and the second table is for Dog Breeds. Dog Groups and Dog Breeds are linked together with strong referential integrity through Group Name. The tables have a one to many relationship -- one group can have many breeds but one breed can not have many groups.

The fields in the Group table will be: GroupID, Group Name and About. The fields in the Breed table will be: BreedID, Breed Name, Size, Color, and About. The primary key in the Group table is GroupID and the primary key in the Breed table is BreedID. Displayed below are the two tables and their contents.

## Group Table:

Group ID |     Group Name   | About
---------|------------------|-----------------------------------
1        |  Terrier Group   |The geography of the specific area (water, rocky terrain) helped to determine the exact duties of each breed, but it usually involved hunting vermin and varmints ranging from rats to badgers to otters and more.
2        |  Sporting Group  |While a number of these breeds perform more than one task, it is generally the duty of pointers and setters to point and mark game; for spaniels to flush game; and for retrievers to recover dead and wounded game.





## Car Table  :

GroupID | Group Name | Model | Car Type | Year | Description
------| -------------| --------|------|----------|---------|
1 | BMW |  M6 | Coupe | 2015 | One of BMWs best performance cars.
2 | Mercedes | S Class | Sedan | 2013 | The ultimate Mercedes in terms of luxury.
3 | Tesla |Model 3 | Electric | 2018 | The worlds first premium electric car under $40,000.



## To Run the Application

### Install necessary virtual environment file:

  *$ virtualenv venv*

### Activate the virtual environment:

  *$ source venv/bin/activate*

### Install necessary packages

  *$ pip install -r requirements.txt*

### Initialize the database

  *$ python manage.py deploy*

### Run the development server with the debugger on

  *$ python manage.py runserver -d*




Make sure to use Python version 2.7.x.

Install `virtualenv` if needed.

If you do not have a virtual environment yet on the project folder, set it up with:

    $ virtualenv venv

Then activate the virtual environment

    $ source venv/bin/activate

Install packages

    $ pip install -r requirements.txt

To initialize the database:

    $ python manage.py deploy

To run the development server (use `-d` to enable debugger and reloader):

    $ python manage.py runserver -d
