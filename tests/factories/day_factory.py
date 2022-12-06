import factory


from alaapp.models.day import Day

class MondayDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Day
        
    id=1
    name='Lunes'


class TuesdayDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Day
        
    id=2
    name='Martes'