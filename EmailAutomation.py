import streamlit as st
import yagmail
from apscheduler.schedulers.background import BackgroundScheduler

# ---------- CONFIG ----------
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"

# ---------- EMAIL FUNCTION ----------
def send_email(to, subject, body):
    yag = yagmail.SMTP(EMAIL, PASSWORD)
    yag.send(to=to, subject=subject, contents=body)

# ---------- SCHEDULER ----------
scheduler = BackgroundScheduler()
scheduler.start()

def schedule_daily_email():
    scheduler.add_job(
        send_email,
        "interval",
        hours=24,
        args=["admin@mail.com", "Daily Report", "Automated Report"]
    )

# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="Email Automation", layout="centered")

st.title("📧 Email Automation Dashboard")
st.caption("Pure Python. No frontend suffering.")

with st.form("email_form"):
    recipient = st.text_input("Recipient Email")
    subject = st.text_input("Email Subject")
    report = st.text_area("Report Content", height=200)

    send_now = st.form_submit_button("Send Email")
    schedule = st.form_submit_button("Schedule Daily Email")

if send_now:
    if recipient and subject and report:
        send_email(recipient, subject, report)
        st.success("Email sent successfully 🚀")
    else:
        st.error("Fill all fields 😐")

if schedule:
    schedule_daily_email()
    st.success("Daily email scheduled ⏰")
