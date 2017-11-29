def menu_prompt():
    
    options = {}

    def problem():
        os.system('clear')
        data = load_json_data()
        prob = get_problem(data)
        print('Problem details')
        print('='*15)
        print('Problem: {}'.format(prob['Problem']))
        print('Page: {}'.format(prob['Page']))
        input('\nPress Enter to continue...')
        options['main']()

    def update():
        os.system('clear')
        data = load_json_data()
        print('Update problem')
        print('='*14)
        prob = input('\nProblem attempted (ex. 12.3) >> ')
        if not valid_prob_num(prob):
            print('Invalid problem number')
            input('\nPress Enter to return to main menu...')
            options['main']()
        status = input('pass/fail/None? >> ')
        if status not in ['pass', 'fail', None]:
            print('Invalid status')
            input('\nPress Enter to return to main menu...')
            options['main']()
        print('Setting problem {} to {}'.format(prob, status))
        update_problem_status(data, prob, status)
        input('\nPress Enter to continue...')
        options['main']()

    def stats():
        os.system('clear')
        data = load_json_data()
        output_stats(data)
        input('\nPress Enter to continue...')
        options['main']()

    def settings():
        os.system('clear')
        settings = load_settings()
        print('Settings')
        print('='*8)
        print('Chapters: {}'.format(settings['Chapters']))
        print('Statuses: {}'.format(settings['Status']))
        print('1) Add chapters')
        print('2) Remove chapters')
        print('3) Update statuses')
        print('4) Return to main menu')
        choice = input('\nEnter choice >> ')
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            options['main']()
        else:
            print('Invalid choice')
            input('\nPress Enter to continue...')
            options['settings']()
        options['main']()

    def quit():
        os.system('clear')
        sys.exit()

    def main():
        os.system('clear')
        print('Crack Study')
        print('='*11)
        print('1) Get a problem')
        print('2) Update problem status')
        print('3) Show stats')
        print('4) User settings')
        print('\n0) Quit')
        choice = input('\nEnter choice >> ')
        options[choice]()

    options = {
        '1': problem,
        '2': update,
        '3': stats,
        '4': settings,
        '0': quit,
        'main': main,
        }

    options['main']()
