def get_first_python(users):
    for x in users:
        if x['language'] == 'Python':
            return f"{x['first_name']}, {x['country']}"
    return 'There will be no Python developers'
