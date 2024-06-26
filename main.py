def main():
    ##################################################
    # Comlete your code here
    ##################################################
    number = int(input('Enter your input: '))
    """
    Make your code here
    """

    if (number % 2) == 0:
        print(f'The value {number} is even')
        result = "0"
    else:
        print(f'The value {number} is an odd')
        result = "1"

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()