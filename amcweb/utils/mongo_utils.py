from mongoengine import *

from .. import models


def next_count(counter_name='Patients', incr_by=1):
    """
    Updates the counter value by incr_by and returns the new value.
    :param counter_name: Counter name to get the value from.
    :param incr_by: Step to increment.
    :return: Returns the updated counter value
    """
    return models.Counter.objects(name=counter_name).modify(upsert=True, new=True, inc__count=incr_by).count
