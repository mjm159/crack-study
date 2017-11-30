# Standard Library
import os

# Local Modules
import problem


class Menu():

    def __init__(self):
        self.title = 'Menu'
        self.options = []
        self.prompt = '>> '

    def __display(self):
        os.system('clear')
        print(self.title)
        print('='*len(self.title))

    def display(self):
        self.__display()
        print('='*len(self.title))
        for option in self.options:
            print(option)
        in_data = input(self.prompt)
        self.selection(in_data)
    
    def selection(self, *args, **kwargs):
        MainMenu().display()


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
        self.__display()
        prob = input('\nProblem attempted (ex. 12.3) >> ')
        if not problem.valid_prob_num(prob):
            print('Invalid problem number')
            input('\nPress Enter to return to main menu...')
            self.selection()
        status = input('pass/fail/None? >> ').lower()
        status = None if status == 'none'
        if status not in ['pass', 'fail', None]:
            print('Invalid status')
            input('\nPress Enter to return to main menu...')
            self.selection()
        print('Setting problem {} to {}'.format(prob, status))
        problem.update_problem_status(data, prob, status)
        input('\nPress Enter to continue...')
        self.selection()

            
class StatsMenu(Menu):

    def __init__(self):
        self.title = 'Problem Stats'
        self.options = []
        self.prompt = '\nPress Enter to return to main menu...'

    def display(self):
        self.__display()
        data = problem.load_json_data()
        output_stats(data)
        input(self.prompt)
        self.selection()

class MainMenu(Menu):

    def __init__(self):
        self.title = 'Crack Study'
        print('1) Get a problem')
        print('2) Update problem status')
        print('3) Show stats')
        print('4) User settings')
        print('\n0) Quit')
        self.options = {
            '1': {'desc':'1) Get a problem', 'fn': pass
            }
        self.prompt = '\nEnter choice >> '

    



def menu_prompt():
    
    options = {}


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
