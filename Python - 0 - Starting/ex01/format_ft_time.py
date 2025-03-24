from datetime import date, datetime

actual = datetime.now()
sec = datetime.timestamp(actual)
print(f"Seconds since January 1, 1970: {sec:,.4f} or {sec:.2e} in scientific notation")
today = date.today()
d = today.strftime("%B %d %Y")
print(d)