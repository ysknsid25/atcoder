from decimal import Decimal, ROUND_HALF_UP
s=input()
print(Decimal(str(s)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))