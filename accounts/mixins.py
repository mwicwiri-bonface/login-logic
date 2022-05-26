from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm


class StylingFormMixin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(StylingFormMixin, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
