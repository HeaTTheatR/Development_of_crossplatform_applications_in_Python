from View.LoginScreen.login_screen import LoginScreenView


class LoginScreenController:
    """
    Обрабатывает пользовательский ввод и события, оповещая модель о
    необходимости изменений. Контролирует и направляет данные от пользователя
    к модели. При необходимости вызывает методы представления.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel object
        self.view = LoginScreenView(
            controller=self, model=self.model
        )

    def get_view(self) -> LoginScreenView:
        return self.view
