from django.forms import ModelForm

from .models import Bookmark

class BookmarkForm(ModelForm):
    # class meta must be present in each model class, it links models together.
    class Meta:
        model = Bookmark
        # using exclude you can leave out thing you dont want clients to touch.
        exclude = ('date_created', 'date_updated', 'owner')