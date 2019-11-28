def build_user(data):
    return __validate_user_data(data.get('name'), data.get('plataform'))

def __validate_user_data(name, plataform):
    if not name:
        raise AttributeError('name has to informed')
    if not plataform:
        raise AttributeError('plataform has to informed')
    if plataform not in ['twitter', 'facebook', 'instagram']:
     raise AttributeError('wrong plataform')
    return (name, plataform)
