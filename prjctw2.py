from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, Line
from kivy.metrics import dp


# =========================
# COLORS
# =========================

CREAM = (0.96, 0.95, 0.91, 1)
WHITE = (1, 1, 1, 1)
ORANGE = (0.68, 0.30, 0.15, 1)
DARK = (0.20, 0.20, 0.18, 1)
GRAY = (0.55, 0.54, 0.51, 1)
BORDER = (0.55, 0.55, 0.53, 1)


# =========================
# LOGIN BOX
# =========================

class LoginBox(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = dp(10)
        self.spacing = dp(6)

        # -------------------------
        # WHITE LOGIN BOX
        # -------------------------

        with self.canvas.before:
            Color(*WHITE)

            self.bg = Rectangle(
                pos=self.pos,
                size=self.size
            )

            Color(*BORDER)

            self.border = Line(
                rectangle=(
                    self.x,
                    self.y,
                    self.width,
                    self.height
                ),
                width=1
            )

        self.bind(
            pos=self.update_graphics,
            size=self.update_graphics
        )

        # -------------------------
        # USERNAME LABEL
        # -------------------------

        self.add_widget(Label(
            text="Username",
            font_size=dp(12),
            bold=True,
            color=DARK,
            halign="left",
            valign="middle",
            text_size=(dp(270), dp(25)),
            size_hint_y=None,
            height=dp(25)
        ))

        # -------------------------
        # USERNAME INPUT
        # -------------------------

        self.username = TextInput(
            text="",
            hint_text="Enter username",
            multiline=False,
            font_size=dp(13),
            foreground_color=DARK,
            background_color=WHITE,
            cursor_color=ORANGE,
            padding=[dp(4), dp(4)],
            size_hint_y=None,
            height=dp(30)
        )

        self.add_widget(self.username)

        # -------------------------
        # PASSWORD LABEL
        # -------------------------

        self.add_widget(Label(
            text="Password",
            font_size=dp(12),
            bold=True,
            color=DARK,
            halign="left",
            valign="middle",
            text_size=(dp(270), dp(25)),
            size_hint_y=None,
            height=dp(25)
        ))

        # -------------------------
        # PASSWORD ROW
        # -------------------------

        password_row = BoxLayout(
            orientation="horizontal",
            spacing=dp(4),
            size_hint_y=None,
            height=dp(30)
        )

        # PASSWORD INPUT

        self.password = TextInput(
            text="",
            hint_text="Enter password",
            password=True,
            multiline=False,
            font_size=dp(13),
            foreground_color=DARK,
            background_color=WHITE,
            cursor_color=ORANGE,
            padding=[dp(4), dp(4)]
        )

        password_row.add_widget(self.password)

        # SHOW / HIDE BUTTON

        self.show_button = Button(
            text="Show",
            font_size=dp(10),
            color=DARK,
            background_normal="",
            background_color=(0.88, 0.87, 0.83, 1),
            size_hint_x=None,
            width=dp(50)
        )

        self.show_button.bind(
            on_press=self.toggle_password
        )

        password_row.add_widget(self.show_button)

        self.add_widget(password_row)

        # -------------------------
        # LOGIN BUTTON
        # -------------------------

        login_button = Button(
            text="Log In",
            font_size=dp(12),
            bold=True,
            color=WHITE,
            background_normal="",
            background_color=ORANGE,
            size_hint=(None, None),
            size=(dp(70), dp(38)),
            pos_hint={"center_x": 0.5}
        )

        login_button.bind(
            on_press=self.login
        )

        self.add_widget(login_button)

        # -------------------------
        # LOGIN MESSAGE
        # -------------------------

        self.login_message = Label(
            text="",
            font_size=dp(10),
            color=GRAY,
            size_hint_y=None,
            height=dp(25)
        )

        self.add_widget(self.login_message)

    # =========================
    # SHOW / HIDE PASSWORD
    # =========================

    def toggle_password(self, instance):

        if self.password.password:
            self.password.password = False
            self.show_button.text = "Hide"

        else:
            self.password.password = True
            self.show_button.text = "Show"

    # =========================
    # LOGIN
    # =========================

    def login(self, instance):

        username = self.username.text
        password = self.password.text

        # DEMO LOGIN
        correct_username = "admin"
        correct_password = "1234"

        if username == correct_username and password == correct_password:

            self.login_message.text = "Login successful!"
            self.login_message.color = (0.2, 0.6, 0.2, 1)

            print("Login successful!")

        else:

            self.login_message.text = "Invalid username or password!"
            self.login_message.color = (0.8, 0.2, 0.2, 1)

            print("Invalid username or password!")

    # =========================
    # UPDATE BOX GRAPHICS
    # =========================

    def update_graphics(self, *args):

        self.bg.pos = self.pos
        self.bg.size = self.size

        self.border.rectangle = (
            self.x,
            self.y,
            self.width,
            self.height
        )


# =========================
# MAIN SCREEN
# =========================

class MainScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        # -------------------------
        # CREAM BACKGROUND
        # -------------------------

        with self.canvas.before:

            Color(*CREAM)

            self.background = Rectangle(
                pos=self.pos,
                size=self.size
            )

        self.bind(
            pos=self.update_background,
            size=self.update_background
        )

        # -------------------------
        # TOP SPACE
        # -------------------------

        self.add_widget(Label(
            text="",
            size_hint_y=0.20
        ))

        # -------------------------
        # TITLE
        # -------------------------

        self.add_widget(Label(
            text="Seller Login",
            font_size=dp(24),
            bold=True,
            color=ORANGE,
            size_hint_y=None,
            height=dp(42)
        ))

        # -------------------------
        # SUBTITLE
        # -------------------------

        self.add_widget(Label(
            text="Enter your credentials to continue",
            font_size=dp(10),
            color=GRAY,
            size_hint_y=None,
            height=dp(25)
        ))

        # -------------------------
        # LOGIN BOX
        # -------------------------

        holder = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(dp(300), dp(250)),
            pos_hint={"center_x": 0.5}
        )

        holder.add_widget(LoginBox())

        self.add_widget(holder)

        # -------------------------
        # BACK
        # -------------------------

        self.add_widget(Label(
            text="← Back",
            font_size=dp(10),
            color=GRAY,
            size_hint_y=None,
            height=dp(35)
        ))

        # -------------------------
        # BOTTOM SPACE
        # -------------------------

        self.add_widget(Label(
            text="",
            size_hint_y=0.5
        ))

    def update_background(self, *args):

        self.background.pos = self.pos
        self.background.size = self.size


# =========================
# APP
# =========================

class SellerLoginApp(App):

    def build(self):

        self.title = "MadaList"

        return MainScreen()


SellerLoginApp().run()