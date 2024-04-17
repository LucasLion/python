
import datetime
import time

sec = time.time();
sec_for = "{:,.4f}".format(sec);
sec_sc = f"{sec:.4e}"
print(f"Seconds since January 1, 1970: {sec_for} or {sec_sc} in scientific notation")

now = datetime.datetime.now()
formatted = now.strftime('%b %d %Y')
print(formatted)
