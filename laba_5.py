import fileinput
from functools import reduce

# Пример функций для обработки данных
def preprocess_data(data):
    # Предположим, что это ваша функция предварительной обработки
    return data.strip().lower()

def process_data(data):
    # Предположим, что это ваша функция обработки данных
    return data.replace('a', 'b')

def write_data(data, output_file):
    # Функция для записи данных в файл
    with open(output_file, 'a') as f:
        f.write(data + '\n')

# Функция для создания композиции функций
def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

# Создание композиции функций для обработки данных
data_pipeline = compose(preprocess_data, process_data)

# Потоковая обработка данных из файла и запись результата в другой файл
input_file = 'input.txt'
output_file = 'output.txt'

with fileinput.input(files=(input_file)) as f_input:
    for line in f_input:
        processed_data = data_pipeline(line)
        write_data(processed_data, output_file)
