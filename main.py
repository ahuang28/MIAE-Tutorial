def main_wrapper():
    # Attributes are a thing!
    print(f"This is the start of our Python project. This function's name is {main_wrapper.__name__}")

    # Code here
    utils.solid_example_1(example_param_1="a", example_param_2=1)

    print("This is the end of our Python project.")


if __name__ == "__main__":
    main_wrapper()