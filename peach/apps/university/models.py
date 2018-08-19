# Create your models here.

from django.db import models
from django.db.models import DateField, CharField, TextField, ForeignKey, BooleanField, OneToOneField, FileField
from djutil.models import TimeStampedModel

from peach.base import choices
from peach.base.choices import METADATA_TYPE


class MetadataType(TimeStampedModel):
    """
    Metadata Types Model
    """
    name = CharField(max_length=200)
    type = CharField(max_length=200, choices=METADATA_TYPE)
    range_start = CharField(max_length=200)
    range_end = CharField(max_length=200)
    unit = CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'metadata_type'

    def __str__(self):
        return "%s %s" % (self.name, self.unit)


class Metadata(TimeStampedModel):
    """
    Metadata Types Model
    """
    name = CharField(max_length=200)
    type = ForeignKey(MetadataType, related_name='metadatas', on_delete=models.CASCADE)
    # TODO: Add user Id here

    class Meta:
        db_table = 'metadata'


class Course(TimeStampedModel):
    """
    Course Model
    Saves the course details and related stuff
    """
    name = CharField(max_length=200)
    status = CharField(max_length=200, choices=choices.STATUS)
    code = CharField(unique=200, max_length=200)
    department = CharField(max_length=200)

    class Meta:
        db_table = 'course'


class Assignment(TimeStampedModel):
    """
    Assignment Model
    """
    name = CharField(max_length=200)
    description = TextField()
    deadline = DateField()
    course = ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)
    # TODO: Add miscellaneous,user and assignment blob if needed

    class Meta:
        db_table = 'assignment'


class Experiment(TimeStampedModel):
    """
    Experiment Model
    """
    description = TextField()
    assignment = ForeignKey(Course, related_name='experiments', on_delete=models.CASCADE)

    class Meta:
        db_table = 'experiment'


class ExperimentMetadata(TimeStampedModel):
    """
    Experiment Metadata Model
    """
    metadata = ForeignKey(Metadata, on_delete=models.CASCADE)
    experiment = ForeignKey(Experiment, related_name='experiment_metadata', on_delete=models.CASCADE)
    input = BooleanField()
    value = CharField(max_length=200)

    class Meta:
        db_table = 'experiment_metadata'


class Equipment(TimeStampedModel):
    """
    Equipment Model
    """
    name = CharField(max_length=200)

    class Meta:
        db_table = 'equipment'


class Submission(TimeStampedModel):
    """
    Submission Model
    """
    submission_date = DateField(auto_now_add=True)
    comment = TextField()
    equipment = ForeignKey(Equipment, related_name="submissions", on_delete=models.CASCADE)
    assignment = OneToOneField(Assignment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'submission'


class Result(TimeStampedModel):
    """
    Result Model
    """
    experiment = OneToOneField(Experiment, on_delete=models.CASCADE)
    submission = ForeignKey(Submission, related_name="results", on_delete=models.CASCADE)
    description = TextField()

    class Meta:
        db_table = 'result'


class ResultMetadata(TimeStampedModel):
    """
    Result Metadata Model
    """
    result = ForeignKey(Result,related_name="result_metadata", on_delete=models.CASCADE)
    metadata = ForeignKey(Metadata, on_delete=models.CASCADE)
    value = CharField(max_length=200)
    input = BooleanField()

    class Meta:
        db_table = 'result_metadata'


class RawFile(TimeStampedModel):
    """
    RawFile Model
    """
    result = ForeignKey(Result,related_name="files", null=True, on_delete=models.SET_NULL)
    file = FileField(upload_to="documents/%Y/%m/%d")
    is_deleted = BooleanField(default=False)

    class Meta:
        db_table = 'raw_file'