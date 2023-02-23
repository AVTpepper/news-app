# from .models import Comment
# from django import forms


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('body',)

# from cloudinary.forms import CloudinaryJsFileField
# from django.forms import ModelForm
# from cloudinary.forms import CloudinaryFileField
# from .models import Photo, Post


# class PhotoForm(ModelForm):
#     image = CloudinaryJsFileField(attrs={'accept': 'image/*'})
#     # image_thumbnail = CloudinaryUnsignedJsFileField(
#     #     attrs={'accept': 'image/*', 'style': 'display:none;'}
#     # )

#     class Meta:
#         model = Photo
#         fields = ['image']
