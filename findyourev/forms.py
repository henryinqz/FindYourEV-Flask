from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, SubmitField, FloatField, BooleanField, ValidationError
from wtforms.validators import InputRequired, NumberRange

# import findyourev.data
from findyourev.data import brands, drivetrains, form_factors, ev_types, prices, years, powers, range_capacities
from findyourev.constants import *

# Equivalents of wtforms.validators.EqualTo()
class LessThanEqualTo(object):
    """
    Compares the values of two fields.

    :param fieldname:
        The name of the other field to compare to.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated with `%(other_label)s` and `%(other_name)s` to provide a
        more helpful error.
    """
    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext("Invalid field name '%s'.") % self.fieldname)
        if field.data > other.data:  #  --> Change to > from !=
            d = {
                'other_label': hasattr(other, 'label') and other.label.text or self.fieldname,
                'other_name': self.fieldname
            }
            message = self.message
            if message is None:
                message = field.gettext('Field must be less than or equal to %(other_name)s.')

            raise ValidationError(message % d)
class GreaterThanEqualTo(object):
    """
    Compares the values of two fields.

    :param fieldname:
        The name of the other field to compare to.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated with `%(other_label)s` and `%(other_name)s` to provide a
        more helpful error.
    """
    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext("Invalid field name '%s'.") % self.fieldname)
        if field.data < other.data:  #  --> Change to < from !=
            d = {
                'other_label': hasattr(other, 'label') and other.label.text or self.fieldname,
                'other_name': self.fieldname
            }
            message = self.message
            if message is None:
                message = field.gettext('Field must be greater than or equal to %(other_name)s.')

            raise ValidationError(message % d)

class SearchForm(FlaskForm):
    # Brands
    brand = SelectMultipleField(
        "Brand", 
        choices = [(_, _) for _ in brands]
    )

    # Min/max price
    min_price = FloatField(
        "Min. Price",
        default=0,
        validators = [InputRequired(), LessThanEqualTo('max_price'), NumberRange(min=0)]
    )
    max_price = FloatField(
        "Max. Price", 
        default = prices[MAX_PRICE],
        validators = [InputRequired(), GreaterThanEqualTo('min_price'), NumberRange(min=0)]
    )

    # Min/max year
    min_year = FloatField(
        "Min. Year", 
        default=0,
        validators = [InputRequired(), LessThanEqualTo('max_year'), NumberRange(min=0)]
    )
    max_year = FloatField(
        "Max. Year", 
        default=years[MAX_YR],
        validators = [InputRequired(), GreaterThanEqualTo('min_year'), NumberRange(min=0)]
    )
    
    # Min/max range
    min_range = FloatField(
        "Min. Range", 
        default=0,
        validators = [InputRequired(), LessThanEqualTo('max_range'), NumberRange(min=0)]
    )
    max_range = FloatField(
        "Max. Range", 
        default=range_capacities[MAX_RANGE], 
        validators = [InputRequired(), GreaterThanEqualTo('min_range'), NumberRange(min=0)]
    )

    # Drivetrain
    drivetrain = SelectMultipleField(
        "Drivetrain",
        # choices = [(_, _) for _ in drivetrains]
        choices=[
            ("AWD", "All Wheel Drive (AWD)"), 
            ("RWD", "Rear Wheel Drive (RWD)"), 
            ("FWD", "Front Wheel Drive (FWD)")
        ]
    )

    # Form factor
    form_factor = SelectMultipleField(
        "Form Factor", 
        choices = [(_, _) for _ in form_factors]
        # choices=[
        #     ("Compact", "Compact"),
        #     ("Hatchback", "Hatchback"),
        #     ("Small", "Small"),
        #     ("Large", "Large"),
        #     ("Mid-size", "Mid-size"),
        #     ("Minivan", "Minivan"),
        #     ("Sedan", "Sedan"),
        #     ("Sport", "Sport"),
        #     ("Station Wagon", "Station Wagon"),
        #     ("Subcompact", "Subcompact"),
        #     ("SUV", "SUV")
        # ]
    )

    # EV Type
    ev_type = SelectMultipleField(
        "Electric Type", 
        # choices = [(_, _) for _ in ev_types]
        choices=[
            ("BEV", "Battery Electric Vehicle (BEV)"),
            ("PHEV", "Plug-in Hybrid Electric Vehicle (PHEV)"),
            ("HFCV", "Hydrogen Fuel Cell Vehicle (HFCV)")
        ]
    )

    # Min/max power (horsepower)
    min_power = FloatField(
        "Min. Power", 
        default=0,
        validators = [InputRequired(), LessThanEqualTo('max_power'), NumberRange(min=0)]
    )
    max_power = FloatField(
        "Max. Power", 
        default=powers[MAX_POWER], 
        validators = [InputRequired(), GreaterThanEqualTo('min_power'), NumberRange(min=0)]
    )

    submit = SubmitField("Search") # Submit button

