from local_database_commands import local_updating
from check_gotted_gift import check_got_gift
from check_buttons_creating import check_buttons_creating
from sizes import get_sizes as get_icons_sizes

import sqlite3, time
conn = sqlite3.connect('DataBase.db')
cur = conn.cursor()

from imports import *
import config

Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'fullscreen', 0)

from kivy.core.window import Window

connection = None
cursor = None


def connecting():
    global connection, cursor

    connection = pymysql.connections.Connection(
        host=config.db_host,
        port=config.db_port,
        user=config.db_user,
        password=config.db_password,
        database=config.db_database,
        cursorclass=cursors.DictCursor,
        connect_timeout=28000
    )
    cursor = connection.cursor()

try:
    connecting()
    x = True

except Exception as ex:
    x = False


local_updating(request='creating', cur=cur, conn=conn, cursor=cursor, connection=connection)
local_updating(request='update_null', cur=cur, conn=conn, cursor=cursor, connection=connection)
local_updating(request='check_import', cur=cur, conn=conn, cursor=None, connection=None)


if x is True:
    tester = 0
    sm = ScreenManager()

    cur.execute('select saved_user_id from Data0')
    x = cur.fetchone()
    conn.commit()
    res = str(x).split("('", 1)[1].split("',)")[0]

    if res != '' and res != '{}' and res:
        suid = local_updating(request='get_suid', cur=cur, conn=conn, cursor=cursor, connection=connection)
        try:
            check_got_gift(cursor=cursor, connection=connection, suid=str(suid), conn=conn, cur=cur)
        except TypeError:
            pass

    id = ''
    psw = ''
    total = ''
    def pswgen():
        global id, psw, total
        for y in range(7):
            id = id + random.choice(list('1234567890'))
        for x in range(40):
            psw = psw + random.choice(list(
                '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
        total = f'{id}:{psw}'

    icon_value = 1

    earn_button_created = 0
    boosts_button_created = 0
    frens_button_created = 0
    airdrop_button_created = 0
    icons_button_created = 0
    settings_button_created = 0

    class BackgroundTemplateWidget_ForAuthScreens(Widget):
        def __init__(self, **kwargs):
            super(BackgroundTemplateWidget_ForAuthScreens, self).__init__(**kwargs)
            with self.canvas.before:
                self.rect = Rectangle(pos=self.pos, size=self.size, source='data/Background/Background.webp')

            self.bind(size=self.update_rect, pos=self.update_rect)

        def update_rect(self, instance, value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size


    class RegisterScreen(Screen, FloatLayout):
        def __init__(self, **kwargs):
            global id, psw, total, suid
            super().__init__(**kwargs)
            from kivy.uix.textinput import TextInput
            self.orientation = "vertical"
            self.spacing = 5

            background_widget = BackgroundTemplateWidget_ForAuthScreens()
            self.add_widget(background_widget)

            self.buttons_layout = RelativeLayout(size_hint=(1, .05), pos_hint={'center_x': .5, 'bottom': 1})
            self.add_widget(self.buttons_layout)

            self.name_label = Label(text="Telegram User_ID:", pos_hint={'center_x': .5, 'center_y': .9}, font_size=get_icons_sizes(Window.width, 'label_font'), bold=True, font_name=r'data/Fonts/CormorantSC-Medium.ttf')
            self.add_widget(self.name_label)

            self.name_input = TextInput(multiline=False, hint_text_color=[255, 255, 255, 0.65],
                      hint_text="Введите ваш Telegram User_ID\n(Он был отправлен вам в боте)",
                      size_hint_x=.75, size_hint_y=0.1, pos_hint={'center_x': .5, 'center_y': .8},
                      background_normal='data/Background/Bg.webp', background_disabled_normal='data/Background/Bg.webp', background_active='data/Background/Bg.png', cursor_color=[255, 255, 255, 0.5], foreground_color=[255, 255, 255, .75], border=(5,5,5,5),
                      font_name=r'data/Fonts/CormorantSC-Light.ttf', font_size=get_icons_sizes(Window.width, 'textinput_font_size'))
            self.add_widget(self.name_input)

            self.password_label = Label(text="Игровой никнейм:", pos_hint={'center_x': .5, 'center_y': .6}, font_size=get_icons_sizes(Window.width, 'label_font'), bold=True, font_name=r'data/Fonts/CormorantSC-Medium.ttf')
            self.add_widget(self.password_label)

            self.password_input = TextInput(multiline=False, password=False, hint_text_color=[255, 255, 255, 0.65],
                        hint_text="Введите ваш игровой никнейм", size_hint_x=.75, size_hint_y=0.1,
                        pos_hint={'center_x': .5, 'center_y': .5},
                        background_normal='data/Background/Bg.webp', background_disabled_normal='data/Background/Bg.webp', background_active='data/Background/Bg.png', cursor_color=[255, 255, 255, 0.5], foreground_color=[255, 255, 255, .75], border=(5,5,5,5),
                      font_name=r'data/Fonts/CormorantSC-Light.ttf', font_size=get_icons_sizes(Window.width, 'textinput_font_size'))
            self.add_widget(self.password_input)

            self.register_status = Label(text=f"", size_hint=(1, 0.1),
                                     bold=True, pos_hint={'center_x': .5, 'center_y': .325}, font_size=get_icons_sizes(Window.width, 'label_font'), font_name=r'data/Fonts/CormorantSC-Medium.ttf')
            self.add_widget(self.register_status)

            self.register_button = Button(text="", color='white', bold=True, size_hint=(None, None), size=(get_icons_sizes(Window.width, 'button_menu'), get_icons_sizes(Window.width, 'button_menu')),
                         pos_hint={'center_x': .33}, background_normal='data/ButtonMenu/Register.png', background_down='data/ButtonMenu/Register.png')
            self.register_button.bind(on_release=self.register)
            self.buttons_layout.add_widget(self.register_button)


            self.go_to_auth_button = Button(text="", color='white', bold=True, size_hint=(None, None), size=(get_icons_sizes(Window.width, 'button_menu'), get_icons_sizes(Window.width, 'button_menu')),
                       pos_hint={'center_x': .66}, background_normal='data/ButtonMenu/SwapAuth.png', background_down='data/ButtonMenu/SwapAuth.png')
            self.go_to_auth_button.bind(on_release=self.go_to_auth)
            self.buttons_layout.add_widget(self.go_to_auth_button)

        def register(self, instance):
            global id, psw, total, suid

            wrong_value = 0

            user_id = self.name_input.text
            nickname = self.password_input.text

            if user_id and nickname:
                lst = []
                lst2 = []
                allowed_chars = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ_"

                for ex in nickname:
                    if ex not in allowed_chars:
                        wrong_value = 1
                    else:
                        pass

                cursor.execute('select username from Data')
                usns = cursor.fetchall()
                connection.commit()

                for i in usns:
                    lst.append(i['username'])

                cursor.execute('select user_id from Data')
                usids = cursor.fetchall()
                connection.commit()

                cursor.execute(f'select register_was from Data where user_id={int(user_id)}')
                rw = cursor.fetchone()
                rw = rw['register_was']
                connection.commit()

                for e in usids:
                    lst2.append(e['user_id'])

                if wrong_value == 0:
                    if int(user_id) in lst2:
                        if rw == 0:
                            if nickname in lst:
                                self.register_status.text = '! Такой никнейм уже существует !'
                            else:
                                pswgen()
                                cursor.execute('update Data set username="{}", fic_id="{}", register_was={} where user_id={}'.format(nickname, total, 1, int(user_id)))
                                connection.commit()
                                cur.execute('update Data0 set auto_auth={}, saved_user_id="{}"'.format(1, total))
                                conn.commit()
                                cursor.execute('insert into PassiveFarm(fic_id) values("{}")'.format(total))
                                connection.commit()

                                time.sleep(1)

                                local_updating(request='creating', cur=cur, conn=conn, cursor=cursor,connection=connection)
                                local_updating(request='update_null', cur=cur, conn=conn, cursor=cursor,connection=connection)
                                suid = local_updating(request='get_suid', cur=cur, conn=conn, cursor=cursor,connection=connection)

                                try:
                                    check_got_gift(cursor=cursor, connection=connection, suid=str(suid))
                                except TypeError:
                                    pass

                                screens = []

                                cursor.execute('select access from Data where fic_id="{}"'.format(str(suid)))
                                acs = cursor.fetchone()
                                acs = acs['access']
                                connection.commit()

                                if acs == 1:
                                    screens = [('main', FigmentInterplanetaryCoin()), ('boosts', BoostsScreen()),
                                               ('frens', FrensScreen()),
                                               ('airdrop', AirDropScreen()), ('icons', IconsScreen()),
                                               ('more_icons', MoreIconScreen()), ('settings', SettingsScreen()),
                                               ('passive_farm', PassiveFarmScreen()), ('ps_setups', SetupScreen()),
                                               ('blocked', BlockedAccessScreen()), ('works', BlockedWorksScreen(acs))]
                                elif acs == 0:
                                    screens = [('blocked', BlockedAccessScreen())]
                                elif acs == 2 or acs == 3:
                                    screens = [('works', BlockedWorksScreen(acs))]

                                for name, screen in screens:
                                    screen.name = name
                                    sm.add_widget(screen)

                                for screen in sm.children:
                                    screen.manager = sm

                                self.manager.transition.direction = 'up'
                                self.manager.current = 'main'

                                return sm
                        else:
                            self.register_status.text = '! Вы уже были зарегистрированы !'
                    else:
                        self.register_status.text = '! Такого user_id нет в базе данных !'
                else:
                    self.register_status.text = '! Недопустимые символы в никнейме !'
            else:
                self.register_status.text = '! Заполните все поля !'

        def go_to_auth(self, instance):
            self.manager.transition.direction = 'left'
            self.manager.current = 'auth'


    class AuthScreen(Screen, FloatLayout):
        def __init__(self, **kwargs):
            global id, psw, total, suid
            super().__init__(**kwargs)
            from kivy.uix.textinput import TextInput
            self.orientation = "vertical"
            self.spacing = 5

            background_widget = BackgroundTemplateWidget_ForAuthScreens()
            self.add_widget(background_widget)

            self.buttons_layout = RelativeLayout(size_hint=(1, .05), pos_hint={'center_x': .5, 'bottom': 1})
            self.add_widget(self.buttons_layout)

            self.id_label = Label(text="FIC ID:", pos_hint={'center_x': .5, 'center_y': .9}, font_size=get_icons_sizes(Window.width, 'label_font'), bold=True, font_name=r'data/Fonts/CormorantSC-Medium.ttf')
            self.add_widget(self.id_label)

            self.id_input = TextInput(multiline=False, password=True, hint_text_color=[255, 255, 255, 0.65],
                                      hint_text="Введите ваш FIC ID",
                                      size_hint_x=.75, size_hint_y=0.1, pos_hint={'center_x': .5, 'center_y': .8},
                                      background_normal='data/Background/Bg.webp', background_disabled_normal='data/Background/Bg.webp', background_active='data/Background/Bg.png', cursor_color=[255, 255, 255, 0.5], foreground_color=[255, 255, 255, .75], border=(5,5,5,5),
                      font_name=r'data/Fonts/CormorantSC-Light.ttf', font_size=get_icons_sizes(Window.width, 'textinput_font_size'))
            self.add_widget(self.id_input)

            self.auth_status = Label(text=f"", size_hint=(1, 0.1),
                                     bold=True, pos_hint={'center_x': .5, 'center_y': .65}, font_size=get_icons_sizes(Window.width, 'label_font'), font_name=r'data/Fonts/CormorantSC-Medium.ttf')
            self.add_widget(self.auth_status)

            self.auth_button = Button(text="", color='white', bold=True, size_hint=(None, None), size=(
            get_icons_sizes(Window.width, 'button_menu'), get_icons_sizes(Window.width, 'button_menu')),
                                          pos_hint={'center_x': .66},
                                          background_normal='data/ButtonMenu/LogIn.png',
                                          background_down='data/ButtonMenu/LogIn.png')
            self.auth_button.bind(on_release=self.oauth)
            self.buttons_layout.add_widget(self.auth_button)

            self.go_to_register_button = Button(text="", color='white', bold=True, size_hint=(None, None), size=(
                get_icons_sizes(Window.width, 'button_menu'), get_icons_sizes(Window.width, 'button_menu')),
                                                pos_hint={'center_x': .33},
                                                background_normal='data/ButtonMenu/SwapAuth.png',
                                                background_down='data/ButtonMenu/SwapAuth.png')
            self.go_to_register_button.bind(on_release=self.go_to_register)
            self.buttons_layout.add_widget(self.go_to_register_button)

        def oauth(self, instance):
            global id, psw, total, suid
            fic_id = self.id_input.text

            if fic_id:
                lst = []

                cursor.execute('select fic_id from Data')
                sid1 = cursor.fetchall()
                connection.commit()

                for i in sid1:
                    lst.append(i['fic_id'])

                if fic_id in lst:
                    cur.execute('update Data0 set auto_auth={}, saved_user_id="{}"'.format(1, fic_id))
                    conn.commit()

                    time.sleep(1)

                    local_updating(request='creating', cur=cur, conn=conn, cursor=cursor, connection=connection)
                    local_updating(request='update_null', cur=cur, conn=conn, cursor=cursor, connection=connection)
                    suid = local_updating(request='get_suid', cur=cur, conn=conn, cursor=cursor, connection=connection)

                    try:
                        check_got_gift(cursor=cursor, connection=connection, suid=str(suid))
                    except TypeError:
                        pass

                    screens = []

                    cursor.execute('select access from Data where fic_id="{}"'.format(str(suid)))
                    acs = cursor.fetchone()
                    acs = acs['access']
                    connection.commit()

                    if acs == 1:
                        screens = [('main', FigmentInterplanetaryCoin()), ('boosts', BoostsScreen()), ('frens', FrensScreen()),
                                   ('airdrop', AirDropScreen()), ('icons', IconsScreen()),
                                   ('more_icons', MoreIconScreen()), ('settings', SettingsScreen()),
                                   ('passive_farm', PassiveFarmScreen()), ('ps_setups', SetupScreen()),
                                   ('blocked', BlockedAccessScreen()), ('works', BlockedWorksScreen(acs))]
                    elif acs == 0:
                        screens = [('blocked', BlockedAccessScreen())]
                    elif acs == 2 or acs == 3:
                        screens = [('works', BlockedWorksScreen(acs))]

                    for name, screen in screens:
                        screen.name = name
                        sm.add_widget(screen)

                    for screen in sm.children:
                        screen.manager = sm

                    self.manager.transition.direction = 'up'
                    self.manager.current = 'main'

                    return sm

                else:
                    self.auth_status.text = '! FIC ID введен неверно !'
            else:
                self.auth_status.text = '! Заполните все поля !'

        def go_to_register(self, instance):
            self.manager.transition.direction = 'right'
            self.manager.current = 'register'


    class BlockedAccessScreen(Screen, RelativeLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.label_blocked_name = (
                Label(
                    text='FIC App',
                    size_hint=(None, None),
                    bold=True,
                    font_size=get_icons_sizes(Window.width, 'label_font'),
                    pos_hint={'center_x': .5, 'top': 1}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
                )
            )
            self.add_widget(self.label_blocked_name)

            self.coin_button = Button(text="",
                                      size_hint=(None, None),
                                      size=(get_icons_sizes(Window.width, 'coin'), get_icons_sizes(Window.width, 'coin')),
                                      pos_hint={'center_x': .5, 'center_y': .5},
                                      bold=True,
                                      background_normal='data/Icons/blocked.png',
                                      background_down='data/Icons/blocked.png',
                                      border=(0, 0, 0, 0)
                                      )
            self.coin_button.bind(on_press=self.on_coin_click)
            self.add_widget(self.coin_button)

            type_blocking_text = 'В Приложении и Боте'

            self.label_blocked = (
                Label(
                    text=f'Вы были заблокированы\n{type_blocking_text}...',
                    size_hint=(None, None),
                    bold=False,
                    font_size=get_icons_sizes(Window.width, 'label_font'),
                    pos_hint={'center_x': .5, 'center_y': .1}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
                )
            )
            self.add_widget(self.label_blocked)

        def update(self):
            cursor.execute('select vibration from Data where fic_id="{}"'.format(str(suid)))
            self.vibration = cursor.fetchone()
            self.vibration = self.vibration['vibration']

        def on_coin_click(self, instance):
            anim = (Animation(size=((get_icons_sizes(Window.width, 'coin')) - 20, (get_icons_sizes(Window.width, 'coin')) - 20),duration=.05) + Animation(size=((get_icons_sizes(Window.width, 'coin')), (get_icons_sizes(Window.width, 'coin'))),duration=.05))
            anim.start(self.coin_button)

    class BlockedWorksScreen(Screen, RelativeLayout):
        def __init__(self, type_works, **kwargs):
            super().__init__(**kwargs)
            self.label_blocked_name = (
                Label(
                    text='FIC App',
                    size_hint=(None, None),
                    bold=True,
                    font_size=get_icons_sizes(Window.width, 'label_font'),
                    pos_hint={'center_x': .5, 'top': 1}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
                )
            )
            self.add_widget(self.label_blocked_name)

            self.coin_button = Button(text="",
                                      size_hint=(None, None),
                                      size=(get_icons_sizes(Window.width, 'coin'), get_icons_sizes(Window.width, 'coin')),
                                      pos_hint={'center_x': .5, 'center_y': .5},
                                      bold=True,
                                      background_normal='data/Icons/blocked.png',
                                      background_down='data/Icons/blocked.png',
                                      border=(0, 0, 0, 0)
                                      )
            self.coin_button.bind(on_press=self.on_coin_click)
            self.add_widget(self.coin_button)

            type_works_text = ''
            if type_works == 3:
                type_works_text = 'В Приложении и Боте'
            elif type_works == 2:
                type_works_text = 'В Приложении'

            self.label_blocked = (
                Label(
                    text=f'Ведутся тех. работы\n{type_works_text}!',
                    size_hint=(None, None),
                    bold=False,
                    font_size=get_icons_sizes(Window.width, 'label_font'),
                    pos_hint={'center_x': .5, 'center_y': .1}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
                )
            )
            self.add_widget(self.label_blocked)

        def update(self):
            cursor.execute('select vibration from Data where fic_id="{}"'.format(str(suid)))
            self.vibration = cursor.fetchone()
            self.vibration = self.vibration['vibration']

        def on_coin_click(self, instance):
            anim = (Animation(size=((get_icons_sizes(Window.width, 'coin')) - 20, (get_icons_sizes(Window.width, 'coin')) - 20),duration=.05) + Animation(size=((get_icons_sizes(Window.width, 'coin')), (get_icons_sizes(Window.width, 'coin'))),duration=.05))
            anim.start(self.coin_button)


    class BackgroundTemplateWidget(Widget):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.rect = None
            self.update_background()
            self.bind(size=self.update_rect, pos=self.update_rect)

        def update_background(self):
            self.canvas.before.clear()
            with self.canvas.before:
                cursor.execute('select background from Data where fic_id="{}"'.format(str(suid)))
                bgtype = cursor.fetchone()['background']
                connection.commit()
                if bgtype == 1:
                    self.rect = Rectangle(pos=self.pos, size=self.size, source='data/Background/Bg.webp')
                else:
                    Color(rgb=(0, 0, 0))
                    self.rect = Rectangle(pos=self.pos, size=self.size)
            self.update_rect(self, self.size)

        def update_rect(self, instance, value):
            if self.rect:
                self.rect.pos = instance.pos
                self.rect.size = value

    class BackgroundManager:
        def __init__(self, screen):
            self.screen = screen
            self.background_widget = BackgroundTemplateWidget()
            self.screen.add_widget(self.background_widget)
            self.update_background()
            self.background_widget.bind(size=self.on_size)

        def update_background(self):
            self.background_widget.update_background()

        def on_size(self, instance, value):
            if hasattr(self.background_widget, 'rect'):
                self.background_widget.rect.size = value


    class NavigationBar(RelativeLayout):
        def __init__(self, screen_manager, button_creating_on_screen_checker, **kwargs):
            super().__init__(**kwargs)
            self.button_creating_on_screen_checker = button_creating_on_screen_checker
            self.screen_manager = screen_manager
            self.size_hint = (1, 0.05)
            self.create_buttons()

        def create_buttons(self):
            if self.button_creating_on_screen_checker == 0:
                def create_button(text, screen_name, pos_hint, button_id):
                    button = Button(
                        text="",
                        size_hint=(None, None),
                        size=(get_icons_sizes(Window.width, 'button_menu'), get_icons_sizes(Window.width, 'button_menu')),
                        pos_hint=pos_hint,
                        bold=True,
                        background_normal=f'data/ButtonMenu/{text}.png',
                        background_down=f'data/ButtonMenu/{text}.png'
                    )
                    button.bind(on_release=lambda x: self.transition_to_screen(screen_name))
                    self.add_widget(button)
                    setattr(self.ids, button_id, button)

                create_button("Earn", "main", {'center_x': .1, 'bottom': 1}, 'earn_button')
                create_button("Boosts", "boosts", {'center_x': .266, 'bottom': 1}, 'boosts_button')
                create_button("Frens", "frens", {'center_x': .42, 'bottom': 1}, 'frens_button')
                create_button("AirDrop", "airdrop", {'center_x': .58, 'bottom': 1}, 'airdrop_button')
                create_button("Icons", "icons", {'center_x': .728, 'bottom': 1}, 'icons_button')
                create_button("Settings", "settings", {'center_x': .9, 'bottom': 1}, 'settings_button')
            else:
                pass

        def transition_to_screen(self, screen_name):
            if self.screen_manager is not None:
                cursor.execute('select access, vibration from Data where fic_id="{}"'.format(str(suid)))
                acss_vib = cursor.fetchone()
                acss = acss_vib['access']
                connection.commit()

                if acss == 1:
                    screen = self.screen_manager.get_screen(screen_name)
                    if hasattr(screen, 'background_manager'):
                        screen.background_manager.update_background()
                    if screen_name in ['boosts', 'frens']:
                        screen.update()
                    elif screen_name == 'main':
                        screen.update_tokens()
                    self.screen_manager.current = screen_name
                    self.screen_manager.transition.direction = 'left'
                elif acss == 0:
                    self.screen_manager.get_screen('blocked').update()
                    self.screen_manager.current = 'blocked'
                elif acss == 2:
                    self.screen_manager.get_screen('works').update()
                    self.screen_manager.current = 'works'
            else:
                print("Error: ScreenManager -> None")


    class FigmentInterplanetaryCoin(Screen, RelativeLayout):
        def __init__(self, **kwargs):
            global suid
            super().__init__(**kwargs)

            cursor.execute('select * from Data where fic_id="{}"'.format(str(suid)))
            x = cursor.fetchone()
            connection.commit()

            self.tokens = x['tokens']
            self.boost1 = x['boost_coin_per_tap']
            self.boost2 = x['boost_charge_full']
            self.skin = x['skin']
            self.conditions = x['conditions']
            self.alltime_conditions = x['alltime_conditions']
            self.vibration = x['vibration']

            import dict
            boosts_dictionary = dict.boosts_dict
            skin_value_dictionary = dict.icon_values_dict

            self.tap = ((((((boosts_dictionary['boost1'])[0])['level'])[0])[self.boost1])[0])['tap']
            self.conditions_full = ((((((boosts_dictionary['boost2'])[0])['level'])[0])[self.boost2])[0])['conditions_full']

            if self.conditions != self.conditions_full:
                self.alltime_conditions += (self.conditions_full - self.conditions)
                self.conditions += (self.conditions_full - self.conditions)

                cursor.execute('update Data set conditions={}, alltime_conditions={} where fic_id="{}"'.format(self.conditions, self.alltime_conditions, str(suid)))
                connection.commit()

            self.background_manager = BackgroundManager(self)

            self.orientation = 'vertical'
            self.padding = 0
            self.spacing = 170
            self.score_label = Label(text=f"\nFICs: {round(self.tokens, 6)}\nКондиции: {self.conditions}", size_hint=(1, 0.1), bold=True, pos_hint={'center_x': .5, 'top': 1}, font_size=get_icons_sizes(Window.width, 'label_font'), font_name=r'data/Fonts/CormorantSC-Bold.ttf')
            self.add_widget(self.score_label)

            self.skin_value = skin_value_dictionary[self.skin]

            self.coin_button = Button(text="",
                                      size_hint=(None, None),
                                      size=(get_icons_sizes(Window.width, 'coin'), get_icons_sizes(Window.width, 'coin')),
                                      pos_hint={'center_x': .5, 'center_y': .5},
                                      bold = True,
                                      background_normal = self.skin_value,
                                      background_down = self.skin_value,
                                      border=(0, 0, 0, 0)
                                      )
            self.coin_button.bind(on_press=self.on_coin_click)
            self.add_widget(self.coin_button)

            self.passive_farming_button = Button(
                text="",
                size_hint=(None, None),
                size=((get_icons_sizes(Window.width, 'passive_farm_button_size')), (get_icons_sizes(Window.width, 'passive_farm_button_size'))),
                pos_hint={'right': 1, 'top': 1},
                bold=True,
                background_normal = r'data/ButtonMenu/PassiveFarm.png',
                background_down = r'data/ButtonMenu/PassiveFarm.png'
            )
            self.passive_farming_button.bind(on_press=self.go_to_passive_farm_screen)
            self.add_widget(self.passive_farming_button)

            self.update_tokens()

        def on_coin_click(self, instance):
            global suid

            anim = (Animation(size=((get_icons_sizes(Window.width, 'coin')) - 20, (get_icons_sizes(Window.width, 'coin')) - 20), duration=.05) + Animation(
                size=(get_icons_sizes(Window.width, 'coin'), get_icons_sizes(Window.width, 'coin')), duration=.05))
            anim.start(self.coin_button)

            if (self.conditions - self.tap) < 0:
                pass
            else:
                self.tokens += 1 * self.tap
                self.alltime_tokens = self.tokens
                self.conditions -= self.tap
                if self.vibration == 1:
                    try:
                        vibrator.vibrate(0.1)
                    except Exception as e:
                        pass
                else:
                    pass

            self.score_label.text = f"\nFICs: {round(self.tokens, 2)}\nКондиции: {self.conditions}"
            self.score_label.font_size = get_icons_sizes(Window.width, 'label_font')

            cursor.execute('update Data set tokens={}, conditions={}, alltime_taps={}, alltime_tokens={} where fic_id="{}"'.format(self.tokens, self.conditions, (self.alltime_taps+1), self.alltime_tokens, str(suid)))

        def update_tokens(self):
            cursor.execute('select * from Data where fic_id="{}"'.format(str(suid)))
            x = cursor.fetchone()
            connection.commit()

            self.tokens = x['tokens']
            self.boost1 = x['boost_coin_per_tap']
            self.boost2 = x['boost_charge_full']
            self.skin = x['skin']
            self.conditions = x['conditions']
            self.alltime_tokens = x['alltime_tokens']
            self.alltime_conditions = x['alltime_conditions']
            self.alltime_taps = x['alltime_taps']
            self.vibration = x['vibration']

            import dict
            boosts_dictionary = dict.boosts_dict
            skin_value_dictionary = dict.icon_values_dict

            self.tap = ((((((boosts_dictionary['boost1'])[0])['level'])[0])[self.boost1])[0])['tap']
            self.conditions_full = ((((((boosts_dictionary['boost2'])[0])['level'])[0])[self.boost2])[0])['conditions_full']

            self.skin_value = skin_value_dictionary[self.skin]

            self.score_label.text = f"\nFICs: {round(self.tokens, 6)}\nКондиции: {self.conditions}"
            self.coin_button.background_normal = self.skin_value
            self.coin_button.background_down = self.skin_value

        def on_pre_enter(self):
            global earn_button_created
            button_creating_on_screen_checker = check_buttons_creating('earn', earn_button_created=earn_button_created,
                                                                       boosts_button_created=None,
                                                                       frens_button_created=None,
                                                                       airdrop_button_created=None,
                                                                       icons_button_created=None,
                                                                       settings_button_created=None)
            self.add_widget(NavigationBar(self.manager, button_creating_on_screen_checker))
            earn_button_created = 1

        def on_pre_leave(self):
            connection.commit()

        def go_to_passive_farm_screen(self, instance):
            self.manager.transition.direction = 'right'
            self.manager.get_screen('passive_farm').update()
            self.manager.current = 'passive_farm'


    class BoostsScreen(Screen, RelativeLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.background_manager = BackgroundManager(self)

            self.info = Label(
                text=f'''FIC Boosts''',
                bold=True,
                font_size=get_icons_sizes(Window.width, 'label_font'),
                size_hint=(None, None), pos_hint={'center_x': .5, 'top': 1}, font_name=r'data/Fonts/CormorantSC-Bold.ttf'
            )
            self.add_widget(self.info)

            import dict
            self.boosts_dictionary = dict.boosts_dict

            self.boosts_layout_box = BoxLayout(orientation='vertical', size_hint=(1, .05), pos_hint={'center_x': .5, 'center_y': .5})
            self.boosts_layout_box.spacing = get_icons_sizes(Window.width, 'boost_layout_spacing')
            self.add_widget(self.boosts_layout_box)

            self.boost_layout_1 = RelativeLayout(size_hint=(1, .05), pos_hint={'center_x': .45, 'center_y': .7})
            self.boost_layout_2 = RelativeLayout(size_hint=(1, .05), pos_hint={'center_x': .45, 'center_y': .4})
            self.boosts_layout_box.add_widget(self.boost_layout_1)
            self.boosts_layout_box.add_widget(self.boost_layout_2)

            self.info_boost_1 = None
            self.info_boost_2 = None
            self.boost_1_button = None
            self.boost_2_button = None

        def update(self):
            self.fetch_boost_data()
            self.update_widgets_boosts()

        def fetch_boost_data(self):
            global boost1
            cursor.execute(
                'select vibration, boost_charge_full, boost_coin_per_tap, tokens, conditions, alltime_conditions, level from Data where fic_id="{}"'.format(
                    str(suid)))
            sob1b2 = cursor.fetchone()
            connection.commit()
            self.vibration_switch = int(sob1b2['vibration'])
            self.boost1 = int(sob1b2['boost_coin_per_tap'])
            self.boost2 = int(sob1b2['boost_charge_full'])
            self.tokens = int(sob1b2['tokens'])
            self.conditions = int(sob1b2['conditions'])
            self.alltime_conditions_db = int(sob1b2['alltime_conditions'])
            self.level_db = int(sob1b2['level'])

            self.tap = ((((((self.boosts_dictionary['boost1'])[0])['level'])[0])[self.boost1])[0])['tap']
            self.description_boost1 = ((self.boosts_dictionary['boost1'])[0])['description']
            if self.boost1 <= 4:
                self.price_boost1 = ((((((self.boosts_dictionary['boost1'])[0])['level'])[0])[self.boost1])[0])['price_boost1']
                self.buy_boost1 = ((((((self.boosts_dictionary['boost1'])[0])['level'])[0])[self.boost1])[0])['buy_boost1']
                self.info_boost_1_label_text = f'''{self.description_boost1}\n\nТвое количество очков FIC за 1 тап — {self.tap}\nСледующий уровень — {self.price_boost1}'''
            else:
                self.info_boost_1_label_text = f'''{self.description_boost1}\n\nТвое количество очков FIC за 1 тап — {self.tap}'''

            self.conditions_full = ((((((self.boosts_dictionary['boost2'])[0])['level'])[0])[self.boost2])[0])[
                'conditions_full']
            self.description_boost2 = ((self.boosts_dictionary['boost2'])[0])['description']
            self.level = ((((((self.boosts_dictionary['boost2'])[0])['level'])[0])[self.boost2])[0])['lvl']
            if self.boost2 <= 6:
                self.price_boost2 = ((((((self.boosts_dictionary['boost2'])[0])['level'])[0])[self.boost2])[0])[
                    'price_boost2']
                self.buy_boost2 = ((((((self.boosts_dictionary['boost2'])[0])['level'])[0])[self.boost2])[0])['buy_boost2']
                self.info_boost_2_label_text = f'''{self.description_boost2}\n\nТвое Максимальное количество\nКондиций — {self.conditions_full}\nСледующий уровень — {self.price_boost2}'''
            else:
                self.info_boost_2_label_text = f'''{self.description_boost2}\n\nТвое Максимальное количество\nКондиций — {self.conditions_full}'''

        def update_widgets_boosts(self):
            self.boost_layout_1.clear_widgets()
            self.boost_layout_2.clear_widgets()

            self.info_boost_1 = Label(
                text=f'''{self.description_boost1}\n\nТвое количество очков FIC за 1 тап — {self.tap}\nСледующий уровень — {self.price_boost1}''' if self.boost1 <= 4 else
                f'''{self.description_boost1}\n\nТвое количество очков FIC за 1 тап — {self.tap}''',
                font_size=get_icons_sizes(Window.width, 'boost_label_font'),
                size_hint=(None, None),
                pos_hint={'center_x': .75, 'center_y': .5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
            )
            self.boost_1_button = Button(
                text="",
                size_hint=(None, None),
                size=(get_icons_sizes(Window.width, 'boost_button_sizes'), get_icons_sizes(Window.width, 'boost_button_sizes')),
                pos_hint={'center_x': .25, 'center_y': .5},
                bold=True,
                background_normal='data/ButtonMenu/Boost1.png',
                background_down='data/ButtonMenu/Boost1.png'
            )

            self.info_boost_2 = Label(text=f'''{self.description_boost2}\n\nТвое Максимальное количество\nКондиций — {self.conditions_full}\nСледующий уровень — {self.price_boost2}''' if self.boost2 <= 6 else
                f'''{self.description_boost2}\n\nТвое Максимальное количество\nКондиций — {self.conditions_full}''',
                font_size=get_icons_sizes(Window.width, 'boost_label_font'),
                size_hint=(None, None),
                pos_hint={'center_x': .75, 'center_y': .5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
            )
            self.boost_2_button = Button(
                text="",
                size_hint=(None, None),
                size=(get_icons_sizes(Window.width, 'boost_button_sizes'), get_icons_sizes(Window.width, 'boost_button_sizes')),
                pos_hint={'center_x': .25, 'center_y': .5},
                bold=True,
                background_normal='data/ButtonMenu/Boost2.png',
                background_down='data/ButtonMenu/Boost2.png'
            )

            if self.boost1 <= 4:
                if self.tokens >= self.buy_boost1:
                    self.boost_1_button.bind(on_release=lambda instance: self.Successfull_Payment_Boost(1))
                else:
                    if self.vibration_switch == 1:
                        self.boost_1_button.bind(on_press=self.vibration)
            else:
                pass

            if self.boost2 <= 6:
                if self.tokens >= self.buy_boost2:
                    self.boost_2_button.bind(on_release=lambda instance: self.Successfull_Payment_Boost(2))
                else:
                    if self.vibration_switch == 1:
                        self.boost_2_button.bind(on_press=self.vibration)
            else:
                pass

            self.boost_layout_1.add_widget(self.boost_1_button)
            self.boost_layout_1.add_widget(self.info_boost_1)
            self.boost_layout_2.add_widget(self.boost_2_button)
            self.boost_layout_2.add_widget(self.info_boost_2)

        def Successfull_Payment_Boost(self, boost_value):
            if boost_value == 1:
                update_data_col = 'boost_coin_per_tap'
                update_data_col_val = self.boost1 + 1
                price = self.tokens - self.buy_boost1
                cursor.execute(
                    'update Data set {}={}, tokens={} where fic_id="{}"'.format(update_data_col, update_data_col_val, price,
                                                                                str(suid)))
                connection.commit()
                self.boost1 = update_data_col_val
                self.tokens = price
                boost1 = self.boost1

            elif boost_value == 2:
                update_data_col = 'boost_charge_full'
                update_data_col_val = self.boost2 + 1
                price = self.tokens - self.buy_boost2
                alltime_conditions = (self.alltime_conditions_db + (self.conditions_full - self.conditions))
                conds = ((((((self.boosts_dictionary['boost2'])[0])['level'])[0])[update_data_col_val])[0])[
                    'conditions_full']
                level = update_data_col_val

                cursor.execute(
                    'update Data set {}={}, tokens={}, conditions={}, level={}, alltime_conditions={} where fic_id="{}"'.format(
                        update_data_col, update_data_col_val, price, conds, level, alltime_conditions, str(suid)))
                connection.commit()
                self.boost2 = update_data_col_val
                self.tokens = price
                self.conditions = conds
                self.level_db = level
                self.alltime_conditions_db = alltime_conditions
                boost2 = self.boost2

            self.manager.get_screen('main').update_tokens()
            self.manager.current = 'main'

        def vibration(self, instance):
            random_choice = random.randint(0, 1)
            if random_choice == 0:
                try:
                    vibrator.vibrate(0.175)
                    vibrator.vibrate(0.175)
                except Exception as e:
                    passpass
            else:
                try:
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                except Exception as e:
                    pass

        def on_pre_enter(self):
            global boosts_button_created
            button_creating_on_screen_checker = check_buttons_creating('boosts', earn_button_created=None,
                                                                       boosts_button_created=boosts_button_created,
                                                                       frens_button_created=None,
                                                                       airdrop_button_created=None,
                                                                       icons_button_created=None,
                                                                       settings_button_created=None)
            self.add_widget(NavigationBar(self.manager, button_creating_on_screen_checker))
            boosts_button_created = 1

    class FrensScreen(Screen, RelativeLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.background_manager = BackgroundManager(self)

            self.info = (
                Label(
                    text=f'''FIC Frens''',
                    bold=True,
                    font_size=get_icons_sizes(Window.width, 'label_font'),
                    size_hint=(None, None), pos_hint={'center_x': .5, 'top': 1}, font_name=r'data/Fonts/CormorantSC-Bold.ttf'
                )
            )
            self.add_widget(self.info)

            self.all_frens = None
            self.get_link_button = None

        def update(self):
            self.fetch_frens_data()
            self.update_widgets_frens()

        def fetch_frens_data(self):
            frens_list = []
            self.text_frens = ''
            cursor.execute('select referrals from Data where fic_id="{}"'.format(str(suid)))
            frens_db = cursor.fetchone()

            if frens_db['referrals'] != '' or frens_db['referrals'] is None:
                frens_db_for_cycle = str(frens_db['referrals']).split(',')
                for frens_data in frens_db_for_cycle:
                    frens_list.append(frens_data)

                try:
                    for one_lst in frens_list:
                        cursor.execute('select username, username_tg, was_added_as_fren_datetime from Data where user_id={}'.format(int(one_lst)))
                        usrnme = cursor.fetchone()
                        usrnme_datetime = usrnme['was_added_as_fren_datetime']
                        usrnme_tg = usrnme['username_tg']
                        usrnme = usrnme['username']
                        connection.commit()

                        if usrnme == '' or usrnme is None:
                            if usrnme_tg in ['None', '@None']:
                                fren_username = f'TG: Без никнейма'
                            else:
                                fren_username = f'TG: {usrnme_tg}'
                            usrnme_stats = 'Еще не поиграл'
                        else:
                            fren_username = f'FIC: {usrnme}'
                            cursor.execute('select alltime_tokens from Data where username="{}"'.format(str(usrnme)))
                            usrnme_stats = cursor.fetchone()
                            usrnme_stats = usrnme_stats['alltime_tokens']
                            connection.commit()

                        self.text_frens += f'{fren_username} — {usrnme_stats} FIC\nДобавлен: {usrnme_datetime}\n\n'
                except:
                    if frens_db['referrals'] == '' or frens_db['referrals'] is None:
                        pass
                    else:
                        self.text_frens += f'У тебя есть несуществующие друзья!\n\nДобро пожаловать в блэклист!'
                        cursor.execute('update Data set access=0 where fic_id="{}"'.format(str(suid)))
                        connection.commit()

            else:
                self.text_frens += f'Тут будет отображаться список твоих друзей\n\nЗа каждое добавление,\nты и твой друг получаете\nпо 100к очков FIC и Новый Скин\n\n\nПригласить друзей можно по кнопке ниже!'

        def update_widgets_frens(self):
            if hasattr(self, 'gridlayout1') and self.gridlayout1:
                self.remove_widget(self.gridlayout1)

            if 'Тут будет отображаться список' in self.text_frens:
                self.spacing = get_icons_sizes(Window.width, 'frens_layout_spacing_no_frens')
            elif 'Тут будет отображаться список' not in self.text_frens:
                self.spacing = get_icons_sizes(Window.width, 'frens_layout_spacing')

            self.gridlayout1 = BoxLayout(orientation='vertical', pos_hint={'center_x': .5, 'center_y': .5},size_hint=(1, .05))
            self.gridlayout1.spacing = self.spacing

            self.add_widget(self.gridlayout1)

            self.gridlayout1.clear_widgets()

            self.all_frens = (
                Label(
                    text=self.text_frens,
                    font_size=get_icons_sizes(Window.width, 'label_frens_font'),
                    size_hint=(None, None),
                    pos_hint={'center_x': .5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
                )
            )
            self.gridlayout1.add_widget(self.all_frens)

            if 'Тут будет отображаться список' in self.text_frens:
                self.get_link_button = (
                    Button(text=f'', size_hint=(None, None), size=(get_icons_sizes(Window.width, 'horizontal_rectangle_buttons_width'), get_icons_sizes(Window.width, 'horizontal_rectangle_buttons_height')),
                                       pos_hint={'center_x': .5, 'bottom': 1}, color='white', bold=True, background_normal='data/ButtonMenu/InviteFren.png', background_down='data/ButtonMenu/InviteFren.png',
                                       font_size=20))
                self.get_link_button.bind(on_release=self.get_my_ref_link)
                self.gridlayout1.add_widget(self.get_link_button)
            else:
                pass

        def get_my_ref_link(self, instance):
            cursor.execute('select referral_link from Data where fic_id="{}"'.format(str(suid)))
            self.referral_link = cursor.fetchone()
            self.referral_link = self.referral_link['referral_link']
            self.referral_text = '%0AДавай%20зарабатывать%20вместе%20со%20мной%20в%20FIC!%0A%0AНажми%20ниже,%20чтобы%20присоединиться%20к%20веселью.%20🌟'
            webbrowser.open(f'https://t.me/share/url?url={self.referral_link}{self.referral_text}')

        def on_pre_enter(self):
            global frens_button_created
            button_creating_on_screen_checker = check_buttons_creating('frens', earn_button_created=None,
                                                                       boosts_button_created=None,
                                                                       frens_button_created=frens_button_created,
                                                                       airdrop_button_created=None,
                                                                       icons_button_created=None,
                                                                       settings_button_created=None)
            self.add_widget(NavigationBar(self.manager, button_creating_on_screen_checker))
            frens_button_created = 1

    class AirDropScreen(Screen, RelativeLayout):
        rotate_value_angle = NumericProperty(0)
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.background_manager = BackgroundManager(self)

            self.info = (
                Label(
                    text=f'''FIC AirDrop''',
                    bold=True,
                    font_size=get_icons_sizes(Window.width, 'label_font'),
                    size_hint=(None, None), pos_hint={'center_x': .5, 'top': 1}, font_name=r'data/Fonts/CormorantSC-Bold.ttf'
                )
            )
            self.add_widget(self.info)

            airdrop_info_layout = BoxLayout(orientation='vertical', size_hint=(.5, 1),pos_hint={'center_x': .5, 'center_y': (get_icons_sizes(Window.width, 'airdrop_box_layout_center_y'))})

            self.airdrop_button = Button(text="",
                                       size_hint=(None, None),
                                       size=(get_icons_sizes(Window.width, 'airdrop_button_sizes'),
                                             get_icons_sizes(Window.width, 'airdrop_button_sizes')),
                                       pos_hint={'center_x': .5},
                                       bold=True,
                                       background_normal='data/Icons/airdrop.png',
                                       background_down='data/Icons/airdrop.png',
                                       border = (0, 0, 0, 0)
                                       )
            self.airdrop_button.bind(on_press=self.on_airdrop_tap, on_release=self.on_release_airdrop_tap)

            self.airdrop_info = (
                Label(
                    text="Скоро будет...",
                    bold=False,
                    font_size=get_icons_sizes(Window.width, 'label_font'),
                    size_hint=(None, None),
                    pos_hint={'center_x': .5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
                )
            )

            airdrop_info_layout.add_widget(self.airdrop_button)
            airdrop_info_layout.add_widget(self.airdrop_info)

            self.add_widget(airdrop_info_layout)

        def on_airdrop_tap(self, instance):
            anim = Animation(size=((get_icons_sizes(Window.width, 'airdrop_button_sizes')) - 10, (get_icons_sizes(Window.width, 'airdrop_button_sizes')) - 10), duration=.05)
            anim.start(self.airdrop_button)

        def on_release_airdrop_tap(self, instance):
            anim = Animation(
                size=(get_icons_sizes(Window.width, 'airdrop_button_sizes'), get_icons_sizes(Window.width, 'airdrop_button_sizes')), duration=.05)
            anim.start(self.airdrop_button)

        def on_pre_enter(self):
            global airdrop_button_created
            button_creating_on_screen_checker = check_buttons_creating('airdrop', earn_button_created=None,
                                                                       boosts_button_created=None,
                                                                       frens_button_created=None,
                                                                       airdrop_button_created=airdrop_button_created,
                                                                       icons_button_created=None,
                                                                       settings_button_created=None)
            self.add_widget(NavigationBar(self.manager, button_creating_on_screen_checker))
            airdrop_button_created = 1

    class IconsScreen(Screen, RelativeLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.background_manager = BackgroundManager(self)

            self.info_all = (
                Label(
                    text=f'''FIC Icons''',
                    bold=True,
                    font_size=get_icons_sizes(Window.width, 'label_font'),
                    size_hint=(None, None), pos_hint={'center_x': .5, 'top': 1}, font_name=r'data/Fonts/CormorantSC-Bold.ttf'))
            self.add_widget(self.info_all)

            self.box_layout = BoxLayout(orientation='vertical', pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.8, .7))
            self.add_widget(self.box_layout)

            self.grid_layouts = [RelativeLayout(pos_hint={'center_x': .5}, size_hint=(1, .05)) for _ in range(5)]
            for i, grid in enumerate(self.grid_layouts):
                grid.pos_hint['center_y'] = 1 - i * 0.25  # Evenly space them vertically
                self.box_layout.add_widget(grid)

            def create_skin_button(skin_index, x_pos):
                icon_path = f'data/Icons/skin_{skin_index}.png'
                button_size = get_icons_sizes(Window.width, 'all_icons_button_size')
                return Button(
                    text='',
                    pos_hint={'center_x': x_pos},
                    size_hint=(None, None),
                    width=button_size,
                    height=button_size,
                    color='white',
                    bold=True,
                    background_normal=icon_path,
                    background_down=icon_path,
                    border=(0, 0, 0, 0),
                    on_release=lambda instance: self.add_value(skin_index)  # Pass the index directly
                )

            skin_data = [
                (1, 0), (2, 0.25), (3, 0.5), (4, 0.75), (5, 1),
                (6, 0), (7, 0.25), (8, 0.5), (9, 0.75), (10, 1),
                (11, 0), (12, 0.25), (13, 0.5), (14, 0.75), (15, 1),
            ]

            grid_index = 0
            for skin_index, x_pos in skin_data:
                button = create_skin_button(skin_index, x_pos)
                self.grid_layouts[grid_index].add_widget(button)
                if (skin_index) % 5 == 0 and skin_index != 1:
                    grid_index += 1

        def add_value(self, skin_index):
            global icon_value
            icon_value = skin_index

            self.manager.get_screen('more_icons').update_icon_value()
            self.manager.current = 'more_icons'
            self.manager.transition.direction = 'up'

        def on_pre_enter(self):
            global icons_button_created
            button_creating_on_screen_checker = check_buttons_creating('icons', earn_button_created=None,
                                                                       boosts_button_created=None,
                                                                       frens_button_created=None,
                                                                       airdrop_button_created=None,
                                                                       icons_button_created=icons_button_created,
                                                                       settings_button_created=None)
            self.add_widget(NavigationBar(self.manager, button_creating_on_screen_checker))
            icons_button_created = 1

    class MoreIconScreen(Screen, RelativeLayout):
        def __init__(self, **kwargs):
            global icon_value, value, icon_dict
            super().__init__(**kwargs)

            self.background_manager = BackgroundManager(self)

            import dict
            icon_dict = dict.icon_dict

            self.morelayout = BoxLayout(orientation='vertical', pos_hint={'center_x': .5, 'center_y': get_icons_sizes(Window.width, 'more_icon_screen_box_layout_pos_y')}, size_hint=(1, 1))
            self.add_widget(self.morelayout)

            self.icon_image = None
            self.info = None
            self.btn_buy = None
            self.btn_use = None
            self.info_payed = None
            self.info_price = None
            self.info_name = None

        def update_icon_value(self):
            global icon_value
            self.icon_value = icon_value
            self.update_widgets()

        def update_widgets(self):
            global tokens_needed, tokens, icon_db_value

            if hasattr(self, 'icon_image') and self.icon_image:
                self.morelayout.remove_widget(self.icon_image)
            if hasattr(self, 'info') and self.info:
                self.morelayout.remove_widget(self.info)
            if hasattr(self, 'btn_buy') and self.btn_buy:
                self.morelayout.remove_widget(self.btn_buy)
            if hasattr(self, 'btn_use') and self.btn_use:
                self.morelayout.remove_widget(self.btn_use)
            if hasattr(self, 'info_payed') and self.info_payed:
                self.morelayout.remove_widget(self.info_payed)
            if hasattr(self, 'info_price') and self.info_price:
                self.morelayout.remove_widget(self.info_price)
            if hasattr(self, 'info_name') and self.info_name:
                self.morelayout.remove_widget(self.info_name)

            icon_db_value = ((icon_dict[icon_value])[0])['icon_db_value']
            icon_name = ((icon_dict[icon_value])[0])['icon_name']
            icon_logo = ((icon_dict[icon_value])[0])['icon_logo']
            price = ((icon_dict[icon_value])[0])['price']
            tokens_needed = ((icon_dict[icon_value])[0])['tokens']

            cursor.execute('select {}, skin, tokens, vibration from Data where fic_id="{}"'.format(icon_db_value, str(suid)))
            so = cursor.fetchone()
            connection.commit()
            vibration_switch = int(so['vibration'])
            pay_value = int(so[icon_db_value])
            using_now_icon = int(so['skin'])
            tokens = int(so['tokens'])

            if using_now_icon == icon_value:
                using_value = 'Used'
            else:
                using_value = 'Use'

            if pay_value == 0:
                pay_value_text = 'Нет'
            else:
                pay_value_text = 'Да'

            self.icon_image = (
                Button(text='', size_hint=(None, None), width=get_icons_sizes(Window.width, 'more_icon_button_sizes'), height=get_icons_sizes(Window.width, 'more_icon_button_sizes'),
                       pos_hint={'center_x': .5}, color='white', bold=True,
                       background_normal=f'{icon_logo}', background_down=f'{icon_logo}', border=(0, 0, 0, 0)))

            self.info_name = (
                Label(text=f'''Название — {icon_name}''', bold=True, font_size=get_icons_sizes(Window.width, 'more_icon_font_size'), size_hint=(None, None),
                      pos_hint={'center_x': .5}, font_name=r'data/Fonts/CormorantSC-Bold.ttf'))

            if icon_value != 15:
                price_text = f'''Цена — {price}'''
            else:
                price_text = f'''{price}'''

            self.info_price = (
                Label(text=price_text, font_size=get_icons_sizes(Window.width, 'more_icon_font_size'), size_hint=(None, None),
                      pos_hint={'center_x': .5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'))
            self.info_payed = (
                Label(text=f'''Приобретено — {pay_value_text}''', font_size=get_icons_sizes(Window.width, 'more_icon_font_size'), size_hint=(None, None),
                      pos_hint={'center_x': .5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'))

            self.morelayout.add_widget(self.icon_image)
            self.morelayout.add_widget(self.info_name)
            self.morelayout.add_widget(self.info_price)
            self.morelayout.add_widget(self.info_payed)

            if pay_value_text == 'Да':
                self.btn_use = (
                    Button(text="",
                           size_hint=(None, None),
                           size=(get_icons_sizes(Window.width, 'horizontal_rectangle_buttons_width'), get_icons_sizes(Window.width, 'horizontal_rectangle_buttons_height')),
                           pos_hint={'center_x': .5, 'center_y': 0},
                           bold=True,
                           background_normal=f'data/ButtonMenu/{using_value}Icon.png',
                           background_down=f'data/ButtonMenu/{using_value}Icon.png'
                           ))
                self.morelayout.add_widget(self.btn_use)

                if using_value == 'Use':
                    self.btn_use.bind(on_release=self.Use_Icon)
                else:
                    pass

            elif pay_value_text == 'Нет':
                if icon_value != 15:
                    pay_button_value = 'Buy'
                else:
                    pay_button_value = 'Get'
                self.btn_buy = (
                    Button(text="",
                           size_hint=(None, None),
                           size=(get_icons_sizes(Window.width, 'horizontal_rectangle_buttons_width'), get_icons_sizes(Window.width, 'horizontal_rectangle_buttons_height')),
                           pos_hint={'center_x': .5, 'center_y': 0},
                           bold=True,
                           background_normal=f'data/ButtonMenu/{pay_button_value}Icon.png',
                           background_down=f'data/ButtonMenu/{pay_button_value}Icon.png'
                           ))
                self.morelayout.add_widget(self.btn_buy)

                if tokens >= tokens_needed:
                    self.btn_buy.bind(on_release=self.Successfull_Payment_Icon)
                else:
                    if vibration_switch == 1:
                        self.btn_buy.bind(on_press=self.vibration)
                    else:
                        pass

            self.btn_back = (
                Button(text="",
                       size_hint=(None, None),
                       size=(get_icons_sizes(Window.width, 'horizontal_rectangle_buttons_width'), get_icons_sizes(Window.width, 'horizontal_rectangle_buttons_height')),
                       pos_hint={'center_x': .5, 'center_y': .105},
                       bold=True,
                       background_normal='data/ButtonMenu/Back2Icons.png',
                       background_down='data/ButtonMenu/Back2Icons.png'
                       )
                )

            self.add_widget(self.btn_back)
            self.btn_back.bind(on_release=self.Back2Icons)

        def vibration(self, instance):
            random_choice = random.randint(0, 1)
            if random_choice == 0:
                try:
                    vibrator.vibrate(0.175)
                    vibrator.vibrate(0.175)
                except Exception as e:
                    passpass
            else:
                try:
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                except Exception as e:
                    pass

        def Back2Icons(self, instance):
            self.manager.current = 'icons'
            self.manager.transition.direction = 'down'

        def Successfull_Payment_Icon(self, instance):
            if icon_value != 15:
                cursor.execute('update Data set tokens={}, {}={}, skin={} where fic_id="{}"'.format((tokens - tokens_needed), icon_db_value, 1, icon_value, str(suid)))
                connection.commit()
                cursor.execute('select all_skins_counter from Data where fic_id="{}"'.format(str(suid)))
                ascr = cursor.fetchone()
                ascr = ascr['all_skins_counter']
                connection.commit()
                if ascr >= 29:
                    cursor.execute('update Data set all_skins_counter={} where fic_id="{}"'.format(ascr+1, str(suid)))
                    connection.commit()
                else:
                    # all have
                    pass
                self.manager.get_screen('main').update_tokens()
                self.manager.current = 'main'
            else:
                cursor.execute('select referral_link from Data where fic_id="{}"'.format(str(suid)))
                self.referral_link = cursor.fetchone()
                self.referral_link = self.referral_link['referral_link']
                self.referral_text = '%0AДавай%20зарабатывать%20вместе%20со%20мной%20в%20FIC!%0A%0AНажми%20ниже,%20чтобы%20присоединиться%20к%20веселью.%20🌟'
                webbrowser.open(f'https://t.me/share/url?url={self.referral_link}{self.referral_text}')

        def Use_Icon(self, instance):
            cursor.execute('update Data set skin={} where fic_id="{}"'.format(icon_value, str(suid)))
            self.manager.get_screen('main').update_tokens()
            self.manager.transition.direction = 'down'
            self.manager.current = 'main'

        def on_pre_enter(self):
            screen_n = self.manager.get_screen('more_icons')
            if hasattr(screen_n, 'background_manager'):
                self.background_manager.update_background()

    class SettingsScreen(Screen, RelativeLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.background_manager = BackgroundManager(self)

            self.info = (
                Label(
                    text=f'''FIC Settings''',
                    bold=True,
                    font_size=get_icons_sizes(Window.width, 'label_font'),
                    size_hint=(None, None), pos_hint={'center_x': .5, 'top': 1}, font_name=r'data/Fonts/CormorantSC-Bold.ttf'))
            self.add_widget(self.info)

            self.settings_box = BoxLayout(orientation='vertical', size_hint=(.7, .6),
                                          pos_hint={'center_x': .5, 'center_y': .55})
            self.settings_box.spacing = 150
            self.add_widget(self.settings_box)

            self.settings_layout_1 = RelativeLayout(size_hint=(1, .05), pos_hint={'center_x': .35})
            self.settings_layout_2 = RelativeLayout(size_hint=(1, .05), pos_hint={'center_x': .35})
            self.settings_layout_3 = RelativeLayout(size_hint=(1, .05), pos_hint={'center_x': .35})

            self.settings_box.add_widget(self.settings_layout_1)
            self.settings_box.add_widget(self.settings_layout_2)
            self.settings_box.add_widget(self.settings_layout_3)

            cursor.execute('select vibration, background from Data where fic_id="{}"'.format(str(suid)))
            sobg = cursor.fetchone()
            connection.commit()

            vibration_switch = int(sobg['vibration'])
            background_switch = int(sobg['background'])

            if vibration_switch == 0:
                self.sw_vib_value = 'On'
                self.vibration_text = 'Выключена'
            elif vibration_switch == 1:
                self.sw_vib_value = 'Off'
                self.vibration_text = 'Включена'

            if background_switch == 0:
                self.sw_bg_value = 'On'
                self.background_text = 'Выключен'
            elif background_switch == 1:
                self.sw_bg_value = 'Off'
                self.background_text = 'Включен'

            self.switch_vib_button = Button(text="",
                                       size_hint=(None, None),
                                       size=(get_icons_sizes(Window.width, 'boost_button_sizes'),
                                             get_icons_sizes(Window.width, 'boost_button_sizes')),
                                       pos_hint={'center_x': .3, 'center_y': .5},
                                       bold=True,
                                       background_normal=f'data/ButtonMenu/Vibration_{self.sw_vib_value}.png',
                                       background_down=f'data/ButtonMenu/Vibration_{self.sw_vib_value}.png'
                                       )
            self.switch_vib_button.bind(on_release=lambda instance: self.switch_func(switch_value='vibration'))

            self.info_switch_vib = (
                Label(
                    text=f'Кнопка включения и выключения\nВибрации\nЧтобы переключить,\nнужно нажать на нее.\n\nСейчас Вибрация {self.vibration_text}',
                    font_size=get_icons_sizes(Window.width, 'settings_label_font_size'),
                    size_hint=(None, None),
                    pos_hint={'center_x': 1, 'center_y': .5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
                )
            )

            self.switch_bg_button = Button(text="",
                       size_hint=(None, None),
                       size=(get_icons_sizes(Window.width, 'boost_button_sizes'),
                             get_icons_sizes(Window.width, 'boost_button_sizes')),
                       pos_hint={'center_x': .3, 'center_y': .5},
                       bold=True,
                       background_normal=f'data/ButtonMenu/Background_{self.sw_bg_value}.png',
                       background_down=f'data/ButtonMenu/Background_{self.sw_bg_value}.png'
                       )
            self.switch_bg_button.bind(on_release=lambda instance: self.switch_func(switch_value='background'))

            self.info_switch_bg = (
                Label(
                    text=f'Кнопка включения и выключения\nЗаднего фона\nЧтобы переключить,\nнужно нажать на нее.\n\nСейчас Задний фон {self.background_text}',
                    font_size=get_icons_sizes(Window.width, 'settings_label_font_size'),
                    size_hint=(None, None),
                    pos_hint={'center_x': 1, 'center_y': .5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
                )
            )

            self.logout_button = Button(text="",
                       size_hint=(None, None),
                       size=(get_icons_sizes(Window.width, 'boost_button_sizes'),
                             get_icons_sizes(Window.width, 'boost_button_sizes')),
                       pos_hint={'center_x': .3, 'center_y': .5},
                       bold=True,
                       background_normal=f'data/ButtonMenu/LogOut.png',
                       background_down=f'data/ButtonMenu/LogOut.png'
                       )
            self.logout_button.bind(on_release=self.accepting_exiting_func)

            self.info_logout = (
                Label(
                    text='Кнопка для выхода из\nсохраненного аккаунта.\nЧтобы выйти,\nнужно нажать на нее',
                    font_size=get_icons_sizes(Window.width, 'settings_label_font_size'),
                    size_hint=(None, None),
                    pos_hint={'center_x': 1, 'center_y': .5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
                )
            )

            self.settings_layout_1.add_widget(self.switch_vib_button)
            self.settings_layout_1.add_widget(self.info_switch_vib)
            self.settings_layout_2.add_widget(self.switch_bg_button)
            self.settings_layout_2.add_widget(self.info_switch_bg)
            self.settings_layout_3.add_widget(self.logout_button)
            self.settings_layout_3.add_widget(self.info_logout)

        def accepting_exiting_func(self, instance):
            global settings_button_created, airdrop_button_created, icons_button_created, frens_button_created, boosts_button_created, earn_button_created

            earn_button_created = 0
            boosts_button_created = 0
            frens_button_created = 0
            airdrop_button_created = 0
            icons_button_created = 0
            settings_button_created = 0

            self.manager.clear_widgets()

            cur.execute('drop table Data0')
            conn.commit()

            local_updating(request='creating', cur=cur, conn=conn, cursor=cursor, connection=connection)
            local_updating(request='update_null', cur=cur, conn=conn, cursor=cursor, connection=connection)
            cur.execute('update Data0 set do_import=1')
            conn.commit()

            screens = [('register', RegisterScreen()), ('auth', AuthScreen())]

            for name, screen in screens:
                screen.name = name
                sm.add_widget(screen)

            for screen in sm.children:
                screen.manager = sm

            return sm


            self.manager.current = 'register'

        def switch_func(self, switch_value):
            updated_button_type = None

            try:
                if switch_value == 'background':
                    button_image = 'data/ButtonMenu/Background_'
                    updated_button_type = self.switch_bg_button
                    self.updated_text = self.info_switch_bg
                elif switch_value == 'vibration':
                    button_image = 'data/ButtonMenu/Vibration_'
                    updated_button_type = self.switch_vib_button
                    self.updated_text = self.info_switch_vib

                cursor.execute('select {} from Data where fic_id="{}"'.format(switch_value, str(suid)))
                ts = cursor.fetchone()
                connection.commit()

                type_switch = ts[f'{switch_value}']

                if type_switch == 1:
                    cursor.execute('update Data set {}={} where fic_id="{}"'.format(switch_value, 0, str(suid)))
                    connection.commit()
                    updated_button_type.background_normal = f'{button_image}On.png'
                    updated_button_type.background_down  =  f'{button_image}On.png'
                    if switch_value == 'vibration':
                        self.updated_text.text = f'Кнопка включения и выключения\nВибрации\nЧтобы переключить,\nнужно нажать на нее.\n\nСейчас Вибрация Выключена'
                    elif switch_value == 'background':
                        self.updated_text.text = f'Кнопка включения и выключения\nЗаднего фона\nЧтобы переключить,\nнужно нажать на нее.\n\nСейчас Задний фон Выключен'


                elif type_switch == 0:
                    cursor.execute('update Data set {}={} where fic_id="{}"'.format(switch_value, 1, str(suid)))
                    connection.commit()
                    updated_button_type.background_normal = f'{button_image}Off.png'
                    updated_button_type.background_down = f'{button_image}Off.png'
                    if switch_value == 'vibration':
                        self.updated_text.text = f'Кнопка включения и выключения\nВибрации\nЧтобы переключить,\nнужно нажать на нее.\n\nСейчас Вибрация Включена'
                    elif switch_value == 'background':
                        self.updated_text.text = f'Кнопка включения и выключения\nЗаднего фона\nЧтобы переключить,\nнужно нажать на нее.\n\nСейчас Задний фон Включен'

                if switch_value == 'background':
                    self.background_manager.update_background()
                else:
                    pass
            except Exception as e:
                pass

        def on_pre_enter(self):
            global settings_button_created
            button_creating_on_screen_checker = check_buttons_creating('settings', earn_button_created=None,
                                                                       boosts_button_created=None,
                                                                       frens_button_created=None,
                                                                       airdrop_button_created=None,
                                                                       icons_button_created=None,
                                                                       settings_button_created=settings_button_created)
            self.add_widget(NavigationBar(self.manager, button_creating_on_screen_checker))
            settings_button_created = 1


    class PassiveFarmScreen(Screen, RelativeLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.info = Label(text=f'''FIC Passive Farm''', bold=True,
                              font_size=get_icons_sizes(Window.width, 'label_font'), size_hint=(None, None),
                              pos_hint={'center_x': .5, 'top': 1}, font_name=r'data/Fonts/CormorantSC-Bold.ttf')

        def update(self):
            self.fetch_pf_data()
            self.update_widgets_pf()

        def fetch_pf_data(self):
            import dict
            self.passive_farm_data = dict.passive_farm_setup_dict

            cursor.execute('select passive_farming, tokens, vibration from Data where fic_id="{}"'.format(str(suid)))
            from_data1 = cursor.fetchone()
            self.passive_farm = from_data1['passive_farming']
            self.vibration_switch = from_data1['vibration']
            self.tokens = from_data1['tokens']
            connection.commit()

            cursor.execute('select target_time, setup_time_until_getting, setup_tokens_getting from PassiveFarm where fic_id="{}"'.format(str(suid)))
            from_passive_farm = cursor.fetchone()
            self.setup1 = from_passive_farm['setup_time_until_getting']
            self.setup2 = from_passive_farm['setup_tokens_getting']
            connection.commit()

            self.time_until = (((((self.passive_farm_data['setup1'])['level'])[0])[self.setup1])[0])['time_until']
            self.many_tokens = (((((self.passive_farm_data['setup2'])['level'])[0])[self.setup1])[0])['many_tokens']

            if self.time_until == 4 or self.time_until == 24:
                self.time_until_hours_text = 'часа'
            elif self.time_until == 6 or self.time_until == 8 or self.time_until == 12:
                self.time_until_hours_text = 'часов'

            self.can_be_getted = int(self.many_tokens) * self.time_until
            self.total = self.tokens + int(self.many_tokens) * self.time_until

            self.target_time_db = from_passive_farm['target_time']


            self.explanation_label = Label(text="Что такое пассивный фарм?\n\nПассивный фарм — дополнительный способ\nфарма очков FIC\n\nЧтобы им управлять, его нужно купить.\n\nТакже у Пассивного фарма есть Прокачка!\n\nЦена для покупки Пассивного фарма — 200К очков-FIC",
                                               font_size=get_icons_sizes(Window.width, 'boost_label_font'),
                                               size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf')

            self.explanation_buttons_box = RelativeLayout(size_hint=(.9, .05), pos_hint={'center_x': .5}, pos=(0,50))

            self.explanation_buy_passive_farm_button = Button(
                text='',
                size_hint=(None, None),
                size=(get_icons_sizes(Window.width, 'passive_farm_explanation_buttons_width'), get_icons_sizes(Window.width, 'passive_farm_explanation_buttons_height')), # 220 70 and 380 100
                pos_hint={'left': .5},
                background_normal = 'data/ButtonMenu/BuyPassiveFarm.png',
                background_down = 'data/ButtonMenu/BuyPassiveFarm.png',
            )
            self.explanation_buy_passive_farm_button.bind(on_release=self.buy_passive_farm)

            self.explanation_back_button = Button(
                text='',
                size_hint=(None, None),
                size=(get_icons_sizes(Window.width, 'passive_farm_explanation_buttons_width'), get_icons_sizes(Window.width, 'passive_farm_explanation_buttons_height')),
                pos_hint={'right': 1},
                background_normal = 'data/ButtonMenu/GoBack.png',
                background_down = 'data/ButtonMenu/GoBack.png',
            )
            self.explanation_back_button.bind(on_release=self.go_back)

            self.setup_button = Button(text="", size=(get_icons_sizes(Window.width, 'button_menu'), get_icons_sizes(Window.width, 'button_menu')),
                                       size_hint=(None, None), pos_hint={'left': 1, 'bottom': 1},
                                       background_normal='data/ButtonMenu/SetUp.png',
                                       background_down='data/ButtonMenu/SetUp.png')
            self.setup_button.bind(on_release=self.go_setup)

            self.farm_button = Button(text="", size=(get_icons_sizes(Window.width, 'button_menu'), get_icons_sizes(Window.width, 'button_menu')),
                                      size_hint=(None, None),
                                      pos_hint={'center_x': .5, 'bottom': 1},
                                      background_normal='data/ButtonMenu/Farm.png',
                                      background_down='data/ButtonMenu/Farm.png')

            self.back_button = Button(text="", size=(get_icons_sizes(Window.width, 'button_menu'), get_icons_sizes(Window.width, 'button_menu')),
                                      size_hint=(None, None),
                                      pos_hint={'right': 1, 'bottom': 1},
                                      background_normal='data/ButtonMenu/GoToEarn.png',
                                      background_down='data/ButtonMenu/GoToEarn.png')
            self.back_button.bind(on_release=self.go_back)

            self.passive_farm_label = Label(text=f"Ты можешь запустить Пассивный Фарм!\n\nПФ будет идти {self.time_until} {self.time_until_hours_text},\nМожно будет собрать {self.can_be_getted} очков FIC\n\nБаланс будет: {self.total} FIC",
                                               font_size=get_icons_sizes(Window.width, 'label_frens_font'),
                                               size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf')

            self.start_pf_button = Button(
                text='',
                size_hint=(None, None),
                size=(get_icons_sizes(Window.width, 'horizontal_rectangle_buttons_width'), get_icons_sizes(Window.width, 'horizontal_rectangle_buttons_height')),
                pos_hint={'center_x': .5},
                background_normal='data/ButtonMenu/StartPassiveFarm.png',
                background_down='data/ButtonMenu/StartPassiveFarm.png',
            )

        def update_widgets_pf(self):
            self.clear_widgets()
            self.background_manager = BackgroundManager(self)
            self.add_widget(self.info)
            self.start_pf_button.unbind()

            if self.passive_farm == 0:
                self.add_widget(self.explanation_label)
                self.add_widget(self.explanation_buttons_box)
                self.explanation_buttons_box.add_widget(self.explanation_buy_passive_farm_button)
                self.explanation_buttons_box.add_widget(self.explanation_back_button)

            elif self.passive_farm == 1:
                self.buttons_pf_layout = RelativeLayout(size_hint=(1, .05), pos_hint={'center_x': .5, 'bottom': 1})
                self.add_widget(self.buttons_pf_layout)

                self.buttons_pf_layout.add_widget(self.setup_button)
                self.buttons_pf_layout.add_widget(self.farm_button)
                self.buttons_pf_layout.add_widget(self.back_button)
                try:
                    if self.target_time_db != '' or self.target_time_db != None:
                        target_datetime = datetime.strptime(self.target_time_db, "%Y.%m.%d %H:%M:%S")
                        now = datetime.now()
                        time_difference = target_datetime - now
                        if time_difference <= timedelta(0):
                            self.passive_farm_label.text = f'''Пассивный Фарм завершен!\n\nТы можешь собрать накопленные токены!'''
                            self.start_pf_button.background_normal = 'data/ButtonMenu/GetTokens.png'
                            self.start_pf_button.background_down = 'data/ButtonMenu/GetTokens.png'
                            self.start_pf_button.unbind()
                            self.start_pf_button.bind(on_release=lambda instance: self.claim_tokens(checker=0))

                        else:
                            self.passive_farm_label.text = f'''Сейчас работает Пассивный Фарм!\n\nТы сможешь собрать накопленные токены\n{datetime.strftime(target_datetime, '%d.%m.%Y в %H:%M')} или позже,\nНо лучше не забывать про сбор!'''
                            self.start_pf_button.background_normal = 'data/ButtonMenu/GetTokens.png'
                            self.start_pf_button.background_down = 'data/ButtonMenu/GetTokens.png'
                            self.start_pf_button.unbind()
                            self.start_pf_button.bind(on_release=lambda instance: self.claim_tokens(checker=1))

                    else:
                        self.start_pf_button.unbind()
                        self.start_pf_button.bind(on_release=self.start_farming)
                except:
                    self.start_pf_button.unbind()
                    self.start_pf_button.bind(on_release=self.start_farming)

                self.about_starting_layout = BoxLayout(orientation='vertical', size_hint=(1, None), size=(0, 300),pos_hint={'center_x': .5, 'center_y': get_icons_sizes(Window.width, 'about_starting_layout_center_y')})
                self.about_starting_layout.spacing = get_icons_sizes(Window.width, 'about_starting_layout_spacing')
                self.add_widget(self.about_starting_layout)

                self.about_starting_layout.add_widget(self.passive_farm_label)
                self.about_starting_layout.add_widget(self.start_pf_button)


        def start_farming(self, instance):
            def add_eight_hours(dt):
                return dt + timedelta(hours=self.time_until)

            now = datetime.now()
            future_time = add_eight_hours(now)
            result = future_time.strftime('%Y.%m.%d %H:%M:%S')

            self.passive_farm_label.text = f'''Пассивный Фарм запущен!\n\nТы сможешь собрать накопленные токены\n{future_time.strftime('%d.%m.%Y в %H:%M')} или позже,\nНо лучше не забывать про сбор!'''
            self.start_pf_button.background_normal = 'data/ButtonMenu/GetTokens.png'
            self.start_pf_button.background_down = 'data/ButtonMenu/GetTokens.png'
            self.start_pf_button.bind(on_release=lambda instance: self.claim_tokens(1))

            cursor.execute('update PassiveFarm set target_time="{}", many_tokens={} where fic_id="{}"'.format(result, int(self.can_be_getted), str(suid)))
            connection.commit()

            self.manager.transition.direction = 'left'
            self.manager.get_screen('main').update_tokens()
            self.manager.current = 'main'

        def claim_tokens(self, checker):
            def update_passive_farm():
                cursor.execute('select many_tokens from PassiveFarm where fic_id="{}"'.format(str(suid)))
                self.many_tokens_after = cursor.fetchone()
                self.many_tokens_after = self.many_tokens_after['many_tokens']
                connection.commit()
                cursor.execute('select tokens from Data where fic_id="{}"'.format(str(suid)))
                self.tokens_now = cursor.fetchone()
                self.tokens_now = self.tokens_now['tokens']
                connection.commit()
                cursor.execute(
                    'update Data set tokens={} where fic_id="{}"'.format((self.tokens_now + self.many_tokens_after),
                                                                         str(suid)))
                connection.commit()
                cursor.execute(
                    'update PassiveFarm set many_tokens=0, target_time="" where fic_id="{}"'.format(str(suid)))
                connection.commit()

            if checker == 1:
                cursor.execute('select target_time from PassiveFarm where fic_id="{}"'.format(str(suid)))
                target_date_time = cursor.fetchone()
                target_date_time = target_date_time['target_time']
                connection.commit()

                def check_reward_time(target):
                    now = datetime.now()
                    time_difference = target - now
                    if time_difference <= timedelta(0):
                        update_passive_farm()
                        self.manager.transition.direction = 'left'
                        self.manager.get_screen('main').update_tokens()
                        self.manager.current = 'main'
                        self.start_pf_button.unbind()
                    else:
                        random_choice = random.randint(0, 1)
                        if random_choice == 0:
                            try:
                                vibrator.vibrate(0.175)
                                vibrator.vibrate(0.175)
                            except Exception as e:
                                passpass
                        else:
                            try:
                                vibrator.vibrate(0.1)
                                vibrator.vibrate(0.1)
                                vibrator.vibrate(0.1)
                                vibrator.vibrate(0.1)
                                vibrator.vibrate(0.1)
                            except Exception as e:
                                pass

                target_datetime = datetime.strptime(target_date_time, "%Y.%m.%d %H:%M:%S")
                check_reward_time(target_datetime)

            elif checker == 0:
                self.start_pf_button.unbind()
                update_passive_farm()

                self.manager.transition.direction = 'left'
                self.manager.get_screen('main').update_tokens()
                self.manager.current = 'main'

        def buy_passive_farm(self, instance):
            if int(self.tokens) >= 200000:
                self.tokens_after = self.tokens - 200000
                cursor.execute('update Data set passive_farming=1, tokens={} where fic_id="{}"'.format(self.tokens_after, str(suid)))
                connection.commit()
                self.update()
            else:
                if self.vibration_switch == 1:
                    self.vibration()
                else:
                    pass

        def vibration(self):
            random_choice = random.randint(0, 1)
            if random_choice == 0:
                try:
                    vibrator.vibrate(0.175)
                    vibrator.vibrate(0.175)
                except Exception as e:
                    passpass
            else:
                try:
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                except Exception as e:
                    pass

        def go_back(self, instance):
            self.manager.transition.direction = 'left'
            self.manager.get_screen('main').update_tokens()
            self.manager.current = 'main'

        def go_setup(self, instance):
            self.manager.transition.direction = 'down'
            self.manager.get_screen('ps_setups').update()
            self.manager.current = 'ps_setups'

        def on_pre_enter(self):
            screen_n = self.manager.get_screen('passive_farm')
            if hasattr(screen_n, 'background_manager'):
                self.background_manager.update_background()

    class SetupScreen(Screen, RelativeLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.background_manager = BackgroundManager(self)

            self.info = Label(
                text=f'''FIC Setup''',
                bold=True,
                font_size=get_icons_sizes(Window.width, 'label_font'),
                size_hint=(None, None), pos_hint={'center_x': .5, 'top': 1}, font_name=r'data/Fonts/CormorantSC-Bold.ttf'
            )
            self.add_widget(self.info)

            self.buttons_pf_layout = RelativeLayout(size_hint=(1, .05), pos_hint={'center_x': .5, 'bottom': 1})
            self.add_widget(self.buttons_pf_layout)

            self.setup_button = Button(text="", size=(
            get_icons_sizes(Window.width, 'button_menu'), get_icons_sizes(Window.width, 'button_menu')),
                                       size_hint=(None, None), pos_hint={'center_x': .33, 'bottom': 1},
                                       background_normal='data/ButtonMenu/SetUp.png',
                                       background_down='data/ButtonMenu/SetUp.png')

            self.farm_button = Button(text="", size=(
            get_icons_sizes(Window.width, 'button_menu'), get_icons_sizes(Window.width, 'button_menu')),
                                      size_hint=(None, None), pos_hint={'center_x': .66, 'bottom': 1},
                                      background_normal='data/ButtonMenu/Farm.png',
                                      background_down='data/ButtonMenu/Farm.png')
            self.farm_button.bind(on_release=self.go_farm)

            self.buttons_pf_layout.add_widget(self.setup_button)
            self.buttons_pf_layout.add_widget(self.farm_button)

            import dict
            self.setup_dictionary = dict.passive_farm_setup_dict

            self.setups_layout_box = BoxLayout(orientation='vertical', size_hint=(1, .05), pos_hint={'center_x': .5, 'center_y': .5})
            self.setups_layout_box.spacing = get_icons_sizes(Window.width, 'boost_layout_spacing')
            self.add_widget(self.setups_layout_box)

            self.setup_layout_1 = RelativeLayout(size_hint=(1, .05), pos_hint={'center_x': .45, 'center_y': .7})
            self.setup_layout_2 = RelativeLayout(size_hint=(1, .05), pos_hint={'center_x': .45, 'center_y': .4})
            self.setups_layout_box.add_widget(self.setup_layout_1)
            self.setups_layout_box.add_widget(self.setup_layout_2)

            self.info_setup_1 = None
            self.info_setup_2 = None
            self.setup_1_button = None
            self.setup_2_button = None

        def update(self):
            self.fetch_setup_data()
            self.update_widgets_setup()

        def fetch_setup_data(self):
            global setup1, setup2
            cursor.execute('select tokens, vibration from Data where fic_id="{}"'.format(str(suid)))
            from_data = cursor.fetchone()
            connection.commit()
            cursor.execute('select setup_time_until_getting, setup_tokens_getting from PassiveFarm where fic_id="{}"'.format(str(suid)))
            from_pf = cursor.fetchone()
            connection.commit()

            self.tokens = int(from_data['tokens'])
            self.vibration_switch = int(from_data['vibration'])
            self.setup1 = int(from_pf['setup_time_until_getting'])
            self.setup2 = int(from_pf['setup_tokens_getting'])

            self.time_until = (((((self.setup_dictionary['setup1'])['level'])[0])[self.setup1])[0])['time_until']
            self.many_tokens = (((((self.setup_dictionary['setup2'])['level'])[0])[self.setup2])[0])['many_tokens']

            if self.time_until == 4 or self.time_until == 24:
                self.time_until_hours_text = 'часа'
            elif self.time_until == 6 or self.time_until == 8 or self.time_until == 12:
                self.time_until_hours_text = 'часов'

            self.description_setup1 = (self.setup_dictionary['setup1'])['description']
            if self.setup1 <= 4:
                self.price_setup1 = (((((self.setup_dictionary['setup1'])['level'])[0])[self.setup1])[0])['price_setup1']
                self.buy_setup1 = (((((self.setup_dictionary['setup1'])['level'])[0])[self.setup1])[0])['buy_setup1']
                self.info_setup_1_label_text = f'''{self.description_setup1}\n\nВремя твоего ПФ — {self.time_until} {self.time_until_hours_text}\nСледующий уровень — {self.price_setup1}'''
            else:
                self.info_setup_1_label_text = f'''{self.description_setup1}\n\nВремя твоего ПФ — {self.time_until} {self.time_until_hours_text}'''

            self.description_setup2 = (self.setup_dictionary['setup2'])['description']
            if self.setup2 <= 4:
                self.price_setup2 = (((((self.setup_dictionary['setup2'])['level'])[0])[self.setup2])[0])['price_setup2']
                self.buy_setup2 = (((((self.setup_dictionary['setup2'])['level'])[0])[self.setup2])[0])['buy_setup2']
                self.info_setup_2_label_text = f'''{self.description_setup2}\n\nТвое Возможное Количество\nТокенов за ПФ — {self.many_tokens}/час\nСледующий уровень — {self.price_setup2}'''
            else:
                self.info_setup_2_label_text = f'''{self.description_setup2}\n\nТвое Возможное Количество\nТокенов за ПФ — {self.many_tokens}/час'''

        def update_widgets_setup(self):
            self.setup_layout_1.clear_widgets()
            self.setup_layout_2.clear_widgets()

            self.info_setup_1 = Label(
                text=f'''{self.description_setup1}\n\nВремя твоего ПФ — {self.time_until} {self.time_until_hours_text}\nСледующий уровень — {self.price_setup1}''' if self.setup1 <= 4 else
                f'''{self.description_setup1}\n\nВремя твоего ПФ — {self.time_until} {self.time_until_hours_text}''',
                font_size=get_icons_sizes(Window.width, 'boost_label_font'),
                size_hint=(None, None),
                pos_hint={'center_x': .75, 'center_y': .5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
            )
            self.setup_1_button = Button(
                text="",
                size_hint=(None, None),
                size=(get_icons_sizes(Window.width, 'boost_button_sizes'), get_icons_sizes(Window.width, 'boost_button_sizes')),
                pos_hint={'center_x': .25, 'center_y': .5},
                bold=True,
                background_normal='data/ButtonMenu/Setup1.png',
                background_down='data/ButtonMenu/Setup1.png'
            )

            self.info_setup_2 = Label(text=f'''{self.description_setup2}\n\nВозможное Количество\nТокенов за ПФ — {self.many_tokens}/час\nСледующий уровень — {self.price_setup2}''' if self.setup2 <= 4 else
                f'''{self.description_setup2}\n\nВозможное Количество\nТокенов за ПФ — {self.many_tokens}/час''',
                font_size=get_icons_sizes(Window.width, 'boost_label_font'),
                size_hint=(None, None),
                pos_hint={'center_x': .75, 'center_y': .5}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
            )
            self.setup_2_button = Button(
                text="",
                size_hint=(None, None),
                size=(get_icons_sizes(Window.width, 'boost_button_sizes'), get_icons_sizes(Window.width, 'boost_button_sizes')),
                pos_hint={'center_x': .25, 'center_y': .5},
                bold=True,
                background_normal='data/ButtonMenu/Setup2.png',
                background_down='data/ButtonMenu/Setup2.png'
            )

            if self.setup1 <= 4:
                if self.tokens >= self.buy_setup1:
                    self.setup_1_button.bind(on_release=lambda instance: self.Successfull_Payment_Setup(1))
                else:
                    if self.vibration_switch == 1:
                        self.setup_1_button.bind(on_press=self.vibration)
            else:
                pass

            if self.setup2 <= 4:
                if self.tokens >= self.buy_setup2:
                    self.setup_2_button.bind(on_release=lambda instance: self.Successfull_Payment_Setup(2))
                else:
                    if self.vibration_switch == 1:
                        self.setup_2_button.bind(on_press=self.vibration)
            else:
                pass

            self.setup_layout_1.add_widget(self.setup_1_button)
            self.setup_layout_1.add_widget(self.info_setup_1)
            self.setup_layout_2.add_widget(self.setup_2_button)
            self.setup_layout_2.add_widget(self.info_setup_2)

        def Successfull_Payment_Setup(self, setup_value):
            if setup_value == 1:
                update_data_col = 'setup_time_until_getting'
                update_data_col_val = self.setup1 + 1
                price = self.tokens - self.buy_setup1
                cursor.execute(
                    'update PassiveFarm set {}={} where fic_id="{}"'.format(
                        update_data_col, update_data_col_val, str(suid)))
                connection.commit()
                cursor.execute(
                    'update Data set tokens={} where fic_id="{}"'.format(price, str(suid)))
                connection.commit()
                cur.execute('update Data1 set tokens={}'.format(price))
                conn.commit()

                self.setup1 = update_data_col_val
                self.tokens = price
                setup1 = self.setup1

            elif setup_value == 2:
                update_data_col = 'setup_tokens_getting'
                update_data_col_val = self.setup2 + 1
                price = self.tokens - self.buy_setup2

                cursor.execute(
                    'update PassiveFarm set {}={} where fic_id="{}"'.format(
                        update_data_col, update_data_col_val, str(suid)))
                connection.commit()
                cursor.execute(
                    'update Data set tokens={} where fic_id="{}"'.format(price, str(suid)))
                connection.commit()
                cur.execute('update Data1 set tokens={}'.format(price))
                conn.commit()

                self.setup2 = update_data_col_val
                self.tokens = price
                setup2 = self.setup2

            self.manager.transition.direction = 'up'
            self.manager.get_screen('passive_farm').update()
            self.manager.current = 'passive_farm'

        def go_farm(self, instance):
            self.manager.transition.direction = 'up'
            self.manager.get_screen('passive_farm').update()
            self.manager.current = 'passive_farm'

        def vibration(self):
            random_choice = random.randint(0, 1)
            if random_choice == 0:
                try:
                    vibrator.vibrate(0.175)
                    vibrator.vibrate(0.175)
                except Exception as e:
                    passpass
            else:
                try:
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                    vibrator.vibrate(0.1)
                except Exception as e:
                    pass


    class FigmentInterplanetaryCoinApp(App):
        def build(self):
            self.icon = 'data/Application/icon.png'

            cur.execute('select auto_auth from Data0')
            sx = cur.fetchone()
            conn.commit()

            data0_string = sx[0]
            data0 = int(data0_string)

            screens = []

            if data0 == 0:
                screens = [('register', RegisterScreen()),('auth', AuthScreen())]

            elif data0 == 1:
                cursor.execute('select access from Data where fic_id="{}"'.format(str(suid)))
                acs = cursor.fetchone()
                acs = acs['access']
                connection.commit()

                if acs == 1:
                    screens = [('main', FigmentInterplanetaryCoin()), ('boosts', BoostsScreen()),('frens', FrensScreen()),('airdrop', AirDropScreen()),('icons', IconsScreen()),('more_icons', MoreIconScreen()),('settings', SettingsScreen()), ('passive_farm', PassiveFarmScreen()), ('ps_setups', SetupScreen()), ('blocked', BlockedAccessScreen()), ('works', BlockedWorksScreen(acs))]
                elif acs == 0:
                    screens = [('blocked', BlockedAccessScreen())]
                elif acs == 2 or acs == 3:
                    screens = [('works', BlockedWorksScreen(acs))]

            for name, screen in screens:
                screen.name = name
                sm.add_widget(screen)

            for screen in sm.children:
                screen.manager = sm

            return sm

    if __name__ == '__main__':
        FigmentInterplanetaryCoinApp().run()


elif x is False:
    class ConnectionFailed(Screen, RelativeLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.label_blocked_name = (
                Label(
                    text='FIC App',
                    size_hint=(None, None),
                    bold=True,
                    font_size=get_icons_sizes(Window.width, 'label_font'),
                    pos_hint={'center_x': .5, 'top': 1}, font_name=r'data/Fonts/CormorantSC-Bold.ttf'
                )
            )
            self.add_widget(self.label_blocked_name)

            self.coin_button = Button(text="",
                                      size_hint=(None, None),
                                      size=(
                                      get_icons_sizes(Window.width, 'coin'), get_icons_sizes(Window.width, 'coin')),
                                      pos_hint={'center_x': .5, 'center_y': .5},
                                      bold=True,
                                      background_normal='data/Icons/blocked.png',
                                      background_down='data/Icons/blocked.png',
                                      )
            self.coin_button.bind(on_press=self.on_coin_click, on_release=self.on_coin_release)
            self.add_widget(self.coin_button)

            self.label_blocked = (
                Label(
                    text=f'Проверьте свое подключение\nк Интернету!',
                    size_hint=(None, None),
                    bold=False,
                    font_size=get_icons_sizes(Window.width, 'label_font'),
                    pos_hint={'center_x': .5, 'center_y': .1}, font_name=r'data/Fonts/CormorantSC-Medium.ttf'
                )
            )
            self.add_widget(self.label_blocked)

        def on_coin_click(self, instance):
            anim = (Animation(size=((get_icons_sizes(Window.width, 'coin')) - 20, (get_icons_sizes(Window.width, 'coin')) - 20),duration=.05))
            anim.start(self.coin_button)

        def on_coin_release(self, instance):
            anim = Animation(size=((get_icons_sizes(Window.width, 'coin')), (get_icons_sizes(Window.width, 'coin'))),duration=.05)
            anim.start(self.coin_button)


    class FigmentInterplanetaryCoinApp(App):
        def build(self):
            Window.borderless = True
            self.icon = 'data/Application/icon.png'

            sm = ScreenManager()
            screens = []

            screens = [('connection_failed', ConnectionFailed())]

            for name, screen in screens:
                screen.name = name
                sm.add_widget(screen)

            return sm

    if __name__ == '__main__':
        FigmentInterplanetaryCoinApp().run()