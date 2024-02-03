from django.db import models


# 다른 app의 model에서 공통 로직을 관리하기 위한 용도
# DB 마이그레이션 X
class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(
        # object가 처음 생성된 date 지정
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        # object가 저장될 때마다 현재 date 지정
        auto_now=True,
    )

    # django에서 model을 configure하기 위해 사용
    class Meta:
        # abstract = True 설정 시 DB에 테이블에 생성되지 않음
        abstract = True
