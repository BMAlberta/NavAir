class Airport(object):

    def __init__(self, initial_data):
        self.icao = initial_data['icao']
        self.name = initial_data['name']
        self.type = initial_data['type']
        self.latitude = initial_data['latitude']
        self.longitude = initial_data['longitude']
        self.elevation = initial_data['elevation']
        self.continent = initial_data['continent']
        self.country = initial_data['country']
        self.region = initial_data['region']

    def __iter__(self):
        yield 'icao', self.icao
        yield 'name', self.name
        yield 'type', self.type
        yield 'latitude', self.latitude
        yield 'longitude', self.longitude
        yield 'elevation', self.elevation
        yield 'continent', self.continent
        yield 'country', self.country
        yield 'regiom', self.region