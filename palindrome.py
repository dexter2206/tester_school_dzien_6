def is_palindrome(text):
    """Checks if text is a palindrome.

    Args:
        text: string to be checked
    Returns:
        True if text is a palindrome, False otherwise
    """
    text = text.lower()
    for i in range(len(text) // 2):
        if text[i] != text[len(text)-i-1]:
            return False
    return True

textttt = 'Oko'
print(is_palindrome(text=textttt))
print(textttt)