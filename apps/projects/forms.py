from django import forms
from apps.stddata.models import Country, Language
from apps.gcd.models import Publisher

PUBLISHERS = [[p.id, p.name]
               for p in Publisher.objects
                                 .filter(deleted=False)
                                 .order_by('name')]

SEVERAL_COVER_PUBLISHER_IDS = [1984, 1950, 196, 1082, 512, 1846, 890, 1163, 4475, 2020, 2549, 119, 745, 4807, 78, 1027, 6084, 2761, 5132, 3932, 5867, 2476, 6524, 7151, 3093, 1868, 4004, 525, 3371, 8162, 4589, 1974, 543, 4551, 2105, 2114, 4476, 3113, 138, 604, 613, 1847, 728, 52, 8886, 4677, 3947, 61, 4720, 2550, 809, 3336, 511, 549, 113, 3752, 1557, 764, 307, 2565, 7459, 895, 682, 3372, 4493, 2063, 445, 3591, 4473, 5732, 2547, 67, 709, 336, 659, 1977, 4604, 76, 379, 3123, 7018, 4999, 1197, 6229, 677, 946, 1901, 833, 279, 1954, 5987, 485, 3532, 1052, 3742, 1963, 3193, 382, 2216, 570, 869, 6889, 819, 3161, 1818, 769, 4508, 349, 3640, 7022, 4219, 828, 7093, 778, 715, 3032, 1513, 145, 32, 7460, 3097, 2001, 3197, 8997, 4058, 3009, 4738, 8943, 538, 3165, 2758, 6124, 2066, 4223, 296, 4035, 825, 4887, 670, 5043, 4573, 515, 6189, 8443, 3361, 5346, 88, 1792, 54, 3370, 8045, 2900, 802, 4835, 8255, 4722, 3022, 8474, 169, 454, 1810, 1071, 4437, 2696, 4681, 2981, 1819, 31, 823]

SEVERAL_COVER_PUBLISHERS = [[p.id, p.name]
               for p in Publisher.objects
                                 .filter(deleted=False,
                                         id__in=SEVERAL_COVER_PUBLISHER_IDS)
                                 .order_by('name')]

IN_USE_COUNTRIES = [['', '--']]
IN_USE_COUNTRIES.extend([c.id, c.name.title()]
                         for c in Country.objects.order_by('name'))

class IssuesWithCoversForm(forms.Form):
    """
    Form for filtering the listing of issues with several covers.
    """
    publisher = forms.ChoiceField(required=False,
                                  choices=SEVERAL_COVER_PUBLISHERS,
                                  initial=709)

class ReprintInspectionForm(forms.Form):
    """
    Form for filtering the listing of issues with identical issue and cover notes.
    """
    choices = [['', '--']]
    choices.extend(PUBLISHERS)
    languages = [['', '--']]
    languages.extend([l.id, l.name] for l in Language.objects.order_by('name'))
    publisher = forms.ChoiceField(required=False,
                                  choices=choices)
    country = forms.ChoiceField(required=False,
                                choices=IN_USE_COUNTRIES,
                                initial='')
    language = forms.ChoiceField(required=False,
                                choices=languages,
                                initial='')
