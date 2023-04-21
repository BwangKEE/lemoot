import subprocess
packages = ['openai']
def install(packages):
  subprocess.call(['pip','install',package])
for package in packages:
  print('\nmenginstall :',package,' (harap tunggu sebentar...  C:nadzib)')
  install(package)


import openai
#intro
print("\n\n\nSelamat datang saya adalah mesin AI-HRD")
print('\nAPI KEYS bisa di dapatkan disini : https://platform.openai.com/account/api-keys')
#input pengguna
apik = input('\nmasukkan API KEYS openai anda :')
nama = input('\nMasukkan nama anda :')

#sistem
messages = [
  {'role':'system','content':'kamu adalah seorang perekrut yang akan menguji dan menanyakan pertanyaan interview kepada pelamar kerja.Kamu menanyakan pertanyaan barus setiap saya selesai memberikan jawaban.Selalu menggunakan bahasa indonesia dalam menjawab pertanyaan'}
]
while True:
  content = input(f'\n{nama} :')
  messages.append({'role':'user','content':content})
  openai.api_key = (str(apik))
  completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages = messages
  )


  #output
  chat_response = (completion.choices[0].message.content)
  print(f'\n[+]AI-HRD:{chat_response}')
  messages.append({'role':'assistant','content': chat_response})
