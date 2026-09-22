def is_prime(n: int) -> bool:
    """주어진 정수 n이 소수인지 판별합니다."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 1부터 100 사이의 소수 구하기
primes = [num for num in range(1, 101) if is_prime(num)]

print("1부터 100 사이의 소수:")
print(primes)
print(f"\n총 개수: {len(primes)}개")

def is_prime(n: int) -> bool:
    """주어진 정수 n이 소수인지 판별합니다."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 1부터 100 사이의 소수 구하기
primes = [num for num in range(1, 101) if is_prime(num)]

print("1부터 100 사이의 소수:")
print(primes)
print(f"\n총 개수: {len(primes)}개")

