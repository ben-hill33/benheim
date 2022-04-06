# Django CRUD and Forms

## [Django Forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)

Working with forms can be complicated. Developers need to:
- Write HTML for the form
- Validate and properly sanitize entered data on the server (possibly the browser too)
- Repost the form with error messages to inform users of any invalid fields
- Handle the data when it has successfully been submitted
- And respond to the user in some way to indicate success

Django forms takes a lot of work out of all tehse steps, by providing a framework that lets you define forms and their fields programmatically, and then use these objects to both generate the form HTML code and handle much of the validation and user interaction.

### [HTML Forms](https://developer.mozilla.org/en-US/docs/Learn/Forms)
The article for Django Forms introduces a simple HTML form with a single text field for entering the name a team. 
```
<form action="/team_name_url/" method="post">
    <label for="team_name">Enter name: </label>
    <input id="team_name" type="text" name="name_field" value="Default name for team.">
    <input type="submit" value="OK">
</form>
```
- The field's `type` attribute defines what sort of widget will be displayed
- The `name` and `id` of the field are sued to identify the field in JS/CSS/HTML
- The `value` defines the initial value for the field when it is first displayed
- The matching team label is specified using the `label` tag
  - `label` utilizes a `for` field containing the `id` value of the associated `input`
- The `submit` input will be displayed as a button by default, that can be pressed by the user to upload the data in all the other input elements in the form to the server (`team_name`)

The form attributes define the HTTP `method` used to send the data and the destination of the data on the server (`action`)
- `action`: The resource/URL where data is to be sent for processing when the form is submitted
  - If not set, even to an empty string, the form will be submitted back to the current page URL
- `method`: The HTTP method used to send the data: _post_ or _get_
  - The `POST` method should always be used if the data is going to result in a change to the server's database as this can be made more resistant to cross-site forgery request attacks
  - The `GET` method should only be used for forms that don't change user data (like a search form). It's recommended for when you want to be able to bookmark or share the URL

The server's role is first to render the initial form state with blank fields or pre-populated with initial values
- After the user presses the submit button, the server will receive the form data with values from the browser and must validate the information
- If the form has invalid data, the server should display the form again, this time with user-entered data in "valid" fields and messages to describe the problem for the invalid fields
- Once server gets a request with valid form data, it can perform an appropriate action like saving, returning result of a search, upload a file, etc. And then notify the user

### Django Form Handling Process

For displaying information about models:
- The view gets a request
- Performs actions required including reading data from models
- Generates and returns an HTML page from a template, into which we pass a _context_ containing the data to be displayed. 
- The server needs to be able to process data provided by the user, and redisplay the page if there are any errors.

_The main things that Django's form handling does are_:
- Display the default form the first time it is requested by the user
  - The form may contain blank fields if you're creating a new record, or it may be pre-populated with initial values (like changing a record, or default initial values)
  - The form is referred to as _unbound_ at this point because it isn't associated with any user-entered data
- Receive data from a submit request and bind it to the form
  - _Binding_ data to the form means that the user-entered data and any errors are available when we need to redisplay the form
- Clean and validate the data
  - _Cleaning_ performs sanitization of the input (removing invalid characters that might be used to send malicious content to the server) and converts them into consistent Python types
  - _Validation_ checks that the values are appropriate for the field (correct date range, aren't too short or too long kind of thing)
- If any data is invalid, re-display the form, this time with any user populated values and error messages for the problem fields
- If all data is valid, perform required actions (save data, send email, return result, etc)
- Open all actions are complete, redirect the user to another page

Django comes with a built in class method `Form`, which simplifies both generation of form HTML and data cleaning/validation

### Form
The Django `Form` specifies the fields, layout, display widgets, labels, initial values, valid values, once validated will display error messages.

It also provides methods for rendering itself in templates using predefined formats (tables, lists) or getting the value of any element
```
from django import forms

class ThingForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
```

Check out other built in field classes [here](https://docs.djangoproject.com/en/3.1/ref/forms/fields/#built-in-field-classes)

Common field arguments:
- `required`: If True, the field may not be left blank or given a None value. Fields are required by default, so you would set required=False to allow blank values in the form.
- `label`: The label to use when rendering the field in HTML. If a label is not specified, Django will create one from the field name by capitalizing the first letter and replacing underscores with spaces (e.g. Renewal date).
- `label_suffix`: By default, a colon is displayed after the label (e.g. Renewal date:). This argument allows you to specify a different suffix containing other character(s).
- `initial`: The initial value for the field when the form is displayed.
- `widget`: The display widget to use.
- `help_text`: Additional text that can be displayed in forms to explain how to use the field.
- `error_messages`: A list of error messages for the field. You can override these with your own messages if needed.
- `validators`: A list of functions that will be called on the field when it is validated.
- `localize`: Enables the localization of form data input (see link for more information).
- `disabled`: The field is displayed but its value cannot be edited if this is True. The default is False.

### Other Resources
- [Django Templates](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page)
- [Django Views](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)

 (../index.md)
