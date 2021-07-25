# from django.test import TestCase
# from api.models import *
# from .serializers import *
# from shapely.geometry import Point
# from shapely.geometry.polygon import Polygon

# class ProviderTestCase(TestCase):
#     def setUp(self):
#         provider_obj = Provider.objects.create(name= "Abhi123", email= "abhi@abhi.abhi", phone= 3645368538, language= "English", currency= "INR")
#         ServiceArea.objects.create(name="PolyTest", coordinates="[[34.545451, 40.169158], [36.953492, 70.169158], [34.953510, 60.170104], [34.950958, 70.169990]]", provider= provider_obj)

#     def test_provider_details(self):
#         """Get the details of provider with name 'Abhi123'."""
#         provider = Provider.objects.get(name="Abhi123")
#         serializer = ProviderSerializer(provider, many=False)
#         self.assertEqual(serializer.data, "{'id': 1, 'name': 'Abhi123', 'email': 'abhi@abhi.abhi', 'phone': 3645368538, 'language': 'English', 'currency': 'INR'}")

#     def test_polygon_details(self):
#         """Get the details of geopolygon created"""
#         geo_polygon = ServiceArea.objects.get(name="PolyTest")
#         serializer = ServiceAreaSerializer(geo_polygon, many=False)       
#         self.assertEqual(serializer.data, "{'id':1,'name:'PolyTest', 'coordinates':'[[34.545451, 40.169158], [36.953492, 70.169158], [34.953510, 60.170104], [34.950958, 70.169990]]', 'provider':'Abhi123'}")


    
#     def test_query(self):
#         point = Point(24.952242,60.1696017)
#         poly_objects = ServiceArea.objects.first()
#         eval_poly_coord = eval(poly_objects)
#         polygon = Polygon(eval_poly_coord)
#         if polygon.contains(point):
#             print("success")