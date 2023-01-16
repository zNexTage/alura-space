from django.db import models

# Create your models here.
class Photography(models.Model):
    class Meta:
        verbose_name = 'Fotografia'
        verbose_name_plural = 'Fotografias'
    

    NEBULA = 1
    STAR = 2
    GALAXY = 3
    PLANET = 4

    CATEGORY_CHOICES = (
        (NEBULA, 'Nebulosa'),
        (STAR, 'Estrela'),
        (GALAXY, 'Galáxia'),
        (PLANET, 'Planeta'),
    )

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    name.verbose_name = 'Nome'

    legend = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    legend.verbose_name = 'Legenda'

    description = models.TextField(
        null=False,
        blank=False
    )
    description.verbose_name = 'Descrição'

    photo = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    photo.verbose_name = 'Foto'

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default=''
    )
    category.verbose_name = 'Categoria'

    def __str__(self) -> str:
        return f'Fotografia - @{self.name}'



