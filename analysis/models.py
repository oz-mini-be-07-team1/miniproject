from django.db import models
from common.models import CommonModel


# - User: FK
class Analysis(CommonModel):
    analysis_id = models.AutoField(
        primary_key=True,
        serialize=False,
        verbose_name='Analysis ID'
    )

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='accounts'
    )

    analysis_target = models.CharField(
        max_length=10,
        verbose_name='Bank Code'
    )

    analysis_period = models.CharField(
        max_length=20,
        verbose_name='Account Number'
    )

    start_date = models.DateField(
        verbose_name='Start Date'
    )

    end_date = models.DateField(
        verbose_name='End Date'
    )

    description = models.TextField(
        verbose_name='Description'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(
        upload_to='images/analysis/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Analysis"
        verbose_name_plural = "Analyses"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'start_date', 'end_date']),
        ]

    def __str__(self):
        return f"Analysis {self.analysis_id} by {self.user}"

    def get_analysis_period(self):
        return f"{self.start_date} to {self.end_date}"

    def is_active(self):
        """
        Checks if the analysis is currently ongoing based on the dates.
        """
        from datetime import date
        today = date.today()
        return self.start_date <= today <= self.end_date