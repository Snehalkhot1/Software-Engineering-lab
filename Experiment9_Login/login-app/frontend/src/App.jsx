
import { useState } from "react";

export default function App() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const [loggedIn, setLoggedIn] = useState(false);

    const handleLogin = async (e) => {
        e.preventDefault();

        try {
            const res = await fetch(
                "http://localhost:5000/api/login",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ email, password })
                }
            );

            const data = await res.json();

            setMessage(data.message);
            setLoggedIn(data.success);
        } catch (err) {
            setMessage(
                "Server not reachable. Start the backend first."
            );
        }
    };

    if (loggedIn) {
        return (
            <div style={{
                textAlign: "center",
                marginTop: 80
            }}>
                <h2>Welcome, {email}</h2>
                <p>{message}</p>

                <button onClick={() => {
                    setLoggedIn(false);
                    setPassword("");
                    setMessage("");
                }}>
                    Logout
                </button>
            </div>
        );
    }

    return (
        <form
            onSubmit={handleLogin}
            style={{
                maxWidth: 320,
                margin: "80px auto"
            }}
        >
            <h2>Login</h2>

            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
            />

            <br /><br />

            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
            />

            <br /><br />

            <button type="submit">Login</button>

            <p>{message}</p>
        </form>
    );
}
