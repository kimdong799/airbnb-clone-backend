# ORM

---
test commit
django는 자동으로 데이터베이스 추상화 API를 제공함

python code를 이용해 db 조작 가능

# how to run python shell

```python
# python console 실행
python3 manage.py shell
```

# Manager

Manager는 db와 소통할 수 있게 도와주는 인터페이스로 모든 model에는 최소 1개 이상의 Manager가 존재한다. 즉, model을 생성하면 Manager도 함께 만들어진다.

# objects.all()

Room이라는 이름의 모델이 존재할 때 db에 저장된 모든 Room의 데이터를 확인하는 방법은 아래와 같다.

```python
# from 앱명.models import 모델명
from rooms.models import Room

Room.objects.all()
# => <QuerySet [<Room: Beautiful House in Seoul>, <Room: Apt in Seoul>]>
```

objects.all() 메소드는 QuerySet을 return하며 Iterable하다.

```python
>>> Room.objects.all().__iter__
<bound method QuerySet.__iter__ of <QuerySet [<Room: Beautiful House in Seoul>, <Room: Apt in Seoul>]>>

>>> for room in Room.objects.all():
...     print(room.name)
... 
Beautiful House in Seoul
Apt in Seoul
```

# get()

objects.get() 메소드는 단 하나의 데이터를 return한다. 즉, 특정 조건에 해당하는 데이터를 조회하고자 할 때 사용한다.

```python
# id가 1인 데이터 조회
Room.objects.get(id=1)
# <Room: Beautiful House in Seoul>

# 특정 조건을 만족하는 데이터 조회
Room.objects.get(name="Beautiful House in Seoul")
# <Room: Beautiful House in Seoul>

>>> Room.objects.get(pk=1)
<Room: Beautiful House in Seoul>

# 다수의 데이터가 조회되는 조건이 주어진 경우 에러가 발생한다.
>>> Room.objects.get(pet_friendly=True)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/kimdonghyeon/Library/Caches/pypoetry/virtualenvs/airbnb-clone-backend-hw4npWL_-py3.10/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/kimdonghyeon/Library/Caches/pypoetry/virtualenvs/airbnb-clone-backend-hw4npWL_-py3.10/lib/python3.10/site-packages/django/db/models/query.py", line 650, in get
    raise self.model.MultipleObjectsReturned(
rooms.models.Room.MultipleObjectsReturned: get() returned more than one Room -- it returned 2!

```

# filter()

objects.filter()는 1개 혹은 다수의 데이터를 조회하고자 하는 경우 모두 사용 가능하다.

```python
>>> Room.objects.filter(pet_friendly=True)
<QuerySet [<Room: Beautiful House in Seoul>, <Room: Apt in Seoul>]>

>>> Room.objects.filter(pet_friendly=False)
<QuerySet []>

# 검색 불가한 조건이 주어지면 FieldError가 발생한다.
>>> Room.objects.filter(potato=True)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/kimdonghyeon/Library/Caches/pypoetry/virtualenvs/airbnb-clone-backend-hw4npWL_-py3.10/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/kimdonghyeon/Library/Caches/pypoetry/virtualenvs/airbnb-clone-backend-hw4npWL_-py3.10/lib/python3.10/site-packages/django/db/models/query.py", line 1476, in filter
    return self._filter_or_exclude(False, args, kwargs)
  File "/Users/kimdonghyeon/Library/Caches/pypoetry/virtualenvs/airbnb-clone-backend-hw4npWL_-py3.10/lib/python3.10/site-packages/django/db/models/query.py", line 1494, in _filter_or_exclude
    clone._filter_or_exclude_inplace(negate, args, kwargs)
  File "/Users/kimdonghyeon/Library/Caches/pypoetry/virtualenvs/airbnb-clone-backend-hw4npWL_-py3.10/lib/python3.10/site-packages/django/db/models/query.py", line 1501, in _filter_or_exclude_inplace
    self._query.add_q(Q(*args, **kwargs))
  File "/Users/kimdonghyeon/Library/Caches/pypoetry/virtualenvs/airbnb-clone-backend-hw4npWL_-py3.10/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1602, in add_q
    clause, _ = self._add_q(q_object, self.used_aliases)
  File "/Users/kimdonghyeon/Library/Caches/pypoetry/virtualenvs/airbnb-clone-backend-hw4npWL_-py3.10/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1634, in _add_q
    child_clause, needed_inner = self.build_filter(
  File "/Users/kimdonghyeon/Library/Caches/pypoetry/virtualenvs/airbnb-clone-backend-hw4npWL_-py3.10/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1484, in build_filter
    lookups, parts, reffed_expression = self.solve_lookup_type(arg, summarize)
  File "/Users/kimdonghyeon/Library/Caches/pypoetry/virtualenvs/airbnb-clone-backend-hw4npWL_-py3.10/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1296, in solve_lookup_type
    _, field, _, lookup_parts = self.names_to_path(lookup_splitted, self.get_meta())
  File "/Users/kimdonghyeon/Library/Caches/pypoetry/virtualenvs/airbnb-clone-backend-hw4npWL_-py3.10/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1761, in names_to_path
    raise FieldError(
django.core.exceptions.FieldError: Cannot resolve keyword 'potato' into field. Choices are: address, amenities, booking, category, category_id, city, country, created_at, description, id, kind, name, owner, owner_id, pet_friendly, photo, price, review, rooms, toilets, updated_at, wishlist
```

## __gt(e)

```python
>>> Room.objects.filter(price__gt=15)
<QuerySet [<Room: Beautiful House in Seoul>]>
```

## __lt(e)

```python
>>> Room.objects.filter(price__lt=15)
<QuerySet [<Room: Apt in Seoul>]>
```

## __contains

```python
>>> Room.objects.filter(name__contains="Seoul")
<QuerySet [<Room: Beautiful House in Seoul>, <Room: Apt in Seoul>]>
```

## __startswith

```python
>>> Room.objects.filter(name__startswith="Apt")
<QuerySet [<Room: Apt in Seoul>]>
```

## __endswith

```python
>>> Room.objects.filter(name__endswith="Seoul")
<QuerySet [<Room: Beautiful House in Seoul>, <Room: Apt in Seoul>]>
```

# FK 관계 데이터 속성 조회

get() 메소드로 조회한 데이터를 특정 변수에 저장하면 다음과 같이 모든 속성을 확인할 수 있다.

```python
room = Room.objects.get(name="Beautiful House in Seoul")
room.id
# 1
room.pk
# 1
room.name
# 'Beautiful House in Seoul'
```

FK 관계를 갖는 데이터를 조회하는 경우 다음과 같은 방식으로 타 모델의 정보를 가져오는 것도 가능하다.

```python
>>> room.owner
<User: dongdong>
>>> print(room.owner)
dongdong
>>> room.owner.email
'kkk@korea.com'
>>>
```

```python
>>> room.amenities.all()[1].description
'Bowls, chopsticks, plates, cups, etc.'
```

# save()

save() 메소드를 이용해 데이터를 변경하는 것이 가능하다.

```python
>>> room.price
5
>>> room.price = 20
>>> room.save()
>>> room.price
20
```

# create()

```python
>>> Amenity.objects.create(name="Amenity from the console", description="how cool is this!")
<Amenity: Amenity from the console>
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/57cf8843-2ef8-4fa5-846a-da9c34572312/859ac352-9626-4ce5-b70d-6c578a8190fc/Untitled.png)

# delete()