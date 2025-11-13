from django.db import models

    ## Trainer
    # name
    # age
    # level 
    # birthday DateField()

class Trainer(models.Model):
    name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False)
    level = models.IntegerField(null=False)
    birthday = models.DateField(null=True, blank=True)
    picture = models.ImageField(upload_to='trainer_pictures/', null=True,blank=True)

    def __str__(self):
        return self.name
    

class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('PS', 'Psíquico'),
        ('T', 'Tierra'),
        ('E', 'Eléctrico'),
        ('N', 'Normal'),
        ('V', 'Veneno'),
        ('H', 'Hielo'),
        ('P', 'Planta'),
        ('L', 'Lagartija'),

    }
    type = models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    picture = models.ImageField(upload_to='pokemon_pictures/', null=True,blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
