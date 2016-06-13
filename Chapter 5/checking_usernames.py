current_users = ['admin', 'bjblast', 'djd', 'pjfrost', 'manwplan']
new_users = ['bjblast', 'frontman', 'pjfrost', 'duder']

for user in new_users:
    if user.lower() in current_users:
        print("That user name is already taken")
    else:
        print("That name is available!")