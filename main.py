from utils.main_functions import show_options, generate_output

def run():
    option1, option2 = show_options()
    generate_output(option1, option2)


if __name__ == "__main__":
    run()