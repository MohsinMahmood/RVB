from django.db import models

# Create your models here.

class Manager(models.Model):
    ID = models.CharField(primary_key=True,max_length=20)
    OwnerID = models.CharField(max_length=20, default='00000')
    TeamLeaderID = models.CharField(max_length=20, default='00000')
    Name = models.CharField(max_length=25)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Address = models.TextField()
    
    def __str__(self):
        return self.Name

class Roles(models.Model):
    ID = models.CharField(primary_key=True,max_length=20,default='00000')
    Name = models.CharField(max_length=25)
    Description = models.TextField()

    def __str__(self):
        return self.Name

class Property(models.Model):
    ID = models.CharField(primary_key=True,max_length=20)
    Name = models.CharField(max_length=25)
    Description = models.TextField()
    ShowAddress = models.BooleanField()
    Availability = models.BooleanField()
    ManagerID= models.ForeignKey(Manager,default='00000')

class Badges(models.Model):
    Description = models.TextField()
    PropertyID= models.ForeignKey(Property,default='00000')
    
    def __str__(self):
        return self.PropertyID

class Channel(models.Model):
    ID = models.CharField(primary_key=True,max_length=20,default='00000')
    ChannelName = models.CharField(max_length=20)
    ChannelLink = models.URLField()
    Status = models.BooleanField()
    ManagerID= models.ForeignKey(Manager,default='00000')
    
    def __str__(self):
        return self.ChannelName

class ContactInformation(models.Model):
    ID = models.CharField(primary_key=True,max_length=20,default='00000')
    DefaultInformation = models.BooleanField()
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    SpokenLanguages = models.TextField()
    ExistingWebsite = models.URLField()
    Status = models.CharField(max_length=3)
    CreationDate = models.DateTimeField()
    PropertyID= models.ForeignKey(Property,default='00000')

class Location(models.Model):
    Country = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    PostalCode=models.CharField(max_length=25)
    Address = models.TextField()
    Latitude = models.CharField(max_length=40)
    Longitude = models.CharField(max_length=40)
    PropertyID= models.ForeignKey(Property,default='00000')
    
    def __str__(self):
        return self.Country

class Distances(models.Model):
    UnitType = models.CharField(max_length=10)
    ByBus = models.CharField(max_length=50)
    ByUnderground = models.CharField(max_length=50)
    ByMotorway = models.CharField(max_length=50)
    ByTrain = models.CharField(max_length=50)
    ByAirport = models.CharField(max_length=50)
    ByPort = models.CharField(max_length=50)
    PropertyID= models.ForeignKey(Property,default='00000')
    
    def __str__(self):
        return self.Country

class Login(models.Model):
    ID = models.CharField(primary_key=True,max_length=15,default='00000')
    UserName = models.CharField(max_length=20)
    Password = models.CharField(max_length=50)
    RoleID= models.ForeignKey(Roles,default='00000')
    
    def __str__(self):
        return self.UserName

class Registrations(models.Model):
    ID = models.CharField(max_length=15, primary_key=True)
    Name = models.CharField(max_length=20)
    Type = models.CharField(max_length=10)
    Description = models.TextField()
    StartDate = models.DateTimeField()
    Duration = models.CharField(max_length=20)
    PropertyID= models.ForeignKey(Property,default='00000')
    
    def __str__(self):
        return self.Name

class AddOnes(models.Model):
    ID = models.CharField(primary_key=True,max_length=20,default='00000')
    Name = models.CharField(max_length=20)
    Pricing = models.CharField(max_length=50)
    Restrictions = models.TextField()
    Status = models.BooleanField()
    PropertyID= models.ForeignKey(Property,default='00000')
    
    def __str__(self):
        return self.Name

class ExternalCertificates(models.Model):
    ID = models.CharField(primary_key=True,max_length=20,default='00000')
    Name = models.CharField(max_length=20)
    PropertyID= models.ForeignKey(Property,default='00000')
    
    def __str__(self):
        return self.Name

class Gallery(models.Model):
    ID = models.CharField(primary_key=True,max_length=20)
    Name = models.CharField(max_length=25)
    ImageFile = models.ImageField()

    def __str__(self):
        return self.Name

class Rents(models.Model):
    ID = models.CharField(primary_key=True,max_length=20)
    StartDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    Rate = models.CharField(max_length=50)
    BookAbility = models.CharField(max_length=10)
    PolicyType = models.CharField(max_length=20)
    ExtraCharge = models.CharField(max_length=50)
    SeasonType = models.CharField(max_length=30)
    CurrencyType = models.CharField(max_length=30)
    RentType = models.CharField(max_length=30)
    Notes = models.TextField()
    PropertyID= models.ForeignKey(Property,default='00000')


    def __str__(self):
        return self.ID

class Reviews(models.Model):
    ID = models.CharField(primary_key=True,max_length=20,default='00000')
    ReviewSources = models.TextField()
    ReviewStatus = models.CharField(max_length=20)
    PropertyID= models.ForeignKey(Property,default='00000')

    def __str__(self):
        return self.ID

class G_R_P_R(models.Model):
    PropertyID= models.ForeignKey(Property,default='00000')
    ReviewsID= models.ForeignKey(Reviews,default='00000')
    RentsID= models.ForeignKey(Rents,default='00000')
    GalleryID= models.ForeignKey(Gallery,default='00000')
    
    def __str__(self):
        return self.PropertyID

class Add_External(models.Model):
    AddOnsID= models.ForeignKey(AddOnes,default='00000')
    ExternalCertificatesID= models.ForeignKey(ExternalCertificates,default='00000')
    
    def __str__(self):
        return self.AddOnsID

class M_B_R_C_R_L(models.Model):
    BadgesID= models.ForeignKey(Badges,default='00000')
    ManagerID= models.ForeignKey(Manager,default='00000')
    RegistrationsID= models.ForeignKey(Registrations,default='00000')
    ContactInformationID= models.ForeignKey(ContactInformation,default='00000')
    RolesID= models.ForeignKey(Roles,default='00000')
    LoginID= models.ForeignKey(Login,default='00000')
 
    def __str__(self):
        return self.ManagerID

class L_C(models.Model):
    LoginID= models.ForeignKey(Login,default='00000')
    ChannelID= models.ForeignKey(Channel,default='00000')

    def __str__(self):
        return self.ChannelID

class P_E_R(models.Model):
    PropertyID= models.ForeignKey(Property,default='00000')
    RegistrationsID= models.ForeignKey(Registrations,default='00000')
    ExternalCertificatesID= models.ForeignKey(ExternalCertificates,default='00000')
   
    def __str__(self):
        return self.ChannelID

class P_D_L(models.Model):
    PropertyID= models.ForeignKey(Property,default='00000')
    DistancesID= models.ForeignKey(Distances,default='00000')
    LocationID= models.ForeignKey(Location,default='00000')

   
    def __str__(self):
        return self.PropertyID


















    
    




    

