from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute


class EarthquakeModel(Model):
    class Meta:
        table_name = "dynamodb-earthquake"
        host = "http://localhost:8000"

    title = UnicodeAttribute(hash_key=True)
    latitude = NumberAttribute(null=True)
    longitude = NumberAttribute(null=True)

    def __repr__(self):
        return f"EarthQuake {self.title}: {self.longitude}:{self.latitude}"
