
# Experiment 6: Client-Server Architecture

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

students = {}


class StudentServer(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        response = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        if self.path == "/students":
            self.send_json(200, students)
        else:
            self.send_json(404, {"message": "Route not found"})

    def do_POST(self):
        if self.path != "/students":
            self.send_json(404, {"message": "Route not found"})
            return

        try:
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length).decode("utf-8"))

            student_id = str(data.get("id", "")).strip()
            name = str(data.get("name", "")).strip()
            marks = data.get("marks")

            if not student_id or not name:
                self.send_json(400, {"message": "ID and name are required"})
                return

            if isinstance(marks, bool) or not isinstance(marks, (int, float)) or not 0 <= marks <= 100:
                self.send_json(400, {"message": "Marks must be between 0 and 100"})
                return

            if student_id in students:
                self.send_json(409, {"message": "Student ID already exists"})
                return

            students[student_id] = {
                "name": name,
                "marks": marks
            }

            self.send_json(201, {
                "message": "Student added successfully",
                "student": students[student_id]
            })

        except (ValueError, TypeError, json.JSONDecodeError):
            self.send_json(400, {"message": "Invalid request data"})


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), StudentServer)
    print("Student server running at http://127.0.0.1:8000")
    print("Press Ctrl+C to stop the server.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()
