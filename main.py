from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''

MDScreenManager:

    MDScreen:
        name: "Главная"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True


            MDTopAppBar:
                id: toolbar
                title: "En-Study"
                elevation: 4
                pos_hint: {"top": 1}
                md_bg_color: "#e7e4c0"
                specific_text_color: "#4a4939"



            BoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}   


                Button:
                    text: "Существительное"
                    background_color: '#e7e4c0'
                    theme_text_color: "Custom"
                    text_color: "white"
                    on_release:
                        root.current = "Существительное_1"                        

                Button:
                    text: "Артикль"
                    background_color: '#e7e4c0'
                    theme_text_color: "Custom"
                    text_color: "white"
                    on_release:
                        root.current = "Артикль_1"                        

                Button:
                    text: "Прилагательное"
                    theme_text_color: "Custom"
                    background_color: '#e7e4c0'
                    text_color: "white"
                    on_release:
                        root.current = "Прилагательное_1"                        

                Button:
                    text: "Глагол"
                    theme_text_color: "Custom"
                    background_color: '#e7e4c0'
                    text_color: "white"
                    on_release:
                        root.current = "Глагол_1"                        

                Button:
                    text: "Времена глагола и условные предложения"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'
                    on_release:
                        root.current = "Времена глагола и условные предложения_1"                        

                Button:
                    text: "Лексика"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Лексика_1"

    MDScreen:
        name: "Существительное_1"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Голос певицы" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "a singers’ voice"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0' 
                        on_release:
                            self.background_color = 'red'
                            root.current = "Существительное_2"           

                    Button:
                        text: "a singers voice"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Существительное_2"

                    Button:
                        text: "a singer’s voice"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green' 
                            root.current = "Существительное_2"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Существительное_2"

    MDScreen:
        name: "Существительное_2"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Собака Дэвида" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "Davids’ dog"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Существительное_3"

                    Button:
                        text: "Davids dog"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Существительное_3"

                    Button:
                        text: "David’s dog"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green' 
                            root.current = "Существительное_3"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Существительное_3"      


    MDScreen:
        name: "Существительное_3"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Window" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "Windowes"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Существительное_4"

                    Button:
                        text: "Windows"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green' 
                            root.current = "Существительное_4"

                    Button:
                        text: "Windowz"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Существительное_4"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Существительное_4"      





    MDScreen:
        name: "Существительное_4"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Лучшая роль актрисы" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "the actress’s best role"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green' 
                            root.current = "Существительное_5"

                    Button:
                        text: "the actresses best role"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Существительное_5"

                    Button:
                        text: "the actress best role"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Существительное_5"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Существительное_5"      


    MDScreen:
        name: "Существительное_5"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1}  

            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Wolf" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "Wolfes"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Главная"

                    Button:
                        text: "Wolves"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green' 
                            root.current = "Главная"

                    Button:
                        text: "Wolfs"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Главная"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Закончить"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "score:5"      













    MDScreen:
        name: "Артикль_1"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Harry is from the USA." 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "True"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green' 
                            root.current = "Артикль_2"

                    Button:
                        text: "False"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Артикль_2"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Артикль_2"

    MDScreen:
        name: "Артикль_2"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "What a good dog!" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "True"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green' 
                            root.current = "Артикль_3"

                    Button:
                        text: "False"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Артикль_3"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Артикль_3"      


    MDScreen:
        name: "Артикль_3"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "This is a last time you are late." 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "True"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Артикль_4"

                    Button:
                        text: "False"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green' 
                            root.current = "Артикль_4"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Артикль_4"             

    MDScreen:
        name: "Артикль_4"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "When was the first time someone crossed the Atlantic Ocean?" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "True"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green' 
                            root.current = "Артикль_5"

                    Button:
                        text: "False"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Артикль_5"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Артикль_5"      

    MDScreen:
        name: "Артикль_5"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1}  

            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "I'll call her later, after we have a breakfast." 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "True"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red' 
                            root.current = "Главная"

                    Button:
                        text: "False"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green' 
                            root.current = "Главная"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Закончить"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "score:5" 












    MDScreen:
        name: "Прилагательное_1"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Лед холоднее, чем мороженое" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "Ice is coldest than ice-cream"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Прилагательное_2"

                    Button:
                        text: "Ice is cold than ice-cream"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Прилагательное_2"

                    Button:
                        text: "Ice is colder than ice-cream"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Прилагательное_2"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Прилагательное_2"

    MDScreen:
        name: "Прилагательное_2"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Воробей – самая красивая в мире птица" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "Sparrow is the most beautiful bird in the world"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Прилагательное_3"

                    Button:
                        text: "Sparrow is the beautifulest bird in the world"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Прилагательное_3"

                    Button:
                        text: "Sparrow is the more beautiful bird in the world"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Прилагательное_3"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Прилагательное_3"      


    MDScreen:
        name: "Прилагательное_3"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Он старше, чем Джек" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "He is the older than Jack"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Прилагательное_4"

                    Button:
                        text: "He is older than Jack"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Прилагательное_4"

                    Button:
                        text: "He is more older than Jack"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Прилагательное_4"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Прилагательное_4"             

    MDScreen:
        name: "Прилагательное_4"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Крысы опаснее мышей" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "Rats are the most danger than mice"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Прилагательное_5"

                    Button:
                        text: "Rats are more dangerous than mice"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Прилагательное_5"

                    Button:
                        text: "Rats are dangerouser than mice"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Прилагательное_5"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Прилагательное_5"      

    MDScreen:
        name: "Прилагательное_5"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1}  

            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "У меня есть решение получше" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "I have got the best decision"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Главная"

                    Button:
                        text: "I have got a better decision"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Главная"

                    Button:
                        text: "I have got a gooder decision"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Главная"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Закончить"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "score:5" 






    MDScreen:
        name: "Глагол_1"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "У меня есть немного печенья." 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "I has got some cookies."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Глагол_2"

                    Button:
                        text: "I haven't got some cookies."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Глагол_2"

                    Button:
                        text: "I have got some cookies."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Глагол_2"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Глагол_2"

    MDScreen:
        name: "Глагол_2"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Дэвид мог бы и купить дом, но он предпочел арендовать его." 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "David could have bought the house but he prefered to rent it."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Глагол_3"

                    Button:
                        text: "David could have been bought the house but he prefered to rent it."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Глагол_3"

                    Button:
                        text: "David could bought the house but he prefered to rent it."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Глагол_3"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Глагол_3"      


    MDScreen:
        name: "Глагол_3"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Можно мне отменить свой заказ?" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "I may cancel my order?"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Глагол_4"

                    Button:
                        text: "Might I cancel my order?"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Глагол_4"

                    Button:
                        text: "May I cancel my order?"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Глагол_4"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Глагол_4"             

    MDScreen:
        name: "Глагол_4"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "You should try asking her out. She likes you." 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "Ты обязан пригласить ее. Ты ей нравишься."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Глагол_5"

                    Button:
                        text: "Тебе не стоит пробовать приглашать ее. Она такая же как ты."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Глагол_5"

                    Button:
                        text: "Тебе следут попробовать пригласить ее. Ты ей нравишься."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Глагол_5"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Глагол_5"      

    MDScreen:
        name: "Глагол_5"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1}  

            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "You missed a good show. You should have seen it. " 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "Ты пропустил хорошее представление. Тебе и не следовать его смотреть. "
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Главная"

                    Button:
                        text: "Ты пропустил хорошее представление. Жаль, что ты его не увидел. "
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Главная"

                    Button:
                        text: "Ты пропустил хорошее представление. Тебе следует иметь это в виду. "
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Главная"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Закончить"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "score:5" 







    MDScreen:
        name: "Времена глагола и условные предложения_1"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Вы сейчас пишете письмо?" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "Is you writing a letter now?"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Времена глагола и условные предложения_2"

                    Button:
                        text: "Are you writing a letter now?"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Времена глагола и условные предложения_2"

                    Button:
                        text: "Do you writing a letter now?"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Времена глагола и условные предложения_2"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Времена глагола и условные предложения_2"

    MDScreen:
        name: "Времена глагола и условные предложения_2"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "John has lived in Japan ___ 2015" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "for"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Времена глагола и условные предложения_3"

                    Button:
                        text: "since"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Времена глагола и условные предложения_3"



            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Времена глагола и условные предложения_3"      


    MDScreen:
        name: "Времена глагола и условные предложения_3"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Мой кот вчера был сердитым. Я забыл его покормить." 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "My cat was angry yesterday. I have forgotten to feed it. "
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Времена глагола и условные предложения_4"

                    Button:
                        text: "My cat was angry yesterday. I forgot to feed it. "
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Времена глагола и условные предложения_4"



            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Времена глагола и условные предложения_4"             

    MDScreen:
        name: "Времена глагола и условные предложения_4"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Если у вас будут вопросы, задавайте их менеджеру." 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "If you have any questions, ask the manager."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Времена глагола и условные предложения_5"

                    Button:
                        text: "If you had any questions, ask the manager."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Времена глагола и условные предложения_5"

                    Button:
                        text: "If you will have any questions, ask the manager."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Времена глагола и условные предложения_5"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Времена глагола и условные предложения_5"      

    MDScreen:
        name: "Времена глагола и условные предложения_5"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1}  

            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Если вы все делаете правильно, вам не нужно беспокоиться." 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "If you do everything right, you won't need to worry.  "
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Главная"

                    Button:
                        text: "If you did everything right, you would need to worry.  "
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Главная"

                    Button:
                        text: "If you do everything right, you don't need to worry.  "
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Главная"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Закончить"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "score:5" 









    MDScreen:
        name: "Лексика_1"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Представление должно продолжаться!" 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "Show must be put off!"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Лексика_2"

                    Button:
                        text: "Show must be go on!"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Лексика_2"

                    Button:
                        text: "Show must get along!"
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Лексика_2"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Лексика_2"

    MDScreen:
        name: "Лексика_2"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Фильм выходит в декабре. " 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "The movie is coming around in December."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Лексика_3"

                    Button:
                        text: "The movie is coming out in December."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Лексика_3"

                    Button:
                        text: "The movie is coming off in December."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Лексика_3"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Лексика_3"      


    MDScreen:
        name: "Лексика_3"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Я давно не видел племянника. Он вырос." 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "I haven’t seen my nephew for a long time. He has risen up."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Лексика_4"

                    Button:
                        text: "I haven’t seen my nephew for a long time. He has grown up."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Лексика_4"

                    Button:
                        text: "I haven’t seen my nephew for a long time. He has talled up."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Лексика_4"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Лексика_4"             

    MDScreen:
        name: "Лексика_4"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1} 


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Телефон звонит, возьми трубку." 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "The phone is ringing, pick it up."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Лексика_5"

                    Button:
                        text: "The phone is ringing, grab it up."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Лексика_5"

                    Button:
                        text: "The phone is ringing, get it up."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Лексика_5"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Дальше"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Лексика_5"      

    MDScreen:
        name: "Лексика_5"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1}  

            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1} 


                MDLabel:
                    id: 'label_1'
                    text: "Сделайте музыку погромче, пожалуйста." 
                    halign: "center"  

                BoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '12dp'
                    pos_hint: {"top": 1} 

                    Button:
                        text: "Switch the music up, please."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Главная"

                    Button:
                        text: "Make the music up, please."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'red'
                            root.current = "Главная"

                    Button:
                        text: "Turn the music up, please."
                        theme_text_color: "Custom"
                        text_color: "white"
                        background_color: '#e7e4c0'  
                        on_release:
                            self.background_color = 'green'
                            root.current = "Главная"


            BoxLayout:
                orientation: "horizontal"
                adaptive_height: True
                padding: '25dp'
                spacing: '12dp'
                pos_hint: {"top": 1}  

                Button:
                    text: "На главную"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "Главная"



                Button:
                    text: "Закончить"
                    theme_text_color: "Custom"
                    text_color: "white"
                    background_color: '#e7e4c0'  
                    on_release:
                        root.current = "score:5"     

    MDScreen:
        name: "score:5"

        BoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: '25dp'
            spacing: '12dp'
            pos_hint: {"top": 1}  

            MDLabel:
                id: 'label_1'
                text: "Congratulations!!!"
                halign: "center" 

            MDLabel:
                id: 'label_1'
                text: "Score: 5"
                halign: "center" 

            Button:
                text: "На главную"
                theme_text_color: "Custom"
                text_color: "white"
                background_color: '#e7e4c0'  
                on_release:
                    root.current = "Главная"


'''


class En_studyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


En_studyApp().run()

