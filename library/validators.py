from django.core.exceptions import ValidationError

def validate_blank(text):
    if len(text.strip()) == 0:
        raise ValidationError(
            ("text is not valid")
        )
    
#Validar que un resumen tenga al menos 20 caracteres
def validate_length(text):
    if len(text) < 20:
        raise ValidationError(
            ("text is too short")
        )
    
def validate_range(rating):
    if rating <= 0 or rating > 5:
        raise ValidationError(
            ("rating is not valid")
        )