from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# django 기본 user model 상속 (커스텀 usera 모델)
# AbstactUser의 수정하고 싶은 부분을 Copy하여 오버라이딩
# 절대 django의 코드는 수정하지 말 것. 배포 시 새로운 django의 소스코드로 변경됨
class User(AbstractUser):
    # editable을 False로 설정하면 관리자 페이지에 나타나지 않음
    # django에서 제공하는 fisrt_name, last_name 대신 name 필드 생성

    # gender 필드의 choice를 위한 클래스
    class GenderChoices(models.TextChoices):
        # 대문자로 작성
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    # language 필드의 choice를 위한 클래스
    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    # currency 필드의 choice를 위한 클래스
    class CurrencyChoices(models.TextChoices):
        WON = ("won", "Korean Won")
        USD = ("usd", "Dallar")

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    avatar = models.ImageField(
        # 필수 항목 해제
        blank=True,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    is_host = models.BooleanField()
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )

    def hosting_rooms(self):
        return self.rooms.count()
