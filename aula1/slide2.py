def string(s):

    # Reverse the string
    reversed = s[::-1]
    print(f"Reversed string: {reversed}")

    # Returns how many “a” and “A” characters are present in the string
    n_a = s.count('a') + s.count('A')
    print(f"Number of 'a' and 'A' characters: {n_a}")

    #  Returns the number of vowels there are present in the string
    v = 'aeiouAEIOU'
    n_v = sum(1 for char in s if char in v)
    print(f"Number of vowels: {n_v}")

    # Convert to lowercase
    l = s.lower()
    print(f"Lowercase string: {l}")

    # Convert to uppercase
    u = s.upper()
    print(f"Uppercase string: {u}")