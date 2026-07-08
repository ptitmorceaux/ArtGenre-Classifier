from django.db import models

class TrainingSession(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    model_type = models.CharField(max_length=50)
    epochs = models.IntegerField()
    learning_rate = models.FloatField()
    accuracy = models.FloatField(null=True, blank=True)
    final_loss = models.FloatField(null=True, blank=True)
    loss_curve_filename = models.CharField(max_length=255, null=True, blank=True)
    confusion_matrix_filename = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.model_type.upper()}] Session {self.session_id} - Acc: {self.accuracy}"