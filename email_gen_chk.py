import pandas as pd 
from selenium import webdriver
import random, os, sys, time, pyautogui


def main():


    ''' Script to generate potential email addresses using common names, email patterns and email providers. Use Have I Been Pwned to attempt
     to verify emails existence on the assumption if an account is real there's a reasonable chance its been involved in a breach. '''


    choice = ('y','yes','yy','yeah')


    os.system('clear')


    print('\n-----------------------------')
    print('------ EMAIL GENERATOR ------')
    print('-----------------------------')
    print('[1] Generate random emails')
    print('[2] Generate specific email')
    print('    & confirm w/ HIBP      ')


    init_prompt = int(input('\nEnter choice: '))


    time.sleep(1)
    os.system('clear')


    ### DECISION BRANCH 1 ###


    if init_prompt == 1:


        fnames_1990 = pd.read_csv('fnames_1990.csv')
        lnames = pd.read_html('https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_North_America')


        def total_names():

            os.system('clear')

            try:
                prompt = int(input('\n\nHow many names do you want to generate [ 1+ ]? '))

            except (ValueError, TypeError):
                print('Error: Enter number > 0')
                total_names()

            return prompt

        prompt = total_names()


        names = 0 
        full_name = [ ]
        while names < prompt:
            fname,  lname  =  random.choice( fnames_1990['First'] ),  random.choice( lnames[7]['Name'] )
            combined = fname.capitalize(), lname.capitalize()
            full_name.append( combined ) 
            names += 1


        def domain_prompt():

            print('\n')
            print('-' * 83)
            print(' ' * 34, 'EMAIL PROVIDERS')
            print('-' * 83)
            print('[1] gmail.com | [3] outlook.com | [5] yahoo.com | [7] aol.com | [9] icloud.com')
            print('[2] mail.ru   | [4] yandex.com  | [6] mail.com  | [8] gmx.com | [10] protonmail.com')
            print('-' * 83)

            try:
                web_prompt = int(input('\n\nEnter a choice [1-10]: '))   

            except (ValueError, TypeError):
                print('Error: Enter a number between 1-10')
                domain_prompt()

            return web_prompt

        web_prompt = domain_prompt()


        index = {1:'gmail.com', 2:'mail.ru', 3:'outlook.com', 4:'yandex.com', 5:'yahoo.com', 6:'mail.com',
                 7:'aol.com', 8:'gmx.com', 9:'icloud.com', 10:'protonmail.com'}

        web_prompt = index[web_prompt]

        emails = [ ]

        df = pd.Series()

        for a, b in full_name:
            pattern0, pattern1, pattern2 = a + '.' + b + '@' + web_prompt,  b + '.' + a + '@' + web_prompt,  a.lower() + '.' + b.lower() + '@' + web_prompt
            pattern3, pattern4, pattern5 = a + '_' + b + '@' + web_prompt,  b + '_' + a + '@' + web_prompt,  a.lower() + '_' + b.lower() + '@' + web_prompt
            pattern6, pattern7, pattern8 = a[0] + '.' + b + '@' + web_prompt,  b + '.' + a[0] + '@' + web_prompt,  a[0].lower() + '.' + b.lower() + '@' + web_prompt
            pattern9, pattern10, pattern11 = a + '.' + b[0] + '@' + web_prompt,  b[0] + '.' + a + '@' + web_prompt,  a.lower() + '.' + b[0].lower() + '@' + web_prompt
            pattern12, pattern13, pattern14 = a + b + '@' + web_prompt, b + a + '@' + web_prompt, a.lower() + b.lower() + '@' + web_prompt 
            pattern15, pattern16, pattern17 = a.lower() + b.lower() + '2' + '@' + web_prompt, b.lower() + a.lower() + '2' + '@' + web_prompt, b.lower() + '.' + a.lower() + '2' + '@' + web_prompt
            pattern18, pattern19, pattern20 = b.lower() + a.lower() + '@' + web_prompt, b[0].lower() + a.lower() + '@' + web_prompt, b.lower() + '_' + a.lower() + '@' + web_prompt
            pattern21, pattern22, pattern23 = a + '.' + b + '1' + '@' + web_prompt,  b + '.' + a + '1' + '@' + web_prompt,  a.lower() + '.' + b.lower() + '1' + '@' + web_prompt
            pattern24, pattern25, pattern26 = a + '-' + b + '@' + web_prompt, b + '-' + a + '@' + web_prompt, a.lower() + '-' + b.lower() + '@' + web_prompt 
            
            print('\n\n', a, b, ' - '  +    pattern0, pattern1, pattern2)
            print(' ' * len(a + b), '    ', pattern3, pattern4, pattern5)
            print(' ' * len(a + b), '    ', pattern6, pattern7, pattern8)
            print(' ' * len(a + b), '    ', pattern9, pattern10, pattern11)
            print(' ' * len(a + b), '    ', pattern12, pattern13, pattern14)
            print(' ' * len(a + b), '    ', pattern15, pattern16, pattern17)
            print(' ' * len(a + b), '    ', pattern18, pattern19, pattern20)
            print(' ' * len(a + b), '    ', pattern21, pattern22, pattern23)
            print(' ' * len(a + b), '    ', pattern24, pattern25, pattern26)

            emails.append([pattern0,pattern1,pattern2,pattern3,pattern4,pattern5,pattern6,pattern7,pattern8,pattern9,pattern10,pattern11,pattern12,pattern13,
                           pattern14,pattern15,pattern16,pattern17,pattern18,pattern19,pattern20,pattern21,pattern22,pattern23,pattern24,pattern25,pattern26])


        ### SAVE TO EXCEL ###

        save = input('\nDo you want to save emails [y/n]? ')

        if save.lower() in choice:
            filename = input('\nOK, enter a filename: ')
            pd.DataFrame(emails).to_excel(filename + '.xlsx')

        
        ### EXIT OR CONTINUE ###

        print('\n[1] MAIN MENU [2] EXIT')

        exit = int(input('\nENTER CHOICE: '))

        if exit == 1:
            main()

        elif exit == 2:
            time.sleep(0.5)
            os.system('clear')
            sys.exit(0)


    ### DECISION BRANCH 2 ###


    elif init_prompt == 2:


        a = input('\nEnter a first name: ')
        b = input('Enter a last name: ')


        def domain_prompt():

            print('\n')
            print('-' * 94)
            print(' ' * 42, 'EMAIL PROVIDERS')
            print('-' * 94)
            print('[1] gmail.com | [3] outlook.com | [5] yahoo.com | [7] aol.com | [9] icloud.com      | [11] all')
            print('[2] mail.ru   | [4] yandex.com  | [6] mail.com  | [8] gmx.com | [10] protonmail.com |')
            print('-' * 94)

            try:
                web_prompt = int(input('\n\nEnter a choice [1-11]: '))

            except (ValueError, TypeError):
                print('Error: Enter a number between 1-11')
                domain_prompt()

            return web_prompt

        web_prompt = domain_prompt()


        index = {1:'gmail.com', 2:'mail.ru', 3:'outlook.com', 4:'yandex.com', 5:'yahoo.com', 6:'mail.com',
                 7:'aol.com', 8:'gmx.com', 9:'icloud.com', 10:'protonmail.com'}

        
        ### CHECK *ALL* WEBMAIL DOMAINS ###


        if web_prompt == 11:

            emails = [ ]

            for domain in index.values():
                web_prompt = domain

                print(web_prompt)

                pattern0, pattern1, pattern2 = a + '.' + b + '@' + web_prompt,  b + '.' + a + '@' + web_prompt,  a.lower() + '.' + b.lower() + '@' + web_prompt
                pattern3, pattern4, pattern5 = a + '_' + b + '@' + web_prompt,  b + '_' + a + '@' + web_prompt,  a.lower() + '_' + b.lower() + '@' + web_prompt
                pattern6, pattern7, pattern8 = a[0] + '.' + b + '@' + web_prompt,  b + '.' + a[0] + '@' + web_prompt,  a[0].lower() + '.' + b.lower() + '@' + web_prompt
                pattern9, pattern10, pattern11 = a + '.' + b[0] + '@' + web_prompt,  b[0] + '.' + a + '@' + web_prompt,  a.lower() + '.' + b[0].lower() + '@' + web_prompt
                pattern12, pattern13, pattern14 = a + b + '@' + web_prompt, b + a + '@' + web_prompt, a.lower() + b.lower() + '@' + web_prompt 
                pattern15, pattern16, pattern17 = a.lower() + b.lower() + '2' + '@' + web_prompt, b.lower() + a.lower() + '2' + '@' + web_prompt, b.lower() + '.' + a.lower() + '2' + '@' + web_prompt
                pattern18, pattern19, pattern20 = b.lower() + a.lower() + '@' + web_prompt, b[0].lower() + a.lower() + '@' + web_prompt, b.lower() + '_' + a.lower() + '@' + web_prompt
                pattern21, pattern22, pattern23 = a + '.' + b + '1' + '@' + web_prompt,  b + '.' + a + '1' + '@' + web_prompt,  a.lower() + '.' + b.lower() + '1' + '@' + web_prompt
                pattern24, pattern25, pattern26 = a + '-' + b + '@' + web_prompt, b + '-' + a + '@' + web_prompt, a.lower() + '-' + b.lower() + '@' + web_prompt 

                print('\n\n', a, b, ' - '  +    pattern0, pattern1, pattern2)
                print(' ' * len(a + b), '    ', pattern3, pattern4, pattern5)
                print(' ' * len(a + b), '    ', pattern6, pattern7, pattern8)
                print(' ' * len(a + b), '    ', pattern9, pattern10, pattern11)
                print(' ' * len(a + b), '    ', pattern12, pattern13, pattern14)
                print(' ' * len(a + b), '    ', pattern15, pattern16, pattern17)
                print(' ' * len(a + b), '    ', pattern18, pattern19, pattern20)
                print(' ' * len(a + b), '    ', pattern21, pattern22, pattern23)
                print(' ' * len(a + b), '    ', pattern24, pattern25, pattern26)

                emails.append([pattern0,pattern1,pattern2,pattern3,pattern4,pattern5,pattern6,pattern7,pattern8,pattern9,pattern10,pattern11,pattern12,pattern13,
                           pattern14,pattern15,pattern16,pattern17,pattern18,pattern19,pattern20,pattern21,pattern22,pattern23,pattern24,pattern25,pattern26])


                ### SAVE TO EXCEL ###


                save = input('\nDo you want to save emails [y/n]? ')

                if save.lower() in choice:

                    filename = input('\nOK, enter a filename: ')
                    pd.DataFrame(emails).to_excel(f'{filename}.xls',sheet_name=a+b)
                     

                ### RUN THROUGH HAVE I BEEN PWNED ###

                web_check = input('\nDo you want to confirm [y/n]? ')

                if web_check in choice:

                    speed_rate = [0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19]
                    speed = random.choice(speed_rate)

                    duration_rate = random.randint(1, 2)

                    x_post = random.randint(399, 406)
                    y_post = random.randint(507, 513)
                    x_post1 = random.randint(972, 978)
                    y_post1 = random.randint(502, 508)

                    delay1 = random.randint(1, 2)
                    delay2 = random.randint(0, 1)

                    for email in emails:

                            for em_index in email:

                                web = webdriver.Firefox()
                                web.get('https://haveibeenpwned.com/')
                                pyautogui.moveTo( x_post, y_post, duration=duration_rate, tween=pyautogui.easeInOutQuad)
                                time.sleep( delay1 )
                                pyautogui.click( x_post, y_post )
                                pyautogui.write( em_index, interval=speed )
                                time.sleep( delay2 )
                                pyautogui.moveTo( x_post1, y_post1, duration=duration_rate, tween=pyautogui.easeInOutQuad)
                                pyautogui.click( x_post1, y_post1 )
                                time.sleep( 20 )
                                web.close()

                emails.clear()


            ### EXIT OR RETURN TO MAIN MENU ###
        
            print('\n[1] MAIN MENU [2] EXIT')

            exit = int(input('\nENTER CHOICE: '))

            if exit == 1:
                main()

            elif exit == 2:
                time.sleep(0.5)
                os.system('clear')
                sys.exit(0)


        ### CONTINUE WITH ONE DOMAIN SELECTION ###


        else:
            web_prompt = index[web_prompt]

        pattern0, pattern1, pattern2 = a + '.' + b + '@' + web_prompt,  b + '.' + a + '@' + web_prompt,  a.lower() + '.' + b.lower() + '@' + web_prompt
        pattern3, pattern4, pattern5 = a + '_' + b + '@' + web_prompt,  b + '_' + a + '@' + web_prompt,  a.lower() + '_' + b.lower() + '@' + web_prompt
        pattern6, pattern7, pattern8 = a[0] + '.' + b + '@' + web_prompt,  b + '.' + a[0] + '@' + web_prompt,  a[0].lower() + '.' + b.lower() + '@' + web_prompt
        pattern9, pattern10, pattern11 = a + '.' + b[0] + '@' + web_prompt,  b[0] + '.' + a + '@' + web_prompt,  a.lower() + '.' + b[0].lower() + '@' + web_prompt
        pattern12, pattern13, pattern14 = a + b + '@' + web_prompt, b + a + '@' + web_prompt, a.lower() + b.lower() + '@' + web_prompt 
        pattern15, pattern16, pattern17 = a.lower() + b.lower() + '2' + '@' + web_prompt, b.lower() + a.lower() + '2' + '@' + web_prompt, b.lower() + '.' + a.lower() + '2' + '@' + web_prompt
        pattern18, pattern19, pattern20 = b.lower() + a.lower() + '@' + web_prompt, b[0].lower() + a.lower() + '@' + web_prompt, b.lower() + '_' + a.lower() + '@' + web_prompt
        pattern21, pattern22, pattern23 = a + '.' + b + '1' + '@' + web_prompt,  b + '.' + a + '1' + '@' + web_prompt,  a.lower() + '.' + b.lower() + '1' + '@' + web_prompt
        pattern24, pattern25, pattern26 = a + '-' + b + '@' + web_prompt, b + '-' + a + '@' + web_prompt, a.lower() + '-' + b.lower() + '@' + web_prompt 


        print('\n\n', a, b, ' - '  +    pattern0, pattern1, pattern2)
        print(' ' * len(a + b), '    ', pattern3, pattern4, pattern5)
        print(' ' * len(a + b), '    ', pattern6, pattern7, pattern8)
        print(' ' * len(a + b), '    ', pattern9, pattern10, pattern11)
        print(' ' * len(a + b), '    ', pattern12, pattern13, pattern14)
        print(' ' * len(a + b), '    ', pattern15, pattern16, pattern17)
        print(' ' * len(a + b), '    ', pattern18, pattern19, pattern20)
        print(' ' * len(a + b), '    ', pattern21, pattern22, pattern23)
        print(' ' * len(a + b), '    ', pattern24, pattern25, pattern26)


        emails = [ ]
        emails.append([pattern0,pattern1,pattern2,pattern3,pattern4,pattern5,pattern6,pattern7,pattern8,pattern9,pattern10,pattern11,pattern12,pattern13,
                       pattern14,pattern15,pattern16,pattern17,pattern18,pattern19,pattern20,pattern21,pattern22,pattern23,pattern24,pattern25,pattern26])


        ### SAVE TO EXCEL ###

        save = input('\nDo you want to save emails [y/n]? ')

        if save.lower() in choice:
            filename = input('\nOK, enter a filename: ')
            pd.DataFrame(emails).to_excel(filename + '.xls', sheet_name=a + b + '_' + web_prompt)


        ### RUN THROUGH HAVE I BEEN PWNED ###

        web_check = input('\nDo you want to confirm [y/n]? ')

        if web_check in choice:

            speed_rate = [0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23]
            speed = random.choice(speed_rate)

            duration_rate = random.randint(1, 2)

            x_post = random.randint(400, 405)
            y_post = random.randint(508, 512)
            x_post1 = random.randint(973, 977)
            y_post1 = random.randint(503, 507)

            delay1 = random.randint(1, 2)
            delay2 = random.randint(0, 1)
            delay3 = random.randint(4, 8)

            for email in emails:
                    for em_index in email:

                        web = webdriver.Firefox()
                        web.get('https://haveibeenpwned.com/')
                        pyautogui.moveTo( x_post, y_post, duration=duration_rate, tween=pyautogui.easeInOutQuad)
                        time.sleep( delay1 )
                        pyautogui.click( x_post, y_post )
                        pyautogui.write( em_index, interval=speed )
                        time.sleep( delay2 )
                        pyautogui.moveTo( x_post1, y_post1, duration=duration_rate, tween=pyautogui.easeInOutQuad)
                        pyautogui.click( x_post1, y_post1 )
                        time.sleep( delay3 )


        ### EXIT OR CONTINUE ###

        print('\n[1] MAIN MENU [2] EXIT')

        exit = int(input('\nENTER CHOICE: '))

        if exit == 1:
            main()

        elif exit == 2:
            time.sleep(0.5)
            os.system('clear')
            sys.exit(0)


main()






