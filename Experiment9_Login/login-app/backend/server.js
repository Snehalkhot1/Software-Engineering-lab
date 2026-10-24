const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

// Static login credentials
const STATIC_EMAIL = "test@gmail.com";
const STATIC_PASSWORD = "123456";

// Login API
app.post("/api/login", (req, res) => {
    const { email, password } = req.body;

    if (
        email === STATIC_EMAIL &&
        password === STATIC_PASSWORD
    ) {
        return res.status(200).json({
            success: true,
            message: "Login Successful"
        });
    }

    return res.status(401).json({
        success: false,
        message: "Login Failed: Invalid email or password"
    });
});

// Start the server
app.listen(5000, () => {
    console.log("Server running on http://localhost:5000");
});