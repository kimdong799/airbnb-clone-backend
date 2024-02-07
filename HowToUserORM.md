# python console 실행
python3 manage.py shell

# from 앱명.models import 모델명
from rooms.models import Room

Room.objects.all()
# => <QuerySet [<Room: Beautiful House in Seoul>, <Room: Apt in Seoul>]>

# id가 1인 데이터 조회
Room.objects.get(id=1)
# <Room: Beautiful House in Seoul>

# 특정 조건을 만족하는 데이터 조회
Room.objects.get(name="Beautiful House in Seoul")
# <Room: Beautiful House in Seoul>

>>> room.owner
<User: dongdong>
>>> print(room.owner)
dongdong
>>> room.owner.email
'kkk@korea.com'
>>>

>>> room.amenities.all()[1].description
'Bowls, chopsticks, plates, cups, etc.'

>>> room.price
5
>>> room.price = 20
>>> room.save()
>>> room.price
20