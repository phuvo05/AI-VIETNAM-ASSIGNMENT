import streamlit as st

# Title
st.title("Ứng dụng quản lý công việc")

# Session state for storing tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Job input
job_name = st.text_input("Nhập tên công việc:", "AIO Learner")

# Priority selection
priority = st.slider("Chọn mức độ ưu tiên:", 1, 5, 5)

# Status selection
status = st.selectbox("Chọn trạng thái:", ["Đang làm", "Hoàn thành", "Chưa bắt đầu"])

# Add job button
if st.button("Thêm công việc"):
    new_task = {"name": job_name, "priority": priority, "status": status}
    st.session_state.tasks.append(new_task)
    st.success("Đã thêm công việc!")

# Display task list
st.subheader("Danh sách công việc:")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks, 1):
        st.write(f"{i}. {task['name']} - Ưu tiên: {task['priority']} - Trạng thái: {task['status']}")

    # Clear all tasks
    if st.button("Xóa danh sách"):
        st.session_state.tasks = []
        st.rerun()
