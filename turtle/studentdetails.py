student_data = {
    "id1":{"name": 'Nimo', "standard": 'IV', "subjects": 'english,maths,science'},
    "id2":{"name": 'kylie', "standard": 'V', "subjects": 'english,maths,science'},
    "id3":{"name": 'Sarah', "standard": 'V', "subjects": 'english,maths,science'},
    "id4":{"name": 'Nimo', "standard": 'IV', "subjects": 'english,maths,science'}
}
result = {}
seen_key = []

for student_id, details in student_data.items():
    unique_id = (details["name"], details["standard"], details["subjects"])
    if unique_id not in seen_key:
      seen_key.append(unique_id)
      result[student_id] = details

for k, v in result.items():
    print(k, ":", v)