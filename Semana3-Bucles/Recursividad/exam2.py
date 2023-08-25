def get_members(group):
    group_data = {
        "sales": ["user1", "user2", "user3"],
        "engineering": ["user4", "user5", "user6", "user7", "user8", "user9",
                        "user10", "user11"],
        "everyone": ["user12", "user13", "user14", "user15", "user16", "user17", "user18", "user19",
                     "user20", "user21", "user22", "user23", "user24", "user25", "user26", "user27", "user28", "user29",],
    }
    return group_data.get(group, [])
def is_group(member):
    return member in ["sales", "engineering", "everyone"]

def count_users(group):
    count = 0
    for member in get_members(group):
        count += 1
        if is_group(member):
            count += count_users(member)
    return count

print(count_users("sales"))        # Debería ser 3
print(count_users("engineering"))  # Debería ser 8
print(count_users("everyone"))     # Debería ser 18

