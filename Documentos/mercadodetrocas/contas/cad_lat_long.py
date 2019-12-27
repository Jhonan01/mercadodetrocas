from opencage.geocoder import OpenCageGeocode
import math

class Local():

    def distancia():

        key = '6940adf71cd14d6697323d05946d7388'

        geocoder = OpenCageGeocode(key)

        query = ("rua presidente kenney. itanhem, bahia, brasil")


     #   query2 = "rua tiradentes, itanhem, bahia, brasil"

        result = geocoder.geocode(query)

       # result2 = geocoder.geocode(query2)

        lat_1 = result[0]['geometry']['lat']
        long_1 = result[0]['geometry']['lng']



 #       lat_2 = result2[0]['geometry']['lat']
  #      long_2 = result2[0]['geometry']['lng']

   #     dist = 6371 * math.acos(math.cos(math.radians(lat_1)) * math.cos(math.radians(lat_2)) * math.cos(math.radians(long_2) - math.radians(long_1)) + math.sin(math.radians(lat_1)) * math.sin(math.radians(lat_2)))

        #lat_1 = 1
       # long_1 = 1

        result = (lat_1 , long_1)

        return result
