from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from random import randint, choice

class MathQuiz(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.question_label = Label(text="Press Start to Begin", font_size=24)
        self.answer_input = TextInput(hint_text="Enter your answer", multiline=False, font_size=20)
        self.result_label = Label(text="", font_size=20)

        self.start_btn = Button(text="Start Question", on_press=self.new_question)
        self.submit_btn = Button(text="Submit", on_press=self.check_answer)

        self.layout.add_widget(self.question_label)
        self.layout.add_widget(self.answer_input)
        self.layout.add_widget(self.submit_btn)
        self.layout.add_widget(self.start_btn)
        self.layout.add_widget(self.result_label)

        return self.layout

    def new_question(self, instance):
        self.a = randint(10, 100)
        self.b = randint(10, 100)
        self.op = choice(["+", "-", "*"])

        if self.op == "+":
            self.result = self.a + self.b
        elif self.op == "-":
            self.result = self.a - self.b
        else:
            self.result = self.a * self.b

        self.question_label.text = f"Solve: {self.a} {self.op} {self.b}"
        self.result_label.text = ""
        self.answer_input.text = ""

    def check_answer(self, instance):
        try:
            user_ans = int(self.answer_input.text)
            if user_ans == self.result:
                self.result_label.text = "✅ Correct!"
            else:
                self.result_label.text = f"❌ Wrong! Correct: {self.result}"
        except:
            self.result_label.text = "⚠️ Enter a number"

if __name__ == "__main__":
    MathQuiz().run()
