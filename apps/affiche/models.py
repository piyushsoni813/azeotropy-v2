from django.db import models
from apps.azeoid.models import AzeoProfile

class AfficheTeam(models.Model):
    team_name = models.CharField(max_length=100, unique=True)
    team_leader = models.ForeignKey(AzeoProfile, on_delete=models.CASCADE, related_name='affiche_leader')
    member2 = models.ForeignKey(AzeoProfile, on_delete=models.CASCADE, related_name='affiche_member2', null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    abstract = models.FileField(upload_to='affiche/abstracts/', null=True, blank=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.team_name} - Leader: {self.team_leader.azeo_id}"