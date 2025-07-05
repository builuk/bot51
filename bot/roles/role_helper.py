from bot.roles.users import users_dict
from bot.roles.commands import commands_dict

def check_command_access(command, user_id):
    # Якщо команди немає в словнику — дозволяємо всім
    if command not in commands_dict:
        return True

    # Шукаємо роль користувача
    user_role = None
    for role, user_list in users_dict.items():
        if int(user_id) in user_list:
            user_role = role
            break

    # Якщо користувач не знайдений ні в одній ролі — доступ заборонено
    if user_role is None:
        return "Access denied: your role is not assigned"

    # Перевіряємо, чи роль користувача дозволена для цієї команди
    allowed_roles = commands_dict[command]
    if user_role in allowed_roles:
        return True
    else:
        return f"Access denied: role '{user_role}' does not have access to '{command}'"
