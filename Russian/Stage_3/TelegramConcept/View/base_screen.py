from kivy.properties import ObjectProperty

from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen

from Utility.observer import Observer


class BaseScreenView(ThemableBehavior, Observer, MDScreen):
    """Реализует базовый класс представления для всех экранов приложения."""

    # Controller представления - Controller.module_screen.ClassScreenController
    controller = ObjectProperty()
    # Model представления - Model.module_screen.ClassScreenModel
    model = ObjectProperty()
    # Менеджер экранов приложения - kivy.uix.screenmanager.ScreenManager
    manager_screens = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.model:
            self.model.add_observer(self)
