import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
client = gspread.authorize(creds)

doc = client.open_by_url('https://docs.google.com/spreadsheets/d/1ScsLVltxRNiKJFuW5SB8eiFuNBuv_SoOOaK1_enqU8g/edit#gid=0')

sheet1 = doc.worksheet('시트1')

cnt = int(sheet1.cell(1, 2).value)
print('기존 행수: ', cnt)
sheet1.insert_row(['지마켓', '사탕/젤리/초콜릿/특별기획전', '7800', 'https://iten/gmarket.co.kr/'], 3)

sheet1.update_cell(1, 2, str(cnt + 10000))
