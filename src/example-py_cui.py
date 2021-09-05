from py_cui import PyCUI, colors, keys

HEIGHT = 12
WIDTH = 11
COLOR_STATUSBAR = colors.WHITE_ON_BLACK
TITLE = 'Manager Wallets'
BAR = ''

class ManagerWallet(object):

    def __init__(self, root: PyCUI):
        self.root = root
        self.window_names = [
            'account',
            'wallet',
            'expense',
            'incoming',
        ]
        self.window = {
            name: self.root.create_new_widget_set(HEIGHT, WIDTH)
            for name in self.window_names
        }
        self.add_main_menu()
        self.create_account_window()
        self.root.apply_widget_set(self.window['account'])

    def create_account_window(self):
        window = self.window['account']
        window.add_text_box('firstname', row=0, column=1, column_span=2)
        window.add_text_box('lastname', row=0, column=3, column_span=2)
        window.add_button('add', row=2, column=1, row_span=1, column_span=4)

    def add_main_menu(self):
        for name, window in self.window.items():
            menu = window.add_scroll_menu('menu', 0, 0, row_span=8, padx=0)
            menu.add_item_list(self.window_names)
            menu.add_key_command(keys.KEY_ENTER, self.open_window)
            menu.set_selected_color(colors.RED_ON_BLACK)
            menu.add_text_color_rule('>', colors.GREEN_ON_BLACK, 'startswith')

    def open_window(self):
        widget = self.root.get_selected_widget()
        item = widget.get()
        index = widget.get_selected_item_index()
        window = self.window[item]
        self.root.set_title(f'{TITLE} - {item}')
        self.root.apply_widget_set(window)
        widget = window.get_widgets()['Widget0']
        self.root.move_focus(widget)
        widget.set_selected_item_index(index)

    def focus_in_menu(self):
        self.root.move_focus(self.menu)

root = PyCUI(HEIGHT, WIDTH)
# root.toggle_unicode_borders()
root.set_title(TITLE)
root.set_status_bar_text(BAR)
root.title_bar.set_color(COLOR_STATUSBAR)
root.status_bar.set_color(COLOR_STATUSBAR)
simple = ManagerWallet(root)
root.start()

