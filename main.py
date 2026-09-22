import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


numbers = list(range(1, 101))
primes = [n for n in numbers if is_prime(n)]

print("1부터 100 사이의 소수:")
print(primes)
print(f"\n총 개수: {len(primes)}개")

plt.figure(figsize=(10, 6))
plt.plot(primes, marker='o', linestyle='-', color='royalblue')
plt.title("1부터 100까지의 소수 그래프")
plt.xlabel("소수의 순서")
plt.ylabel("소수 값")
plt.grid(True)
plt.tight_layout()
plt.savefig("prime_graph.png")
print("\n그래프 이미지를 저장했습니다: prime_graph.png")

