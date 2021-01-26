from django.db import models

class Bases(models.Model):
    codi = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length = 180)

    def __str__(self):
        return self.nom


class Consultes(models.Model):
    codi = models.IntegerField(primary_key=True)
    pregunta = models.TextField()
    pista = models.TextField()
    base_id = models.ForeignKey(Bases, on_delete=models.CASCADE)

    def __str__(self):
        return self.pregunta

class Respostes(models.Model):
    codi = models.IntegerField(primary_key=True)
    resposta = models.TextField()
    
    def __str__(self):
        return self.resposta

class Solucions(models.Model):
    codi_pregunta = models.ForeignKey(Consultes, on_delete=models.CASCADE)
    codi_resposta = models.ForeignKey(Respostes, on_delete=models.CASCADE)