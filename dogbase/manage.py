from flask_script import Manager
from dogbase import app, db, Group, Breed

manager = Manager(app)


# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    terrier = Group(name='Terrier Group', about='The geography of the specific area (water, rocky terrain) helped to determine the exact duties of each breed, but it usually involved hunting vermin and varmints ranging from rats to badgers to otters and more.')
    working = Group(name='Working Group', about='While the uses and appearances of the dogs in the Working Group vary, most are powerfully built and intelligent, performing various tasks for their people.')
    sporting = Group(name='Sporting Group', about='While a number of these breeds perform more than one task, it is generally the duty of pointers and setters to point and mark game; for spaniels to flush game; and for retrievers to recover dead and wounded game.')
    toy = Group(name='Toy Group', about='Toy dogs have been around for centuries, and are bred for one purpose: to be companions for their humans.')
    nonsport = Group(name='Non-Sporting Group', about='Today, the Non-Sporting Group is literally every breed that is left, resulting in a wide variety of sizes, shapes, hair, function and history.')
    hound = Group(name='Hound Group', about='Most of these breeds were developed to hunt somewhat independently for their humans, who usually followed on foot or on horseback as the hounds chased down the prey.')
    herding = Group(name='Herding Group', about='Herding is a natural instinct in dogs that is seen in the wild. Humans have used that instinct to their advantage on farms and ranches with herding dogs who have the sole purpose of gathering and moving livestock from one place to another.')


    breed1 = Breed(name='Dandie Dinmont Terrier', size='Small', color='Mustard or Pepper', description="The unique looking Dandie Dinmont Terrier is a tough but dignified little exterminator. Sturdily built for the rigors of farm life, they will agreeably adapt to city living. Dandies are compact companions blessed with a big personality.", group=terrier)
    breed2 = Breed(name='Dogue de Bordeaux', size='Extra Large', color='Fawn, Isabella, Mahogany, or Red', description="The most ancient of French dog breeds, the Dogue de Bordeaux ('Mastiff of Bordeaux') was around even before France was France. These brawny fawn-coated guardians of considerable courage are famously loyal, affectionate, and protective.", group=working)
    breed3 = Breed(name='English Setter', size='Medium', color='Black and White', description="The English Setter is a medium sized sporting dog of sweet temper and show stopping good looks. It is one of the AKCs four British setters created to work on the distinctly different terrains of England, Ireland, and Scotland.", group=sporting)
    breed4 = Breed(name='Papillon', size='Extra Small', color='White and Black, Lemon, Red, Sable, or Tan', description="The quick, curious Papillon is a toy dog of singular beauty and upbeat athleticism. Despite his refined appearance, the Pap is truly a 'doggy dog' blessed with a hardy constitution. Papillon fanciers describe their breed as happy, alert, and friendly.", group=toy)
    breed5 = Breed(name='Dalmatian', size='Medium', color='Black and White', description="The dignified Dalmatian, dogdom's citizen of the world, is famed for his spotted coat and unique job description. During their long history, these coach dogs have accompanied the horse-drawn rigs of nobles, gypsies, and firefighters.", group=nonsport)
    breed6 = Breed(name='American Foxhound', size='Medium', color='Black, White and Tan or White Black and Tan', description="American Foxhounds are good-natured, low-maintenance hounds who get on well with kids, dogs, even cats, but come with special considerations for prospective owners. They are closely associated with Revolutionary heroes and the rolling estates of old Virginia.", group=hound)
    breed7 = Breed(name='Border Collie', size='Medium', color='Wide Range and Mix of Colors', description="A remarkably bright workaholic, the Border Collie is an amazing dog..maybe a bit too amazing for owners without the time, energy, or means to keep it occupied. These energetic dogs will settle down for cuddle time when the workday is done.", group=herding)

    db.session.add(terrier)
    db.session.add(sporting)
    db.session.add(working)
    db.session.add(toy)
    db.session.add(nonsport)
    db.session.add(hound)
    db.session.add(herding)

    db.session.add(breed1)
    db.session.add(breed2)
    db.session.add(breed3)
    db.session.add(breed4)
    db.session.add(breed5)
    db.session.add(breed6)
    db.session.add(breed7)

    db.session.commit()


if __name__ == "__main__":
    manager.run()
