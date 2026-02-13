from django.forms import ModelForm
from .models import Book
from django.core.exceptions import ValidationError
from datetime import date


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "year", "category", ]
    
    def clean_year(self):
        year = self.cleaned_data['year']

        if year > date.today().year:
            raise ValidationError('The year published cannot be in the future.')

        if year < 1440:
            raise ValidationError('The printing press was not invented until 1440.')

        return year
    
    def clean_category(self):
        category = self.cleaned_data.get("category")

        if category == "horror":
            raise ValidationError("Category cannot be that scary. Smile!")

        return category
    
    def save(self, commit=True):
        book = super().save(commit=False)
        book.title = book.title.title()
        book.published_date = date.today()

        if commit:
            book.save()
        
        return book