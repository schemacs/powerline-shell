
def add_username_segment():
    import os
    if powerline.args.shell == 'bash':
        user_prompt = ' \\u '
        known_users = {'longlele': 'lele'}
        if os.getenv('USER') in known_users:
            user_prompt = ' %s ' % known_users[os.getenv('USER')]
    elif powerline.args.shell == 'zsh':
        user_prompt = ' %n '
    else:
        user_prompt = ' %s ' % os.getenv('USER')
    powerline.append(user_prompt, Color.USERNAME_FG, Color.USERNAME_BG)

add_username_segment()
