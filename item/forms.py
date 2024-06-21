from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition duration-300 ease-in-out'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES + ' appearance-none bg-white text-gray-700 hover:bg-gray-100'
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES + ' bg-white text-gray-700 hover:bg-gray-100'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES + ' resize-none bg-white text-gray-700 hover:bg-gray-100'
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES + ' bg-white text-gray-700 hover:bg-gray-100'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES + ' bg-white text-gray-700 hover:bg-gray-100'
            })
        }





class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }