from docxtpl import DocxTemplate
from datetime import datetime
import pandas as pd

doc = DocxTemplate("template-manager-info.docx")

my_name = " Florian Remus "
my_phone = "0770 864 332"
my_email = "remusbalaj@yahoo.com"
my_address = "Oradea"
today_date = datetime.today().strftime("%d %b, %Y")

my_context = {'my_name': my_name, 'my_phone': my_phone, 'my_email': my_email, 'my_address': my_address,
              'today_date': today_date}

# df = dataframe = the table
df = pd.read_csv('users_data.csv')

for index, row in df.iterrows():
    context = {'hiring_manager_name': row['name'],
               'address': row['address'],
               'phone_number': row['phone_number'],
               'email': row['email'],
               'job_position': row['job'],
               'company_name': row['company']}

    context.update(my_context)

    doc.render(context)
    doc.save(f"generated_doc_{index}.docx")

