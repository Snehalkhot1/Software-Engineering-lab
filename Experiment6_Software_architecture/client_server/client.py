
# Client for Student Management System

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

BASE_URL = "http://127.0.0.1:8000"


def request_server(path, method="GET", data=None):
    body = None

    if data is not None:
        body = json.dumps(data).encode("utf-8")

    request = Request(
        BASE_URL + path,
        data=body,
        method=method,
        headers={"Content-Type": "application/json"}
    )

    try:
        with urlopen(request, timeout=5) as response:
            return json.loads(response.read().decode("utf-8"))

    except HTTPError as error:
        return json.loads(error.read().decode("utf-8"))

    except URLError:
        return {"message": "Cannot connect. Start the server first."}


def main():
    while True:
        print("\n--- Client Menu ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            student_id = input("Student ID: ")
            name = input("Student name: ")

            try:
                marks = float(input("Marks: "))
                result = request_server(
                    "/students",
                    "POST",
                    {"id": student_id, "name": name, "marks": marks}
                )
                print(result)
            except ValueError:
                print("Marks must be a number.")

        elif choice == "2":
            print(request_server("/students"))

        elif choice == "3":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
