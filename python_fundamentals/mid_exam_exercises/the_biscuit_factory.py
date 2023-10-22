from math import floor

biscuits_per_day = int(input())
workers = int(input())
_30_day_production = int(input())

my_monthly_production = 0

for i in range(1,31):
    if i % 3 == 0:
        my_monthly_production += floor(workers*biscuits_per_day*0.75)
    else:
        my_monthly_production += workers*biscuits_per_day

print(f'You have produced {floor(my_monthly_production)} biscuits for the past month.')
result = abs(floor(my_monthly_production)-_30_day_production)/_30_day_production*100
if my_monthly_production > _30_day_production:
    print(f'You produce {result:.2f} percent more biscuits.')
else:
    print(f'You produce {result:.2f} percent less biscuits.')
