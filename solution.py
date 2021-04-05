def converter(mpg):
  # Oh just a buncha math. Nothin' fancy.
  return round(mpg / 4.54609188 * 1.609344, 2)

def maskify(cc):
  # Return a `#` for every character but the last four,
  # then add the last four characters.
  return '#' * (len(cc) - 4) + cc[-4:]

def name_in_str(text, name):
  # For every character in the text:
  for c in text.lower():
    # If we've hit the next character in name:
    if c == name[0].lower():
      # Strip the first character off name (so we can check the net character next time)
      name = name[1:]
      # If there's no name left, we hit every character in name.
      if not name:
        return True

  # We never ran out of characters in name (or we would've returned above.)
  # So there were characters we didn't match.
  # So: False.
  return False
