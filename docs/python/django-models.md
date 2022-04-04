# Django Models

## [Using Models](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)
Models are usually defined in an applications `models.py` file. They are implemented as sublclasses of `django.db.models.Model`, and can include fields, methods and metadata. 

When designing your models it makes sense to have separate mdoels for every "object" or group of related information.

You might also want to use models to represent selection-list options (e.g. like a drop down list of choices), rather than hard coding the choices into the website itself — this is recommended when all the options aren't known up front or may change.
The code fragment below shows a "typical" model, named MyModelName:
```
from django.db import models

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name
```

### Fields
A model can have an arbitrary number of fields, of any type. Each one represents a column of data that we want to store in one of our database tables. Each database record (row) will consist of one of each field value.

The field name is used to refer to it in queries and templates. Fields also have a label specified as an argument (verbose_name), the default value of which is `None`, meaning replacing any underscores in the field name with a space.

### Metadata
You can declare model-level metadata for your Model by declaring `class Meta`:
```
class Meta:
    ordering = ['-my_field_name']
```
One of the most useful features of this metadata is to control the _default ordering_ of records returned when you query the model type. 
- You do this by specifying the match order in a list of field names to the `ordering` attribute
- The ordering will depend on the type of field
  - Character fields are sorted alphabetically, while date fields are sorted chronologically
- You can prefix the name with a minus symbol (-) to reverse the order

### Methods
Minimally, in every model you should define the standard Python class method `__str__()` to return a human-readable string for each object. 
- Another absolute method to include is `get_absolute_url()`, which returns a URL for displaying individual model records on the website
  - Defining this method will have Django automatically add a "View on Site" button to the model's record editing screens in the Admin site

A typical pattern for `get_absolute_url()`:
```
def get_absolute_url(self):
    """Returns the url to access a particular instance of the model."""
    return reverse('model-detail-view', args=[str(self.id)])
```

### Creating and modifying records
Once you've defined your model classes you can use them to create, update, or delete records. Or to run queries to get all records or particular subsets of records.

To create a record you can define an instance of the model and then call `save()`
```
# Create a new record using the model's constructor.
record = MyModelName(my_field_name="Instance #1")

# Save the object into the database.
record.save()
```
If you haven't declared any field as a `primary_key`, the new record will be given one automatically, with the field name `id`.
- You can access the fields in this new record uisng the dot syntax, and change the values. 
- You have to call `save()` to store modified values to the database.
```
# Access model field values using Python attributes.
print(record.id) # should return 1 for the first record.
print(record.my_field_name) # should print 'Instance #1'

# Change record by modifying the fields, then calling save().
record.my_field_name = "New Instance Name"
record.save()
```

### Searching for records
You can search for records that match certain criteria using the model's `objects` attribute.
- You can get all records for a model as a `QuerySet`, using `objects.all()`

The `filter()` method allows us to filter the returned `QuerySet` to match a specified text or numeric field against a particular criteria
- variable = Class.objects.filter(title__contains='stuff')

In some cases you'll need to filter on a field that defines a one-to-many relationship to another model or `ForeignKey`. 

After creating the models, re-run your database migrations to add them to your database.
```
python3 manage.py makemigrations
python3 manage.py migrate
```

## [Django Admin](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site)
The Django admin _application_ can use your models to automatically build a site area that you can use to create, view, update, and delete records. This can save you a lot of time during development, making it easier to test your models and get a feel for whether you have the _right_ data. 
- Admin can also be useful for managing data in production, though it's recommended only for internal data management.

All the configuration to run the admin site was done automatically when you created your project. All you have to do to add your models to the admin app is to _register_ them

### Registering models
- Open `admin.py`
- Add `admin.site.register(ModelClassName)` for howevery many model classes you need to register

### Create a superuser
In your `manage.py` file call the following command
```
python manage.py createsuperuser
```
- Once this command completes a new superuser will have been added to the database. 
- Restart the server and test the login by running
```
python manage.py runserver
```

### Logging in and using the site
To login to the site,
- Open /admin URL and enter your new superuser id and password credentials
  - You'll be redirected to the login page, then back to /admin
- Click on the **Add** link to the right of the model class name to create a new record. 


[Table of Contents](../index.md)
