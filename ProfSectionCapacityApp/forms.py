from django import forms
from .models import Capacity, Free, CapacitySection,TypePoints,CourseYear
from UsersApp.models import Professor
from AcademicInfoApp.models import Year,Section,Course
from django.core.exceptions import ValidationError

class UploadForm(forms.Form):
    file = forms.FileField(
        label="Carregar fitxer Excel",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )

class CapacityForm(forms.ModelForm):
    class Meta:
        model = Capacity
        fields = ['Professor', 'Year', 'Points', 'Comment']
        labels = {
            'Professor':'Professor/a',
            'Year':'Curs acadèmic',            
            'Points': 'Punts totals ',
            'Comment':'Comentari',
        }
        widgets = {
            'Professor': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'Year': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'Points': forms.NumberInput(attrs={'required': 'required','class': 'form-control'}), 
            'Comment': forms.Textarea(attrs={'rows': 3,'class': 'form-control', 'placeholder': 'Comentari opcional'}),
        }

    def __init__(self, *args, **kwargs):
        professor = kwargs.pop('professor', None)
        super().__init__(*args, **kwargs)

        # Dynamically set the queryset for the 'Year' field
        self.fields['Year'].queryset = Year.objects.all().order_by('-Year')

        if professor:
            # If a professor is passed, set it as initial and make it read-only
            self.fields['Professor'].initial = professor
            self.fields['Professor'].disabled = True
        elif self.instance and self.instance.pk:
            # If editing an existing Capacity, make the professor read-only
            self.fields['Professor'].disabled = True


    
class FreeForm(forms.ModelForm):
    class Meta:
        model = Free
        fields = ['Professor', 'Year', 'PointsFree', 'Comment']
        labels = {
            'Professor':'Professor/a',
            'Year':'Curs acadèmic',
            'Comment':'Comentari',
            'PointsFree': "Punts d'alliberació",
        }
        widgets = {
            'Professor': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'Year': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'PointsFree': forms.NumberInput(attrs={'required': 'required','class': 'form-control'}), 
            'Comment': forms.Textarea(attrs={'rows': 3, 'class': 'form-control','placeholder': 'Comentari opcional'}),
        }
       
    
    def __init__(self, *args, **kwargs):
        professor = kwargs.pop('professor', None)
        super().__init__(*args, **kwargs)
        
        self.fields['Year'].queryset = Year.objects.all().order_by('-Year')

        if professor:
            # If a professor is passed, set it as initial and make it read-only
            self.fields['Professor'].initial = professor
            self.fields['Professor'].disabled = True
        elif self.instance and self.instance.pk:
            # If editing an existing Capacity, make the professor read-only
            self.fields['Professor'].disabled = True
        


class CapacitySectionForm(forms.ModelForm):
    class Meta:
        model = CapacitySection
        fields = ['Professor', 'Year', 'Section', 'Points', 'Comment']
        labels = {
            'Professor':'Professor/a',
            'Year':"Curs acadèmic",
            'Section':'Secció',
            'Comment':'Comentari',
            'Points': 'Punts per secció',
        }
        widgets = {
            'Professor': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'Year': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'Section': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'Points': forms.NumberInput(attrs={'required': 'required','class': 'form-control'}), 
            'Comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Comentari opcional','class': 'form-control'}),
        }  
    
    def __init__(self, *args, **kwargs):
        professor = kwargs.pop('professor', None)
        super().__init__(*args, **kwargs)
        
        self.fields['Year'].queryset = Year.objects.all().order_by('-Year')

        if professor:
            # If a professor is passed, set it as initial and make it read-only
            self.fields['Professor'].initial = professor
            self.fields['Professor'].disabled = True
        elif self.instance and self.instance.pk:
            # If editing an existing Capacity, make the professor read-only
            self.fields['Professor'].disabled = True

