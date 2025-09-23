# 代码生成时间: 2025-09-23 23:20:24
import gr

class FormValidator:
    def __init__(self):
        """Initialize the form validator."""
        self.required_fields = []  # Fields that are required
        self.validation_rules = {}  # Custom validation rules for fields

    def add_required_field(self, field_name):
        """Add a field to the list of required fields."""
        self.required_fields.append(field_name)

    def add_validation_rule(self, field_name, validation_func):
        """Add a custom validation rule for a field.

        Args:
            field_name (str): The name of the field.
            validation_func (function): A function that takes the field value and returns a boolean indicating if the field is valid.
        """
        self.validation_rules[field_name] = validation_func

    def validate(self, form_data):
        """Validate the provided form data.

        Args:
            form_data (dict): A dictionary containing the form data.

        Returns:
            tuple: A tuple containing a boolean indicating if the form data is valid and a list of error messages.
        """
        is_valid = True
        error_messages = []

        # Check for required fields
        for field in self.required_fields:
            if field not in form_data or not form_data[field]:
                error_messages.append(f"The field '{field}' is required.")
                is_valid = False

        # Check for custom validation rules
        for field, validation_func in self.validation_rules.items():
            if field in form_data and not validation_func(form_data[field]):
                error_messages.append(f"The field '{field}' is invalid.")
                is_valid = False

        return is_valid, error_messages

# Example usage
if __name__ == '__main__':
    # Create a form validator instance
    validator = FormValidator()
    
    # Add required fields
    validator.add_required_field('name')
    validator.add_required_field('email')
    
    # Add custom validation rules
    validator.add_validation_rule('email', lambda x: '@' in x)
    
    # Sample form data
    form_data = {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
    }
    
    # Validate the form data
    is_valid, errors = validator.validate(form_data)
    
    # Print the validation result
    if is_valid:
        print('Form data is valid.')
    else:
        print('Form data is invalid:')
        for error in errors:
            print(error)