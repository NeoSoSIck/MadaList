from kivy.app import App
from kivy.metrics import dp, sp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle, Line
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


# =========================================================
# COLORS
# =========================================================

CREAM = (0.96, 0.95, 0.91, 1)
WHITE = (1, 1, 1, 1)
ORANGE = (0.68, 0.30, 0.15, 1)
DARK = (0.20, 0.20, 0.18, 1)
GRAY = (0.55, 0.54, 0.51, 1)
BORDER = (0.55, 0.55, 0.53, 1)


# =========================================================
# FIRST SCREEN / LANDING PAGE
# =========================================================

class LandingScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.clearcolor = (0.965, 0.955, 0.925, 1)

        root = FloatLayout()

        # -------------------------
        # TITLE
        # -------------------------

        title = Label(
            text="MadaList",
            font_size=sp(35),
            bold=True,
            color=(0.67, 0.25, 0.14, 1),
            size_hint=(0.90, None),
            height=dp(55),
            pos_hint={"center_x": 0.5, "top": 0.88},
        )
        root.add_widget(title)

        # -------------------------
        # SUBTITLE
        # -------------------------

        subtitle = Label(
            text="Sari-Sari Store Sales & Inventory Tracker",
            font_size=sp(13),
            color=(0.56, 0.55, 0.53, 1),
            size_hint=(0.92, None),
            height=dp(35),
            pos_hint={"center_x": 0.5, "top": 0.825},
            halign="center",
            valign="middle",
        )

        subtitle.bind(
            size=lambda obj, value: setattr(obj, "text_size", value)
        )

        root.add_widget(subtitle)

        # -------------------------
        # CONTINUE AS
        # -------------------------

        continue_label = Label(
            text="Continue as",
            font_size=sp(21),
            bold=True,
            color=(0.12, 0.12, 0.12, 1),
            size_hint=(0.90, None),
            height=dp(45),
            pos_hint={"center_x": 0.5, "top": 0.69},
        )
        root.add_widget(continue_label)

        # -------------------------
        # SELLER BUTTON
        # -------------------------

        seller = Button(
            text="Seller",
            font_size=sp(15),
            bold=True,
            color=(1, 1, 1, 1),
            background_normal="",
            background_down="",
            background_color=(0.72, 0.25, 0.13, 1),
            size_hint=(0.43, None),
            height=dp(59),
            pos_hint={"x": 0.05, "top": 0.60},
        )

        seller.bind(on_release=self.seller_clicked)
        root.add_widget(seller)

        # -------------------------
        # CUSTOMER BUTTON
        # -------------------------

        customer = Button(
            text="Customer",
            font_size=sp(15),
            bold=True,
            color=(1, 1, 1, 1),
            background_normal="",
            background_down="",
            background_color=(0.72, 0.25, 0.13, 1),
            size_hint=(0.43, None),
            height=dp(59),
            pos_hint={"x": 0.52, "top": 0.60},
        )

        customer.bind(on_release=self.customer_clicked)
        root.add_widget(customer)

        # -------------------------
        # TOC BUTTON
        # -------------------------

        terms = Button(
            text="Terms and Conditions",
            font_size=sp(11.5),
            color=(0.51, 0.50, 0.48, 1),
            background_normal="",
            background_color=(0, 0, 0, 0),
            size_hint=(0.43, None),
            height=dp(32),
            pos_hint={"x": 0.07, "y": 0.025},
        )

        terms.bind(on_release=self.terms_clicked)
        root.add_widget(terms)
        
        
        
        # SEPARATOR " | " #

        separator = Label(
            text="|",
            font_size=sp(11),
            color=(0.75, 0.74, 0.72, 1),
            size_hint=(None, None),
            size=(dp(16), dp(32)),
            pos_hint={"center_x": 0.50, "y": 0.025},
        )
        root.add_widget(separator)
        
        
        
        
        # HOW IT WORK BUTTON #
        
        how = Button(
            text="How it Work",
            font_size=sp(11.5),
            color=(0.51, 0.50, 0.48, 1),
            background_normal="",
            background_color=(0, 0, 0, 0),
            size_hint=(0.43, None),
            height=dp(32),
            pos_hint={"x": 0.55, "y": 0.025},
        )

        how.bind(on_release=self.how_clicked)
        root.add_widget(how)
        
        self.add_widget(root)
        

    # -------------------------
    # BUTTON FUNCTIONS
    # -------------------------

    def seller_clicked(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "seller_login"
   
    def customer_clicked(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "customer_login"

    

    def terms_clicked(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "terms_screen"
        
    def how_clicked(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "how_screen"    
           


# =========================================================
# LOGIN BOX
# =========================================================

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

        # -------------------------
        # SHOW / HIDE BUTTON
        # -------------------------

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

    # -------------------------
    # SHOW / HIDE PASSWORD
    # -------------------------

    def toggle_password(self, instance):

        if self.password.password:
            self.password.password = False
            self.show_button.text = "Hide"

        else:
            self.password.password = True
            self.show_button.text = "Show"

    # -------------------------
    # LOGIN
    # -------------------------

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

    # -------------------------
    # UPDATE BOX GRAPHICS
    # -------------------------

    def update_graphics(self, *args):

        self.bg.pos = self.pos
        self.bg.size = self.size

        self.border.rectangle = (
            self.x,
            self.y,
            self.width,
            self.height
        )


# =========================================================
# SELLER LOGIN SCREEN
# =========================================================

class SellerLoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical"
        )

        # -------------------------
        # CREAM BACKGROUND
        # -------------------------

        with root.canvas.before:

            Color(*CREAM)

            self.background = Rectangle(
                pos=root.pos,
                size=root.size
            )

        root.bind(
            pos=self.update_background,
            size=self.update_background
        )

        # -------------------------
        # TOP SPACE
        # -------------------------

        root.add_widget(Label(
            text="",
            size_hint_y=0.20
        ))

        # -------------------------
        # TITLE
        # -------------------------

        root.add_widget(Label(
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

        root.add_widget(Label(
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

        root.add_widget(holder)

        # -------------------------
        # BACK BUTTON
        # -------------------------

        back_button = Button(
            text="Back",
            font_size=dp(10),
            color=GRAY,
            background_normal="",
            background_color=(0, 0, 0, 0),
            size_hint_y=None,
            height=dp(35)
        )

        back_button.bind(on_release=self.go_back)

        root.add_widget(back_button)

        # -------------------------
        # BOTTOM SPACE
        # -------------------------

        root.add_widget(Label(
            text="",
            size_hint_y=0.5
        ))

        self.add_widget(root)

    def update_background(self, *args):
        self.background.pos = self.children[0].pos
        self.background.size = self.children[0].size

    def go_back(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "landing"
        
                         ####
        ## CUSTOMER LOGIN ##
                         ####

class CustomerLoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical"
        )

        # -------------------------
        # CREAM BACKGROUND
        # -------------------------

        with root.canvas.before:

            Color(*CREAM)

            self.background = Rectangle(
                pos=root.pos,
                size=root.size
            )

        root.bind(
            pos=self.update_background,
            size=self.update_background
        )

        # -------------------------
        # TOP SPACE
        # -------------------------

        root.add_widget(Label(
            text="",
            size_hint_y=0.20
        ))

        # -------------------------
        # TITLE
        # -------------------------

        root.add_widget(Label(
            text="Customer Login",
            font_size=dp(24),
            bold=True,
            color=ORANGE,
            size_hint_y=None,
            height=dp(42)
        ))

        # -------------------------
        # SUBTITLE
        # -------------------------

        root.add_widget(Label(
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

        root.add_widget(holder)

        # -------------------------
        # BACK BUTTON
        # -------------------------

        back_button = Button(
            text="Back",
            font_size=dp(10),
            color=GRAY,
            background_normal="",
            background_color=(0, 0, 0, 0),
            size_hint_y=None,
            height=dp(35)
        )

        back_button.bind(on_release=self.go_back)

        root.add_widget(back_button)

        # -------------------------
        # BOTTOM SPACE
        # -------------------------

        root.add_widget(Label(
            text="",
            size_hint_y=0.5
        ))

        self.add_widget(root)

    def update_background(self, *args):
        self.background.pos = self.children[0].pos
        self.background.size = self.children[0].size

    def go_back(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "landing"
        
                               
### TOC PAG PININDOT ###

                       
class TermsScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical"
        )

        # -------------------------
        # CREAM BACKGROUND
        # -------------------------

        with root.canvas.before:

            Color(*CREAM)

            self.background = Rectangle(
                pos=root.pos,
                size=root.size
            )

        root.bind(
            pos=self.update_background,
            size=self.update_background
        )
        
        
        

                
        self.add_widget(root)

    def update_background(self, *args):
        self.background.pos = self.children[0].pos
        self.background.size = self.children[0].size

    def go_back(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "landing"
        
        
### HOW IT WORK BUTTON ###

                       
class HowScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical"
        )

        # -------------------------
        # CREAM BACKGROUND
        # -------------------------

        with root.canvas.before:

            Color(*CREAM)

            self.background = Rectangle(
                pos=root.pos,
                size=root.size
            )

        root.bind(
            pos=self.update_background,
            size=self.update_background
        )
        
        
        

                
        self.add_widget(root)

    def update_background(self, *args):
        self.background.pos = self.children[0].pos
        self.background.size = self.children[0].size

    def go_back(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "landing"        
                               


# =========================================================
# APP
# =========================================================

class MadaListApp(App):

    def build(self):

        self.title = "MadaList"

        sm = ScreenManager(
            transition=SlideTransition(duration=0.20)
        )

        sm.add_widget(
            LandingScreen(name="landing")
        )

        sm.add_widget(
            SellerLoginScreen(name="seller_login")
        )

        sm.add_widget(
            CustomerLoginScreen(name="customer_login")
        )
        
        sm.add_widget(
        
TermsScreen(name="terms_screen")
        )
        
        sm.add_widget(
        
HowScreen(name="how_screen")
        )

        return sm


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    MadaListApp().run()