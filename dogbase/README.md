# This is Shae Muller's DogBase Application Markdown files

The DogBase database will contain two tables. The first table is for Dog Groups and the second table is for Dog Breeds. Dog Groups and Dog Breeds are linked together with strong referential integrity through Group Name. The tables have a one to many relationship -- one group can have many breeds but one breed can not have many groups.

The fields in the Group table will be: Group ID, Group Name and About. The fields in the Breed table will be: Breed ID, Breed Name, Size, Color,  Description and Group name from the Group table. The primary key in the Group table is GroupID and the primary key in the Breed table is BreedID. Displayed below are the two tables and their contents.

## Group Table:

Group ID |     Group Name   | About
---------|------------------|-----------------------------------
1        |  Terrier Group |The geography of the specific area (water, rocky terrain) helped to determine the exact duties of each breed, but it usually involved hunting vermin and varmints ranging from rats to badgers to otters and more.
2        |  Working Group |While the uses and appearances of the dogs in the Working Group vary, most are powerfully built and intelligent, performing various tasks for their people.
3        |  Sporting Group |While a number of these breeds perform more than one task, it is generally the duty of pointers and setters to point and mark game; for spaniels to flush game; and for retrievers to recover dead and wounded game.
4        |  Toy Group |Toy dogs have been around for centuries, and are bred for one purpose: to be companions for their humans.
5        |  Non-Sporting Group |Today, the Non-Sporting Group is literally every breed that is left, resulting in a wide variety of sizes, shapes, hair, function and history.
6        | Hound Group |Most of these breeds were developed to hunt somewhat independently for their humans, who usually followed on foot or on horseback as the hounds chased down the prey.
7        | Herding Group |Herding is a natural instinct in dogs that is seen in the wild. Humans have used that instinct to their advantage on farms and ranches with herding dogs who have the sole purpose of gathering and moving livestock from one place to another.


## Breed Table  :

Breed ID | Breed Name | Size | Color | Description | Group Name
------| -------------| --------|------|----------|---------|
1 | Dandie Dinmont Terrier |  Small | Mustard or Pepper | The unique looking Dandie Dinmont Terrier is a tough but dignified little exterminator. Sturdily built for the rigors of farm life, they will agreeably adapt to city living. Dandies are compact companions blessed with a big personality. | Terrier Group
2 | Dogue de Bordeaux |  Extra Large | Fawn, Isabella, Mahogany, or Red | The most ancient of French dog breeds, the Dogue de Bordeaux ('Mastiff of Bordeaux') was around even before France was France. These brawny fawn-coated guardians of considerable courage are famously loyal, affectionate, and protective. | Working Group
3 | English Setter|  Medium | Black and White| The English Setter is a medium sized sporting dog of sweet temper and show stopping good looks. It is one of the AKCs four British setters created to work on the distinctly different terrains of England, Ireland, and Scotland.| Sporting Group
4 | Papillon |  Extra Small |White and Black, Lemon, Red, Sable, or Tan| The quick, curious Papillon is a toy dog of singular beauty and upbeat athleticism. Despite his refined appearance, the Pap is truly a 'doggy dog' blessed with a hardy constitution. Papillon fanciers describe their breed as happy, alert, and friendly.| Toy Group
5 | Dalmatian|  Medium | Black and White | The dignified Dalmatian, dogdom's citizen of the world, is famed for his spotted coat and unique job description. During their long history, these coach dogs have accompanied the horse-drawn rigs of nobles, gypsies, and firefighters. | Non-Sporting Group
6 | American Foxhound |  Medium| American Foxhounds are good-natured, low-maintenance hounds who get on well with kids, dogs, even cats, but come with special considerations for prospective owners. They are closely associated with Revolutionary heroes and the rolling estates of old Virginia. | Hound Group
7 | Border Collie |  Medium | Wide Range and Mix of Colors |A remarkably bright workaholic, the Border Collie is an amazing dog..maybe a bit too amazing for owners without the time, energy, or means to keep it occupied. These energetic dogs will settle down for cuddle time when the workday is done. | Herding Group


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
