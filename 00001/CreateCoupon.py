import uuid

def create_Coupon(num):
  coupon_list = {}
  while len(coupon_list)<num:
    coupon_list[uuid.uuid4()] = 'coupon info'
  return coupon_list

if __name__ == '__main__':
    coupon_list = create_Coupon(200)
    print len(coupon_list)
