# Standard Library
import os
import sys

# Local Modules
import problem
import settings

class Menu():

    def __init__(self):
        self.title = 'Menu'
        self.options = []
        self.prompt = '>> '

    def _display(self):
        os.system('clear')
        print(self.title)
        print('='*len(self.title))

    def display(self):
        self._display()
        for option in self.options:
            print(option)
        in_data = input(self.prompt)
        self.selection(in_data)
    
    def selection(self, *args, **kwargs):
        return

    def invalid_choice(self, choice):
        print('"{}" is not a valid choice'.format(choice))
        input('Press Enter to continue...')

    def quit(self):
        os.system('clear')
        sys.exit()


class GetProblemMenu(Menu):

    def __init__(self):
        self.title = 'Problem Details'
        data = problem.load_json_data()
        prob = problem.get_problem(data)
        self.options = [
            'Problem: {}'.format(prob['Problem']),
            'Page: {}'.format(prob['Page']),
            ]
        self.prompt = '\nPress Enter to return to main menu...'


class UpdateProblemMenu(Menu):

    def __init__(self):
        self.title = 'Update Problem'

    def display(self):
        self._display()
        prob = input('\nProblem attempted (ex. 12.3) >> ')
        if not problem.valid_prob_num(prob):
            print('Invalid problem number')
            input('\nPress Enter to return to main menu...')
            self.selection()
        status = input('pass/fail/None? >> ').lower()
        if status == 'none':
            status = None
        if status not in ['pass', 'fail', None]:
            print('Invalid status')
            input('\nPress Enter to return to main menu...')
            self.selection()
        print('Setting problem {} to {}'.format(prob, status))
        data = problem.retrieve_problem_data() 
        problem.update_problem_status(data, prob, status)
        input('\nPress Enter to continue...')
        self.selection()

            
class StatsMenu(Menu):

    def __init__(self):
        self.title = 'Problem Stats'
        self.options = []
        self.prompt = '\nPress Enter to return to main menu...'

    def display(self):
        self._display()
        data = problem.load_json_data()
        problem.output_stats(data)
        input(self.prompt)
        self.selection()


class SettingsMenu(Menu):

    def __init__(self):
        self.title = 'Settings Menu'
        self.menu = {
            '1': self.add_chapter,
            '2': self.rm_chapter,
            '3': lambda: None,
            }
        self.options = [
            '1) Add chapters',
            '2) Remove chapters',
            '3) Return to main menu',
            ]
        self.prompt = '\nEnter choice >> '
    
    def add_chapter(self):
        pass

    def rm_chapter(self):
        pass

    def selection(self, choice):
        self.menu[choice]()


class MainMenu(Menu):

    def __init__(self):
        self.title = 'Crack Study'
        self.menu = {
            '1': GetProblemMenu(),
            '2': UpdateProblemMenu(),
            '3': StatsMenu(),
            '4': SettingsMenu(),
            }
        self.options = [
            '1) Get a problem',
            '2) Update problem status',
            '3) Show stats',
            '4) User settings',
            '\n0) Quit',
            ]
        self.prompt = '\nEnter choice >> '

    def selection(self, choice):
        print(choice)
        if choice == '0':
            self.quit()
        if choice not in self.menu.keys():
            self.invalid_choice(choice)
            self.display()
        self.menu[choice].display()


    def run(self):
        while True:
            self.display()

    



#def menu_prompt():
#    
#    options = {}
#
#
#    def settings():
#        os.system('clear')
#        settings = load_settings()
#        print('Settings')
#        print('='*8)
#        print('Chapters: {}'.format(settings['Chapters']))
#        print('Statuses: {}'.format(settings['Status']))
#        print('1) Add chapters')
#        print('2) Remove chapters')
#        print('3) Update statuses')
#        print('4) Return to main menu')
#        choice = input('\nEnter choice >> ')
#        if choice == '1':
#            pass
#        elif choice == '2':
#            pass
#        elif choice == '3':
#            pass
#        elif choice == '4':
#            options['main']()
#        else:
#            print('Invalid choice')
#            input('\nPress Enter to continue...')
#            options['settings']()
#        options['main']()
#
#    def quit():
#        os.system('clear')
#        sys.exit()
#
#    def main():
#        os.system('clear')
#        print('Crack Study')
#        print('='*11)
#        print('1) Get a problem')
#        print('2) Update problem status')
#        print('3) Show stats')
#        print('4) User settings')
#        print('\n0) Quit')
#        choice = input('\nEnter choice >> ')
#        options[choice]()
#
#    options = {
#        '1': problem,
#        '2': update,
#        '3': stats,
#        '4': settings,
#        '0': quit,
#        'main': main,
#        }
#
#    options['main']()
