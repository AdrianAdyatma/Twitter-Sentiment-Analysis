import re

string = "Jokowi... github.com/adrianadyatma @telah berhasil tahun, masa-masa mant.ap/$#==~!@#$%^&*() https://asu.com keluarga. #JokowiAja https://t.co/WAOAW9sja"

url = re.findall(r'[!-\-/-~]+\.[!-\-/-~]+', string)

print(url)
