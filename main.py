import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

person_list = []
for contact in contacts_list:
  person = " ".join(contact[0:3]).strip(" ")
  person = person.replace(' ', ',')
  person_list.append(person)

i = 0
while i < len(person_list):
  person_list[i] = person_list[i].split(',')
  if len(person_list[i]) < 3:
    person_list[i].append(' ')
  i = i + 1

i = 0
while i < len(contacts_list):
  contacts_list[i][0] = person_list[i][0]
  contacts_list[i][1] = person_list[i][1]
  contacts_list[i][2] = person_list[i][2]
  i = i + 1

pattern = r"(\+7|8)\s*\(?(\d{3})\)?\s*\-?(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s-]*\(?(доб)?\.?\s*(\d{4}\s*)?\)?"
subst = r"+7(\2)\3-\4-\5 \6.\7"

i = 1
while i < len(contacts_list):
  contacts_list[i][5] = re.sub(pattern, subst, contacts_list[i][5])
  i = i + 1

for i, contact in enumerate(contacts_list):
  id = i + 1
  while id < len(contacts_list):
    if contact[0] == contacts_list[id][0] and contact[1] == contacts_list[id][1]:
      c = 0
      while c < len(contact):
        if contact[c] == '':
          contact[c] = contacts_list[id][c]
        c = c + 1
      del(contacts_list[id])
    id = id + 1

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)