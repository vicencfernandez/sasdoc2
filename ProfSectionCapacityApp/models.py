from django.db import models
from AcademicInfoApp.models import Year,Section,Course,Language
from UsersApp.models import Professor

# Create your models here.

class Capacity(models.Model):
    idCapacity = models.AutoField(primary_key=True)
    Professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    Year = models.ForeignKey(Year, on_delete=models.CASCADE)
    Points = models.IntegerField(default=0)
    Comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name='capacity'
        verbose_name_plural='capacities'
        unique_together = ('Professor', 'Year')  # Ensure unique combinations


    def __str__(self):
        return f"{self.Professor.name} {self.Professor.family_name} - {self.Year.Year} - Points: {self.Points}"


class Free(models.Model):
    idFree = models.AutoField(primary_key=True)
    Professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    Year = models.ForeignKey(Year, on_delete=models.CASCADE)
    PointsFree = models.IntegerField(default=0)
    Comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name='free'
        verbose_name_plural='frees'

    def __str__(self):
        return f"{self.Professor.name} {self.Professor.family_name} - {self.Year.Year} - Free Points: {self.PointsFree}"


class CapacitySection(models.Model):
    idCapacitySection = models.AutoField(primary_key=True)
    Professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    Year = models.ForeignKey(Year, on_delete=models.CASCADE)
    Section = models.ForeignKey(Section, on_delete=models.CASCADE)
    Points = models.IntegerField(default=0)
    Comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name='capacity section'
        verbose_name_plural='capacity sections'
        unique_together = ('Professor', 'Year','Section')  # Ensure unique combinations

    def __str__(self):
        return f"{self.Professor.name} {self.Professor.family_name} - {self.Year.Year} - {self.Section.NameSection} - Points: {self.Points}"


class TypePoints(models.Model):
    idTypePoints = models.AutoField(primary_key=True)
    Year = models.ForeignKey(Year, on_delete=models.CASCADE)
    Section = models.ForeignKey(Section, on_delete=models.CASCADE)
    NamePointsA = models.CharField(max_length=100, default="", blank=True, null=True)
    NamePointsB = models.CharField(max_length=100, default="", blank=True, null=True)
    NamePointsC = models.CharField(max_length=100, default="", blank=True, null=True)
    NamePointsD = models.CharField(max_length=100, default="", blank=True, null=True)
    NamePointsE = models.CharField(max_length=100, default="", blank=True, null=True)
    NamePointsF = models.CharField(max_length=100, default="", blank=True, null=True)

    class Meta:
        verbose_name='type points'
        verbose_name_plural='type points'
        unique_together = ('Year', 'Section')  # Ensure unique combinations


    def __str__(self):
        return f"{self.Year.Year} - {self.Section.NameSection}"
    
class CourseYear(models.Model):
    idCourseYear = models.AutoField(primary_key=True)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_years')
    Year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='course_years')
    Semester = models.CharField(max_length=2, choices=[('Q1', 'Q1'), ('Q2', 'Q2')], default='Q1')
    PointsA = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    PointsB = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    PointsC = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    PointsD = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    PointsE = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    PointsF = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    Language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True, related_name='course_years')
    Comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name='course year'
        verbose_name_plural='course years'
        unique_together = ('Year', 'Course','Semester')  # Ensure unique combinations

    def __str__(self):
        return f"{self.Course.NameCourse} ({self.Year.Year} - {self.get_Semester_display()})"
