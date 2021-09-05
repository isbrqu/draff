import npyscreen

class myEmployeeForm(npyscreen.Form):

    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        y, x = self.useable_space()
        self.box = self.add(
            npyscreen.BoxTitle,
            name='bruh',
            relx=1,
            rely=1,
            max_width=x//10,
            max_height=-30
        )
        self.box.values = [
            'accounts',
            'wallets',
            'transactions',
            'categories',
            'users',
        ]
        self.myName = self.add(
            npyscreen.TitleText,
            name='Name'
        )
        self.types = self.add(
            npyscreen.TitleSelectOne,
            scroll_exit=True,
            max_height=3,
            name='types',
            values=['alimento', 'transporte', '']
        )
        self.myDate = self.add(
            npyscreen.TitleDateCombo,
            name='date'
        )

class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.TransparentThemeLightText)
        self.addForm('MAIN', myEmployeeForm, name='New Employee')
        # A real application might define more forms here.......

if __name__ == '__main__':
    app = MyApplication()
    app.run()


