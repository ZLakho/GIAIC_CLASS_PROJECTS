def main():
    temp_in_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    temp_in_celcius = (temp_in_fahrenheit - 32)*5.0/9.0
    print(f"Temperature {temp_in_fahrenheit} in fahrenheit is equals to {temp_in_celcius} degree celcius")


if __name__ == "__main__":
    main()