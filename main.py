import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager


kivy.require('2.0.0')


class ContainerOne(Screen):
    pass


class ContainerTwo(Screen):
    def number_of_sheets_m2(self):
        if all((self.text_input_width.text, self.text_input_m2.text)):
            try:
                g = str(0.64 * float(self.text_input_width.text))
                self.label_result_m2.text = f'В роле примерно ' \
                                            f'{round(float(self.text_input_m2.text) / float(g))} ' \
                                            f'листа(ов)'
            except AttributeError:
                self.label_result_m2.text = 'Ошибка'
        else:
            self.label_result_m2.text = 'Заполните все поля'

    def clear1(self):
        self.text_input_width.text, self.text_input_m2.text = '', ''
        self.label_result_m2.text = ''

    def number_of_sheets_pm(self):
        if self.text_input_pm.text:
            try:
                self.label_result_pm.text = f'В роле примерно ' \
                                            f'{round(float(self.text_input_pm.text) / 0.63)} ' \
                                            f'листа(ов)'
            except AttributeError:
                self.label_result_pm.text = 'Ошибка'
        else:
            self.label_result_pm.text = 'Заполните все поля'

    def clear2(self):
        self.text_input_pm.text = ''
        self.label_result_pm.text = ''


class ContainerThree(Screen):
    def on_solution(self):
        if all((self.solution1.text, self.solution2.text, self.solution3.text)):
            try:
                # t, y and z я не зная что это за переменные в формуле
                t = str((float(self.solution1.text) - float(self.solution3.text)) / float(2))
                y = str((float(4) * float(t) * (float(self.solution1.text) - float(t)) /
                         (float(self.solution1.text) * float(self.solution1.text) - 0.1 * 0.1) *
                         float(self.solution2.text)))
                z = str(float(self.solution2.text) - float(y))
                self.print_result.text = f'Остаток {round(float(z), 2)} кг'
            except AttributeError:
                self.print_result.text = 'Ошибка'
        else:
            self.print_result.text = 'заполните все поля'

    def on_button_press(self):
        self.solution1.text, self.solution2.text, self.solution3.text = '', '', ''
        self.print_result.text = ''


class WindowManager(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        self.title = 'Бумажный калькулятор'


if __name__ == '__main__':
    MainApp().run()
