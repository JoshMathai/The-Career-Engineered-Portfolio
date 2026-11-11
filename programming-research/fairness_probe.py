"""Coin Dash planning model, not a playable game. Python 3, standard library only."""
from math import dist
from random import Random

WIDTH, HEIGHT = 60.0, 40.0
SPEED, TIMER, REACTION = 5.0, 10.0, 2.0
SAFE_DISTANCE = SPEED * (TIMER - REACTION)


def coin_count(score):
    return max(2, 6 - score // 3)


def minimum_distance(score):
    return min(30.0, 4.0 + score)


def reachable(player, coin):
    return dist(player, coin) / SPEED + REACTION <= TIMER + 1e-9


def random_point(rng):
    return rng.uniform(0, WIDTH), rng.uniform(0, HEIGHT)


def safe_anchor(player, score, rng, attempts=100):
    """Try bounded random sampling, then place on a safe line toward a corner."""
    lower = minimum_distance(score)
    for _ in range(attempts):
        point = random_point(rng)
        if lower <= dist(player, point) <= SAFE_DISTANCE:
            return point
    corners = [(0.0, 0.0), (WIDTH, 0.0), (0.0, HEIGHT), (WIDTH, HEIGHT)]
    farthest = max(corners, key=lambda p: dist(player, p))
    distance = dist(player, farthest)
    target = (lower + min(SAFE_DISTANCE, distance)) / 2
    assert distance >= lower, "Arena or difficulty parameters need revision"
    return tuple(a + (b - a) * target / distance for a, b in zip(player, farthest))


def guarded_spawn(player, score, rng, attempts=100):
    coins = [safe_anchor(player, score, rng, attempts)]
    # Other coins may be risky; they never replace the guaranteed reachable one.
    while len(coins) < coin_count(score):
        point = random_point(rng)
        if dist(player, point) >= minimum_distance(score) and point not in coins:
            coins.append(point)
    return coins


def main():
    rng = Random(218)
    baseline_failures = 0
    for case in range(5000):
        player = random_point(rng)
        score = case % 41
        baseline = [random_point(rng) for _ in range(coin_count(score))]
        baseline_failures += not any(reachable(player, coin) for coin in baseline)
        coins = guarded_spawn(player, score, rng)
        assert len(coins) == coin_count(score) and len(set(coins)) == len(coins)
        assert all(0 <= x <= WIDTH and 0 <= y <= HEIGHT for x, y in coins)
        assert all(dist(player, coin) >= minimum_distance(score) - 1e-9 for coin in coins)
        assert any(reachable(player, coin) for coin in coins)
    for player in [(0, 0), (WIDTH, 0), (0, HEIGHT), (WIDTH, HEIGHT), (30, 20)]:
        for score in [0, 3, 6, 9, 12, 40]:
            coin = safe_anchor(player, score, rng, attempts=0)
            assert reachable(player, coin)
            assert minimum_distance(score) <= dist(player, coin) + 1e-9
    assert reachable((0, 0), (40, 0))
    assert not reachable((0, 0), (40.001, 0))
    assert [coin_count(s) for s in [0, 3, 6, 9, 12, 99]] == [6, 5, 4, 3, 2, 2]
    print("Coin Dash fairness planning probe | November 11, 2026 | seed 218")
    print("Assumptions: 60x40 arena, speed 5 units/s, 10-second timer, 2-second reserve.")
    print(f"Maximum safe path: {SAFE_DISTANCE:.0f} units; minimum distance capped at 30 units.")
    print(f"Random-only baseline: {baseline_failures}/5000 layouts had no reachable coin.")
    print("Guarded placement: 5000/5000 sampled layouts had a reachable coin.")
    print("PASS: counts, minimum distance, bounds, uniqueness, 30 forced fallbacks, distance boundary.")
    print("Limits: mathematical sampling, not Godot gameplay or a universal proof.")
    print("No acceleration, turning cost, collision, camera, frame timing, or human reaction measured.")


if __name__ == "__main__":
    main()
