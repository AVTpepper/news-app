from cloudinary.forms import CloudinaryJsFileField


class PostForm(forms.ModelForm):
    image = CloudinaryJsFileField()
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']