from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


# custom clearable file = c_c_f
class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'artworks/custom_widget_templates/c_c_f_input.html'
