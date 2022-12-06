from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username


    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            user_profile = Profile(user=instance)
            user_profile.save()
            user_profile.follows.set([instance.profile.id])
            user_profile.save()

# Create a Profile for each new user.
    #post_save.connect(create_profile, sender=User)

class Post(models.Model):
        user = models.ForeignKey(
            User, related_name="post", on_delete=models.DO_NOTHING
        )
        body = models.CharField(max_length=200)
        created_at = models.DateTimeField(auto_now_add=True)   
        link = models.URLField(max_length=500,default="")
        category = models.CharField(max_length=20,default="")

        def __str__(self):
            return (
                f"{self.user} "
                f"({self.created_at:%Y-%m-%d %H:%M}): "
                f"{self.body[:30]}..."
                f"{self.link[:20]}..."
                f"{self.category[:20]}..."
            )


