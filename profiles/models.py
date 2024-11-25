import re
from django.db import models
from user.models import CustomUser
from core.utils import generate_unique_id
from django.core.exceptions import ValidationError
from user.models import BaseModel


def validate_iranian_phone_number(value):
    if not re.match(r"^(?:0)?9\d{9}$", value):
        raise ValidationError("Enter a valid Iranian phone number.")


class Skill(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skill"

    def __str__(self):
        return self.name


class SocialMedia(BaseModel):
    telegram = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    gitlab = models.URLField(null=True, blank=True)
    gitbe = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "SocialMedia"
        verbose_name_plural = "SocialMedia"


class Profile(BaseModel):
    gender_choices = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    slug_id = models.CharField(
        max_length=8, unique=True, default=generate_unique_id)
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(
        max_length=100, unique=True, null=True, blank=True)
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        blank=True,
        null=True,
        validators=[validate_iranian_phone_number],
    )
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True, null=True)

    description_myself = models.TextField(blank=True, null=True)
    cv_file = models.FileField(upload_to="cv_files/", blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="profile_images/", null=True, blank=True
    )

    skills = models.ManyToManyField(Skill, related_name="profiles", blank=True)
    socialmedia = models.ManyToManyField(
        SocialMedia, related_name="socialmedia", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.nickname}"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"


class WorkHistory(BaseModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="work_history_entries"
    )
    job_title = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(null=True, blank=True)
    job_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

    class Meta:
        verbose_name = "WorkHistory"
        verbose_name_plural = "WorkHistory"


class Education(BaseModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="education_entries"
    )
    institution_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} from {self.institution_name}"

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
