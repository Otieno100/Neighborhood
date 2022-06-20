from django.test import testcases
from django.test import TestCase
from .models import Neighbourhood, Business, User



# Create your tests here.



class NeighbourhoodTestClass(TestCase):
    """
    Testing Neighborhood model 
    """

    def setUp(self):
        """Set up method"""
        self.chescourt = Neighbourhood(
            name='Chester Court', location='Nairobi', occupants_count=10)

    def test_instance(self):
        """Test instance"""
        self.admin = User(username='admin',
                          email='admin@test.com', password='admin')
        self.assertTrue(isinstance(self.chescourt, Neighbourhood))

    def test_create_neighborhood(self):
        """Test create_neighborhood"""
        self.chescourt.create_neighbourhood()
        neighborhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighborhood) > 0)

    def test_delete_neighborhood(self):
        """Test delete_neighborhood"""
        self.chescourt.create_neighbourhood()
        self.chescourt.delete_neighbourhood()
        neighborhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighborhood) == 0)

    def test_find_neighborhood(self):
        """Test find_neighborhood"""
        self.chescourt.create_neighborhood()
        neighborhood = Neighbourhood.objects.get(name='Nyali')
        self.assertTrue(neighborhood.name == 'Nyali')

    def test_update_neighborhood(self):
        """Test update_neighborhood"""
        self.chescourt.create_neighborhood()
        self.chescourt.update_neighborhood('Nyali', 'Mombasa', 10)
        neighborhood = Neighbourhood.objects.get(name='Nyali')
        self.assertTrue(neighborhood.name == 'Nyali')
        self.assertTrue(neighborhood.location == 'Mombasa')
        self.assertTrue(neighborhood.occupants_count == 15)

    def test_get_occupants_count(self):
        """Test get_occupants_count"""
        self.chescourt.create_neighborhood()
        neighborhood = Neighbourhood.objects.get(name='Nyali')
        self.assertTrue(neighborhood.get_occupants_count() == 15)

    def tearDown(self):
        """Tear down method"""
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()


class BusinessTestClass(TestCase):
    """  Testing Business model    """

    def setUp(self):
        """ set up method
        """
        self.business = Business(name='Utawala', email='utawala@gmail.com')

    def test_instance(self):
        """Test instance"""
        self.assertTrue(isinstance(self.business, Business))

     

    def test_create_business(self):
        """Test create_business"""
        self.business.create_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_business(self):
        """_ test delete_business
        """
        self.business.create_business()
        self.business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)

    def tearDown(self):
        """tear down to delete saved instances"""
        Business.objects.all().delete()

    def test_update_neighborhood(self):
        """_ test update_business
        """
        self.business.create_business()
        self.business.update_business('Ujamaa', 'ujamaa@palace.com')
        business = Business.objects.get(name='ujamaa')
        self.assertTrue(business.name == 'ujamaa')
        self.assertTrue(business.email == 'ujamaa@gmail.com')

    def test_find_business(self):
        """Test find_neighborhood"""
        self.business.create_business()
        business = Business.objects.get(name='ujamaa')
        self.assertTrue(business.name == 'ujamaa')