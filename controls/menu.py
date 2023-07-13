from pick import pick


def show_menu(title, options):
    option, index = pick(options, title, indicator='=>')
    print(option, index)
