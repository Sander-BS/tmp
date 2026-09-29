# =====================================================================
# 1. СПИСКИ (LISTS)
# =====================================================================

def remove_duplicates_preserve_order(items: list) -> list:
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    result.sort()
    return result


def get_top_n_above_threshold(numbers: list[int | float], n: int, threshold: int | float) -> list[int | float]:
    result = []

    for num in numbers:
        if num > threshold:
            result.append(num)

    result.sort(reverse=True)
    return result[:n]


# =====================================================================
# 2. КОРТЕЖИ (TUPLES)
# =====================================================================

def calculate_bounding_box(points: list[tuple[int, int]]) -> tuple[int, int, int, int]:
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for point in points:
        min_x = min(min_x, point[0])
        max_x = max(max_x, point[0])
        min_y = min(min_y, point[1])
        max_y = max(max_y, point[1])
    return (min_x, max_x, min_y, max_y)


def compare_versions(version1: tuple[int, ...], version2: tuple[int, ...]) -> int:
    if version1 < version2:
        return -1
    elif version1 > version2:
        return 1
    else:
        return 0


# =====================================================================
# 3. СЛОВАРИ (DICTIONARIES)
# =====================================================================

def group_by_category(items: list[dict]) -> dict[str, list[str]]:
    result = {}

    for item in items:
        category = item["category"]
        name = item["name"]

        if category not in result:
            result[category] = []

        result[category].append(name)

    return result



def merge_configs(default_config: dict, user_config: dict) -> dict:
    result = {}

    for item in default_config.keys():
        if item in user_config:
            result[item] = user_config[item]
        else:
            result[item] = default_config[item]

    return result

# =====================================================================
# 4. МНОЖЕСТВА (SETS)
# =====================================================================

def find_common_elements(*lists: list) -> set:
    result = set(lists[0])
    for item in lists:
        result &= set(item)
    return result



def analyze_user_interests(user_a_tags: set[str], user_b_tags: set[str]) -> dict[str, set[str]]:
    result = {'shared': set(), 'only_a': set(), 'only_b': set()}

    result['shared'] = user_a_tags & user_b_tags
    result['only_a'] = user_a_tags - user_b_tags
    result['only_b'] = user_b_tags - user_a_tags

    return result


# =====================================================================
# 5. КОМБИНИРОВАННЫЕ ЗАДАЧИ
# =====================================================================

def calculate_invoice(cart: list[dict], prices: dict[str, float], discounts: dict[str, float]) -> float:
    result = 0.0

    for entry in cart:
        item_name = entry["item"]
        quantity = entry["quantity"]

        price = prices.get(item_name, 0.0)
        discount_pct = discounts.get(item_name, 0.0)

        item_total = price * quantity * (1 - discount_pct / 100)

        result += item_total

    return round(result, 2)


def summarize_user_activity(logs: list[dict]) -> dict[str, dict[str, int]]:
    result = {}

    for log in logs:
        user = log["user"]
        action = log["action"]

        if user not in result:
            result[user] = {}

        if action not in result[user]:
            result[user][action] = 0

        result[user][action] += 1

    return result


# =====================================================================
# ПРОВЕРКА РЕЗУЛЬТАТОВ (RUNNER)
# =====================================================================

if __name__ == "__main__":
    print("--- 1.1 Remove Duplicates ---")
    res1 = remove_duplicates_preserve_order(["a", "b", "a", "c", "b", "d"])
    print(f"Результат:  {res1}\nОжидается:  ['a', 'b', 'c', 'd']\n")

    print("--- 1.2 Top N Above Threshold ---")
    res2 = get_top_n_above_threshold([10, 2, 45, 12, 8, 30, 45, 1], n=3, threshold=9)
    print(f"Результат:  {res2}\nОжидается:  [45, 45, 30] или [45, 30, 12] (в зависимости от обработки повторов)\n")

    print("--- 2.1 Bounding Box ---")
    res3 = calculate_bounding_box([(2, 5), (-1, 10), (4, 3), (0, 0)])
    print(f"Результат:  {res3}\nОжидается:  (-1, 4, 0, 10)\n")

    print("--- 2.2 Compare Versions ---")
    res4_1 = compare_versions((1, 2, 0), (1, 10, 0))
    res4_2 = compare_versions((2, 1), (2, 1, 0))
    print(f"Результат 1: {res4_1} (Ожидается -1)")
    print(f"Результат 2: {res4_2} (Ожидается 0 или -1 в зависимости от строгости по длине)\n")

    print("--- 3.1 Group By Category ---")
    products = [
        {"name": "Phone", "category": "tech"},
        {"name": "Shirt", "category": "clothes"},
        {"name": "Tablet", "category": "tech"},
    ]
    res5 = group_by_category(products)
    print(f"Результат:  {res5}\nОжидается:  {{'tech': ['Phone', 'Tablet'], 'clothes': ['Shirt']}}\n")

    print("--- 3.2 Merge Configs ---")
    def_cfg = {"host": "localhost", "port": 8080, "debug": False}
    usr_cfg = {"port": 9000, "debug": True}
    res6 = merge_configs(def_cfg, usr_cfg)
    print(f"Результат:  {res6}\nОжидается:  {{'host': 'localhost', 'port': 9000, 'debug': True}}\n")

    print("--- 4.1 Common Elements ---")
    res7 = find_common_elements([1, 2, 3, 4], [2, 3, 5], [0, 2, 3, 9])
    print(f"Результат:  {res7}\nОжидается:  {{2, 3}}\n")

    print("--- 4.2 User Interests ---")
    res8 = analyze_user_interests({"python", "sql", "git"}, {"python", "docker", "linux"})
    print(
        f"Результат:  {res8}\nОжидается:  {{'shared': {{'python'}}, 'only_a': {{'sql', 'git'}}, 'only_b': {{'docker', 'linux'}}\n")

    print("--- 5.1 Calculate Invoice ---")
    cart_items = [{"item": "apple", "quantity": 3}, {"item": "banana", "quantity": 2}]
    price_list = {"apple": 100.0, "banana": 50.0}
    discount_list = {"apple": 10}  # 10% скидка на яблоки
    res9 = calculate_invoice(cart_items, price_list, discount_list)
    print(f"Результат:  {res9}\nОжидается:  370.0\n")

    print("--- 5.2 Summarize User Activity ---")
    raw_logs = [
        {"user": "alex", "action": "login"},
        {"user": "alex", "action": "click"},
        {"user": "maria", "action": "login"},
        {"user": "alex", "action": "click"},
    ]
    res10 = summarize_user_activity(raw_logs)
    print(f"Результат:  {res10}\nОжидается:  {{'alex': {{'login': 1, 'click': 2}}, 'maria': {{'login': 1}}}}\n")