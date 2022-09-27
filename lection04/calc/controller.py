import model_del as model
import view

def button_click(): # метод нажатия на кнопку
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b) # инициализация начальных значений
    result = model.do_it()
    view.view_data(result, "result")