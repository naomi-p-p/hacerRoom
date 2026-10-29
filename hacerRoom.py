def decode_message(message):
    if not isinstance(message, str) or len(message) < 2:
        raise ValueError("message must be a string with at least 2 characters")
    digit = message[1]
    print(digit)
    return digit


def slice_message(message):
    return message[1::2]


def find_suspicious_accounts(accounts):
    suspects = []
    for username, details in accounts.items():
        if details.get("failed_logins", 0) >= 5 and details.get("location") == "UNKNOWN":
            suspects.append(username)
    return suspects


def find_final_digit(candidates):
    for candidate in candidates:
        first, middle, last = (int(ch) for ch in candidate)
        if middle == 2 and first > last:
            return candidate[-1]
    return None  # safe fallback: no matching candidate


# --- Test ---
message = "K4P9Z2"
accounts = {
    "neo": {"failed_logins": 1, "location": "HQ", "token": "N3O"},
    "trinity": {"failed_logins": 7, "location": "UNKNOWN", "token": "TR7"},
    "morpheus": {"failed_logins": 2, "location": "HQ", "token": "M8P"},
}
candidates = ["583", "126", "942", "371", "805", "722"]

digit1 = decode_message(message)
suspects = find_suspicious_accounts(accounts)
digit2 = accounts[suspects[0]]["token"][-1]
digit3 = find_final_digit(candidates)

print("Suspicious:", suspects)
print("Final code:", digit1 + digit2 + digit3)