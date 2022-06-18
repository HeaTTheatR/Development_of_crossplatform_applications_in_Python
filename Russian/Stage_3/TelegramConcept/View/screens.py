# Словарь экранов - содержит объекты моделей и контроллеров экранов приложения.

from Model.login_screen import LoginScreenModel

from Controller.login_screen import LoginScreenController

screens = {
    # Имя экрана.
    "login screen": {
        "model": LoginScreenModel,  # модель экрана
        "controller": LoginScreenController,  # контроллер экрана
    },
}

