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
        number = "0"
    else:
        print(f'The value {number} is an odd')
        number = "1"

    ########################################
    # Do not delete the return statement
    ########################################
    return result

if __name__ == '__main__':
    main()