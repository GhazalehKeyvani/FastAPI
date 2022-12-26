
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = [
    {'name': 'Student 1', 'age': 20},
    {'name': 'Student 2', 'age': 18},
    {'name': 'Student 3', 'age': 16}
]
#filtering 

@app.get('/students')
def user_list(min: Optional[int] = None, max: Optional[int] = None):
    if min and max:
        filtered_students = list(
            filter(lambda student: max >= student['age'] >= min, students)
        )
        return {'students': filtered_students}
    return {'students': students}

#fetching
def student_check(student_id):
    if not students[student_id]:
        raise HTTPException(status_code=404, detail='Student Not Found')

@app.get('/students/{student_id}')
def user_detail(student_id: int):
    student_check(student_id)
    return {'student': students[student_id]}

#create schema for get data and changing

class Student(BaseModel):
    name: str
    age: int

#POST data

@app.post('/students')
def user_add(student: Student):
    students.append(student)

    return {'student': students[-1]}


#PUT 

@app.put('/students/{student_id}')
def user_update(student: Student, student_id: int):
    student_check(student_id)
    students[student_id].update(student)

    return {'student': students[student_id]}


#DELET

@app.delete('/students/{student_id}')
def user_delete(student_id: int):
    student_check(student_id)
    del students[student_id]

    return {'students': students}























































































# from googleapiclient.discovery import build
# from google.oauth2 import service_account
# from fastapi import FastAPI, File, UploadFile
# from pydantic import BaseModel
 
# app = FastAPI()

# # SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# # SERVICE_ACCOUNT_FILE = 'keys.json'

# # creds = None
# # creds = service_account.Credentials.from_service_account_file(
# #         SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# # # If modifying these scopes, delete the file token.json.

# # # a sample spreadsheet.
# # SAMPLE_SPREADSHEET_ID = '1k8CvFGj79y-GYG8M_sFJDM3AnBDq7H2kLPkvGvRTfDk'
# # service = build('sheets', 'v4', credentials=creds)
# # sheet = service.spreadsheets()



# # @app.get('{SCOPES}/{SAMPLE_SPREADSHEET_ID}')
# # def detail(SAMPLE_SPREADSHEET_ID):
# #     sheet.check(SAMPLE_SPREADSHEET_ID)
# #     return {'sheet': sheet[SAMPLE_SPREADSHEET_ID]}

# def data_check(data_id):
#     if not datas[data_id]:
#         raise HTTPException(status_code=404, detail='data Not Found')

# # datas = [
# #   {'name': 'data 1', 'age': 20},
# #   {'name': 'data 2', 'age': 18},
# #   {'name': 'data 3', 'age': 16}
# # ]



# excel_file_path = r"C:\Users\ghkey\Desktop\fastapi\the_excel_file.xlsx"
# class ExcelRequestInfo(BaseModel):
#     client_id: str

# @app.post('/')
# #@app.get('/datas/{data_id}')
# def detail(datas:UploadFile=File()):
#     data_check(data_id)
#     headers = {'Content-Disposition': 'attachment; filename="Book.xlsx"'}
#     return FileResponse(excel_file_path, headers=headers)
#     #return {'datas':json.load(UploadFile.file)}
#     # return {'data': datas[data_id]}




# # @app.get('/datas/{data_id}')
# # def user_detail(data_id: int):
# #     data_check(data_id)
# #     return {'data': datas[data_id]}


