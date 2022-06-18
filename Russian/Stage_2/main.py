from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty

from kivymd.app import MDApp

from View.screens import screens
from libs.translation import Translation
from Model.database import DataBase


class TelegramConcept(MDApp):
    lang = StringProperty("ru")  # значение языковой локализации

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Класс реализующий смену языковой локализации приложения.
        self.translation = Translation(
            self.lang, "TelegramConcept", f"{self.directory}/data/locales"
        )
        # Рекурсивно загружает KV файлы из выбранного каталога.
        self.load_all_kv_files(self.directory)
        # Это менеджер экранов, который будет содержать все экраны вашего
        # приложения.
        self.manager_screens = ScreenManager()
        # Класс, реализующий методы работы с базой данных Firebase.
        self.database = DataBase()

    def build(self) -> ScreenManager:
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self) -> None:
        """
        Создание и добавление экранов в менеджер экранов.
        Вы не должны изменять этот цикл без необходимости. Он самодостаточен.

        Если вам нужно добавить какой-либо экран, откройте модуль
        `View.screens.py` и посмотрите, как добавляются новые экраны
        в соответствии с заданной архитектурой приложения.
        """

        for name_screen in screens.keys():
            model = screens[name_screen]["model"](self.database)
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

    def on_lang(self, instance_app, lang_value: str) -> None:
        """
        Вызывается при изменении значения языковой локализации :attr:`~lang`.
        """

        self.translation.switch_lang(lang_value)

    def switch_lang(self) -> None:
        """Переключает языковую локализацию приложения."""

        self.lang = "ru" if self.lang == "en" else "en"


TelegramConcept().run()
