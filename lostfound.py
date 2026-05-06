import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Get the exact folder where this Python script lives
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "lost_found.db")

# --- Database Setup ---
engine = create_engine(f"sqlite:///{db_path}")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# --- Models ---

class LostItem(Base):
    __tablename__ = "lost_items"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    description = Column(String)
    location = Column(String)


class FoundItem(Base):
    __tablename__ = "found_items"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    description = Column(String)
    location = Column(String)
    contact = Column(String)
    email = Column(String)


# Create tables
Base.metadata.create_all(engine)


# --- Add Lost Item ---
def add_lost_item():
    print("\n--- Add Lost Item ---")

    print("1. ID Card\n2. Wallet\n3. Book\n4. Phone\n5. Other")
    choice = input("Enter choice: ")

    if choice == '1':
        type_ = "ID Card"
        desc = input("Enter ID number: ")

    elif choice == '2':
        type_ = "Wallet"
        color = input("Enter color: ")
        money = input("Enter money: ")
        desc = f"Color: {color}, Money: {money}"

    elif choice == '3':
        type_ = "Book"
        desc = input("Enter book name: ")

    elif choice == '4':
        type_ = "Phone"
        brand = input("Enter brand: ")
        info = input("Enter description: ")
        desc = f"{brand} - {info}"

    elif choice == '5':
        type_ = "Other"
        name = input("Enter item name: ")
        info = input("Enter description: ")
        desc = f"{name} - {info}"

    else:
        print("Invalid choice!")
        return

    location = input("Enter lost location: ")

    item = LostItem(type=type_, description=desc, location=location)
    session.add(item)
    session.commit()

    print("✔ Lost item added\n")


# --- Add Found Item ---
def add_found_item():
    print("\n--- Add Found Item ---")

    print("1. ID Card\n2. Wallet\n3. Book\n4. Phone\n5. Other")
    choice = input("Enter choice: ")

    if choice == '1':
        type_ = "ID Card"
        desc = input("Enter ID number: ")

    elif choice == '2':
        type_ = "Wallet"
        color = input("Enter color: ")
        money = input("Enter money: ")
        desc = f"Color: {color}, Money: {money}"

    elif choice == '3':
        type_ = "Book"
        desc = input("Enter book name: ")

    elif choice == '4':
        type_ = "Phone"
        brand = input("Enter brand: ")
        info = input("Enter description: ")
        desc = f"{brand} - {info}"

    elif choice == '5':
        type_ = "Other"
        name = input("Enter item name: ")
        info = input("Enter description: ")
        desc = f"{name} - {info}"

    else:
        print("Invalid choice!")
        return

    location = input("Enter found location: ")
    contact = input("Enter contact: ")
    email = input("Enter email: ")

    item = FoundItem(
        type=type_,
        description=desc,
        location=location,
        contact=contact,
        email=email
    )

    session.add(item)
    session.commit()

    print("✔ Found item added\n")


# --- View Items ---
def view_items():
    print("\n--- Lost Items ---")
    for item in session.query(LostItem).all():
        print(f"{item.type} | {item.location}")
        print(f"{item.description}")
        print("-" * 30)

    print("\n--- Found Items ---")
    for item in session.query(FoundItem).all():
        print(f"{item.type} | {item.location}")
        print(f"{item.description}")
        print(f"Contact: {item.contact} | Email: {item.email}")
        print("-" * 30)


# --- Search Feature ---
def search_items():
    keyword = input("\nEnter keyword to search: ")

    print("\n--- Matching Lost Items ---")
    lost_results = session.query(LostItem).filter(
        LostItem.description.contains(keyword)
    ).all()

    if not lost_results:
        print("No matches found")
    else:
        for item in lost_results:
            print(f"{item.type} | {item.location}")
            print(item.description)
            print("-" * 30)

    print("\n--- Matching Found Items ---")
    found_results = session.query(FoundItem).filter(
        FoundItem.description.contains(keyword)
    ).all()

    if not found_results:
        print("No matches found")
    else:
        for item in found_results:
            print(f"{item.type} | {item.location}")
            print(item.description)
            print(f"Contact: {item.contact}")
            print("-" * 30)


# --- Main Menu ---
while True:
    print("\n1. Add Lost Item")
    print("2. Add Found Item")
    print("3. View Items")
    print("4. Search Items")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_lost_item()
    elif choice == '2':
        add_found_item()
    elif choice == '3':
        view_items()
    elif choice == '4':
        search_items()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")