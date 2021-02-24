lax_coordinates = (33.9425, -118.408056)

city, year, pop, chg, area = ('Tokyo', 2003, 32459,0.66, 8014)

traveler_ids = [('USA','31195855'),('BRA','CE324567'),('ESP','XDA31940')]

for passport in sorted(traveler_ids): # 리스트를 반복할때 passport 변수가 각 튜플에 바인딩 된다.
    print('%s %s' %  passport) # % 포맷 연산자는 튜플을 이해하고 각 항목을 하나의 필드로 처리한다.

for country, _ in traveler_ids:
    print(country)

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

b, a = a, b

dv = divmod(20,8)
print(dv)
t = (20,8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder)

import os
_,filename = os.path('/home/luciano/.ssh/idrsa.pub')
print(filename)

a, b, *rest = range(5)
print(a,b,rest)
a, b, *rest = range(3)
print(a,b,rest)
a, b, *rest = range(2)
print(a,b,rest)

a, *body, c, d = range(5)
print(a,body,c,d)
*head, b, c, d = range(5)
print(head,b,c,d)

metro_areas=[
    ('Tokyo','JP',36.933,(35.3224,23.421)),
    ('korea','KR',34.933,(54.3224,53.12)),
    ('USA','US',58.933,(3214,-38.4)),
    ('Mexico city','MX',20.933,(31.244,39.4842)),
]
print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for  name, cc, pop, (latitude,longitude) in metro_areas:
    if longitude>0 :
        print(fmt.format(name,latitude,longitude))

from collections import namedtuple
City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo','JP',36.933,(35.689722,139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

print(City._fields)
Latlong = namedtuple('LatLong','lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, Latlong(28.1231,32.4949))
delhi = City._make(delhi_data)
print(delhi._asdict())
for key,value in delhi._asdict().items():
    print(key+':',value)