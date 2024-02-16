from openai import OpenAI
from dotenv import load_dotenv
import os
import time
import schedule
from utils import send_email

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

assistant_id = "asst_IfIZWt6NBbOaydEmvK8kgRPD"

thread = client.beta.threads.create()

def job():
    #메시지 보내기
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="안녕, 오늘의 뉴스레터를 HTML 형식에 맞춰서 보내줘."
    )
    #답변 받기
    run = client.beta.threads.runs.create(
      thread_id=thread.id,
      assistant_id=assistant_id
    )

    while run.status != "completed":
        keep_retrieving_run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        # print(f"Run status: {keep_retrieving_run.status}")
        if keep_retrieving_run.status == "failed" :
            print(keep_retrieving_run.last_error)

        if keep_retrieving_run.status == "completed" :
            print("\n")
            break

    #답변 출력
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    send_email("GPT newsletter", messages.data[0].content[0].text.value, "heon0128@gamil.com")



schedule.every().day.at("01:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)