from modeltranslation.translator import translator, TranslationOptions
from .models import Slider



class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Slider, SliderTranslationOptions)