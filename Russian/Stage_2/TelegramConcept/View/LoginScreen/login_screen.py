from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.textfield import MDTextField

from View.base_screen import BaseScreenView


class LoginScreenView(BaseScreenView):
    """Реализует экран регистрации пользователя в приложении."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Red"

        box = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            size_hint_x=0.5,
            size_hint_min_x="240dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=24,
            spacing="12dp",
            padding="24dp",
            md_bg_color=self.theme_cls.bg_darkest,
        )
        box_buttons = MDBoxLayout(
            adaptive_size=True,
            spacing="12dp",
            padding=(0, "24dp", 0, 0),
            pos_hint={"center_x": 0.5},
        )

        logo = FitImage(
            source="avatar.png",  # укажите путь к изображению на вашем компьютере
            size_hint=(None, None),
            size=("120dp", "120dp"),
            pos_hint={"center_x": 0.5},
        )
        login_field = MDTextField(
            mode="rectangle",
            hint_text="Login",
            size_hint_x=0.8,
            pos_hint={"center_x": 0.5},
        )
        password_field = MDTextField(
            mode="rectangle",
            hint_text="Password",
            size_hint_x=0.8,
            pos_hint={"center_x": 0.5},
        )
        button_login = MDRaisedButton(text="LOGIN")
        button_cancel = MDRaisedButton(text="CANCEL")

        box_buttons.add_widget(button_login)
        box_buttons.add_widget(button_cancel)

        box.add_widget(logo)
        box.add_widget(login_field)
        box.add_widget(password_field)
        box.add_widget(box_buttons)

        self.add_widget(box)
