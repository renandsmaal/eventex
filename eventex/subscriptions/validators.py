from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF Deve conter apenas numeros', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF Deve conter 11 digitos', 'lenght')
