from django.db import models
from django.utils import timezone

# Create your models here.

class Post( models.Model ) :
	author         = models.ForeignKey( 'auth.User')
	title  		   = models.CharField( max_length = 200 )
	text           = models.TextField()
	created_date   = models.DateTimeField( default=timezone.now )
	published_date = models.DateTimeField( blank=True, null=True )

	def publish( self ) :
		self.published_date = timezone.now()
		self.save()

	def __str__( self ) :
		return self.title		

class Animal( models.Model ) :
	FELINO = 'F'
	CANINO = 'C'
	REPTIL = 'R'

	CLASSES = (
				( FELINO, 'Felino' ),
				( CANINO, 'Canino' ),
				( REPTIL, 'Réptil' )
			  )

	PEQUENO = 'P'
	MEDIO   = 'M'
	GRANDE  = 'G'
	PORTES  = ( 
				( PEQUENO, 'Pequeno' ),
				( MEDIO,   'Médio' ),
				( GRANDE,  'Grande' )
			  )

	dono   = models.ForeignKey( 'auth.User')
	genero = models.CharField( max_length = 1, choices = CLASSES )
	raca   = models.CharField( max_length = 20 )
	cor    = models.CharField( max_length = 20 )
	porte  = models.CharField( max_length = 1, choices = PORTES )