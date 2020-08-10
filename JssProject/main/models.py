from django.db import models
from django.contrib.auth.models import User

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
# User : 자소서 = 1 : N
# on_delete=models.CASCADE 연결된 오브젝트가 지워지면 연결된 자소서 오브젝트들도 사라진다.