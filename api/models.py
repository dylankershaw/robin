from django.db import models



class Intent(models.Model):
    name = models.CharField(max_length=255)

    # TODO: use a Signal with the intent's name so it can be called with a generic Intent.trigger method
    # https://docs.djangoproject.com/en/2.1/topics/signals/

    def __str__(self):
        return self.name

class Phrase(models.Model):
  name = models.CharField(max_length=255)
  intent = models.ForeignKey(Intent, on_delete=models.CASCADE)

  def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255)
    sentiment_score = models.FloatField()

    def __str__(self):
        return self.name