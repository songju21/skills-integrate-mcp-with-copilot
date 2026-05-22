"""
Seed script for initial DB data (roles, activities, demo users)
"""
from src.models import Base, User, Role, Activity
from src.database import engine, SessionLocal

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    # Roles
    admin_role = Role(name="admin")
    student_role = Role(name="student")
    teacher_role = Role(name="teacher")
    db.add_all([admin_role, student_role, teacher_role])
    db.commit()
    # Activities
    activities = [
        Activity(name="Chess Club", description="Learn strategies and compete in chess tournaments", schedule="Fridays, 3:30 PM - 5:00 PM", max_participants=12),
        Activity(name="Programming Class", description="Learn programming fundamentals and build software projects", schedule="Tuesdays and Thursdays, 3:30 PM - 4:30 PM", max_participants=20),
        Activity(name="Gym Class", description="Physical education and sports activities", schedule="Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM", max_participants=30),
    ]
    db.add_all(activities)
    db.commit()
    # Demo user
    admin = User(email="admin@school.edu", name="Admin", role=admin_role)
    db.add(admin)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed()
