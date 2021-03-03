DIAL_CODES = [
    (86, 'china'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (82,'korea')
]

d1 = dict(DIAL_CODES)
print('d1:',d1.keys())
d2 = dict(sorted(DIAL_CODES))
print('d2:',d2.keys())
d3 = dict(sorted(DIAL_CODES,key=lambda x:x[1]))
print('d3:',d3.keys())
assert d1==d2 and d2==d3