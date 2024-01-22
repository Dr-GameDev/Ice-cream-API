from django.db import models

# Create your models here.

"""
models should contain type of ice-cream at a higher level
lower than should be the name, description of each ice-cream

    e.g => ::
    {name: "gelato", 
    description: {
        "origin": "Italy",
        "flavors": ["pistachio, stracciatella, hazelnut, fior di latte, nocciola (hazelnut), chocolate, vanilla, fruit flavors like lemon, strawberry, mango, raspberry."],
        "toppings": ["candied fruits, nuts, limoncello, amaretto, balsamic vinegar, olive oil, dried herbs, cinnamon, nutmeg, lavender, rose"],
        }, }
    
"""

class IceCream(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.JSONField(default=dict)

    def __str__(self):
        return self.name
