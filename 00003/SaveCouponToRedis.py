import uuid
import redis

def create_coupon(num):
  coupon_list = {}
  while len(coupon_list)<num:
    coupon_list[uuid.uuid4()] = 'coupon info'
  return coupon_list

def start_redis(port=6379):
  return redis.Redis(host='localhost', port=6379, db=0)

r = start_redis()
coupons = create_coupon(200)
r.delete('coupon')
for i in coupons:
  r.hset(i, 'detail', coupons[i])
  r.sadd('coupon', i)
print r.scard('coupon')
