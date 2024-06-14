import random
import string

def generate_password(length):
  """
  Generates a random password of the specified length.

  Args:
      length: The desired length of the password.

  Returns:
      A randomly generated password string.
  """

  # Define character sets for different password elements
  lowercase_letters = string.ascii_lowercase
  uppercase_letters = string.ascii_uppercase
  digits = string.digits
  punctuation = string.punctuation

  # Combine all character sets
  all_characters = lowercase_letters + uppercase_letters + digits + punctuation

  # Ensure at least one character from each set is included
  password = (
      random.choice(lowercase_letters)
      + random.choice(uppercase_letters)
      + random.choice(digits)
      + random.choice(punctuation)
  )

  # Fill the remaining characters with random selections from all characters
  password += ''.join(random.choices(all_characters, k=length - 4))

  # Shuffle the characters for better randomness (optional)
  # random.shuffle(list(password))
  # password = ''.join(password)

  return password

# Get password length from user
password_length = int(input("Enter desired password length: "))

# Generate and display password
generated_password = generate_password(password_length)
print("Your generated password is:", generated_password)
