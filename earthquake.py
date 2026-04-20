class Earthquake():
    def __init__(self, depth, mag, lat, long, time):
        # depth: depth of the earthquake in km, downward from the surface, float
        # mag: magnitude of the earthquake, float
        #lat: -90 to 90 float,
        #long: -180 to 180 float,
        #time: dt.datetime object
        self.depth=depth
        self.mag=mag
        self.lat=lat
        self.long=long
        self.time=time

    def get_depth(self):return self.depth
    def get_mag(self):return self.mag
    def get_loc(self):return (self.lat,self.long)
    def get_time(self):return self.time

    def set_depth(self, new_depth):self.depth=new_depth
    def set_mag(self, new_mag):self.mag=new_mag
    def set_loc(self, new_lat, new_long):self.lat,self.long=new_lat, new_long
    def set_time(self, new_time):self.time=new_time