class TypePointsForm(forms.ModelForm):
    class Meta:
        model = TypePoints
        fields = ['Year','Section','NamePointsA','NamePointsB','NamePointsC','NamePointsD','NamePointsE','NamePointsF']
        labels = {
            'Year':'Curs acadèmic',
            'Section':'Secció',
            'NamePointsA':'Nom punts A',
            'NamePointsB':'Nom punts B',
            'NamePointsC':'Nom punts C',
            'NamePointsD':'Nom punts D',
            'NamePointsE':'Nom punts E',
            'NamePointsF':'Nom punts F',
        }
        widgets = {
            'Year': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'Section': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'NamePointsA': forms.TextInput(attrs={'class': 'form-control','placeholder': '...'}),
            'NamePointsB': forms.TextInput(attrs={'class': 'form-control','placeholder': '...'}),
            'NamePointsC': forms.TextInput(attrs={'class': 'form-control','placeholder': '...'}),
            'NamePointsD': forms.TextInput(attrs={'class': 'form-control','placeholder': '...'}),
            'NamePointsE': forms.TextInput(attrs={'class': 'form-control','placeholder': '...'}),
            'NamePointsF': forms.TextInput(attrs={'class': 'form-control','placeholder': '...'}),
        }

    def __init__(self, *args, **kwargs):
        super(TypePointsForm, self).__init__(*args, **kwargs)
        self.fields['Year'].queryset = Year.objects.all().order_by('-Year')  # Order by -Year

class CourseYearForm(forms.ModelForm):
    class Meta:
        model = CourseYear
        fields = [ 'Course', 'Year', 'Semester', 'PointsA', 'PointsB', 'PointsC', 'PointsD', 'PointsE','PointsF', 'Language','Comment']
        labels = {
            'Course': 'Assignatura',
            'Year': 'Curs acadèmic',
            'Semester': 'Semestre',
            'PointsA': 'Punts A',
            'PointsB': 'Punts B',
            'PointsC': 'Punts C',
            'PointsD': 'Punts D',
            'PointsE': 'Punts E',
            'PointsF': 'Punts F',
            'Language': 'Idioma',
            'Comment':'Comentari',
        }
        widgets = {
            'Course': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'Year': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'Semester': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'PointsA': forms.NumberInput(attrs={'class': 'form-control','placeholder': '-'}),
            'PointsB': forms.NumberInput(attrs={'class': 'form-control','placeholder': '-'}),
            'PointsC': forms.NumberInput(attrs={'class': 'form-control','placeholder': '-'}),
            'PointsD': forms.NumberInput(attrs={'class': 'form-control','placeholder': '-'}),
            'PointsE': forms.NumberInput(attrs={'class': 'form-control','placeholder': '-'}),
            'PointsF': forms.NumberInput(attrs={'class': 'form-control','placeholder': '-'}),
            'Language': forms.Select(attrs={'required': 'required','class': 'form-select'}),
            'Comment': forms.Textarea(attrs={'rows': 3,'class': 'form-control', 'placeholder': 'Comentari opcional'}),
        }

    
    def clean(self):
        cleaned_data = super().clean()
        Course = cleaned_data.get('Course')
        Year = cleaned_data.get('Year')
        Semester = cleaned_data.get('Semester')

        instance = self.instance  # The current instance of Course being edited

        if instance.pk:
            # Exclude the current instance from the query to allow for editing the same object
            if CourseYear.objects.filter(Course=Course, Year=Year, Semester=Semester).exclude(pk=instance.pk).exists():
                raise ValidationError('Aquest Curs ja existeix en aquest Any i Semestre.')

        else:
            # Check if a Course already exists with the same CodeCourse and Degree (for new entries)
            if CourseYear.objects.filter(Course=Course, Year=Year, Semester=Semester).exists():
                raise ValidationError('Aquest Curs ja existeix en aquest  Any i Semestre.')

        return cleaned_data


    def __init__(self, *args, **kwargs):
        course = kwargs.pop('Course', None)
        super().__init__(*args, **kwargs)
        
        self.fields['Year'].queryset = Year.objects.all().order_by('-Year')
        self.fields['Course'].queryset = Course.objects.all().order_by('NameCourse')

    
        if course:
            # If a course is passed, set it as initial and make it read-only
            self.fields['Course'].initial = course
            self.fields['Course'].disabled = True
        elif self.instance and self.instance.pk:
            # If editing an existing Course, make the course read-only
            self.fields['Course'].disabled = True
    
