def groups_per_user(group_dictionary):
    user_groups = {}

    # Itera a través de group_dictionary
    for group, users in group_dictionary.items():
        # Ahora itera a través de los usuarios en el grupo
        for user in users:
            # Agrega el grupo a la lista de grupos para este usuario,
            # creando la entrada en el diccionario si es necesario
            if user in user_groups:
                user_groups[user].append(group)
            else:
                user_groups[user] = [group]

    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
                      "public": ["admin", "userB"],
                      "administrator": ["admin"]}))
