import factory

from alaapp.models.time_restriction import TimeRestriction

class TimeRestrictionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TimeRestriction
    id=1
    name='test_tr'
    date_from='2022-10-10'
    date_to='2022-10-12'
    hour_from='00:00'
    hour_to='23:59'

class OtherTimeRestrictionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TimeRestriction
    id=2
    name='other_test_tr'
    date_from='2022-10-12'
    date_to='2022-11-12'
    hour_from='16:00'
    hour_to='23:59'
   