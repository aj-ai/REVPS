"""
Prereq: City is input into program.
Returns: Longitude, Latitude of the center of the city.
Directions API Key: AIzaSyDHjW3OCWmIKYksFb01CTOPiG4hdGSQT6g
"""

from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3

""" IMPORTANT: If you call both address_to_latlong and then call
    latlong_to_address on the same pair, then you will end up with
    a slightly different address. Thus, for the sake of consumer side
    support, on the website, restate the original input address.
    
    """
class CoordinateConvert:

    def __init__(self, address):
        self.address= address

    def getAddress(self):
        
   
        return self.inputAddress

    # def getCity():
        

    #     return self.inputCity

    def address_to_latlong(self,inpAddress, city):
        
        """ Input: address as a string
            Returns: Latitude, Longitude as a single concatenated string
                     separated by ", " """
        

        geolocator = GoogleV3(format_string = "%s, " + city )
        self.address, (latitude, longitude) = geolocator.geocode(self.inpAddress)
        
        return (str(latitude) + ", " + str(longitude))


    def latlong_to_address(self,latlng):
        
        """ Input: Latitude, Longitude as concatenated string with ", " separating the two
            Returns: Address as a single string"""
            
        geolocator = Nominatim()
        location = geolocator.reverse(latlng)
        
        return(location.address)
    def Main(self):
        self.theAddress = self.inpAddress[0]
        self.theCity = self.inpAddress[1]
        print(address_to_latlong(self.theAddress, self.theCity))
        print(latlong_to_address(address_to_latlong(self.theAddress, self.theCity)))
Main()
