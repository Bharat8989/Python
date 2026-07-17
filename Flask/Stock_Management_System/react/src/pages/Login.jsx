import { useState } from "react";
import api from "../api/axios";

function Login() {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async (e) => {

        e.preventDefault();

        try {

            const response = await api.post("/login", {
                email,
                password
            });

            console.log(response.data);

            if (response.data.status) {

                localStorage.setItem("token", response.data.token);

                alert("Login Successful");

            } else {

                alert(response.data.message);

            }

        } catch (error) {

            console.log(error);

            if (error.response) {
                alert(error.response.data.message);
            } else {
                alert("Server Error");
            }

        }

    };

    return (

        <div
            style={{
                width: "350px",
                margin: "100px auto",
                padding: "20px",
                border: "1px solid gray",
                borderRadius: "10px"
            }}
        >

            <h2>Login</h2>

            <form onSubmit={handleLogin}>

                <input
                    type="email"
                    placeholder="Enter Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    style={{
                        width: "100%",
                        padding: "10px",
                        marginBottom: "10px"
                    }}
                />

                <input
                    type="password"
                    placeholder="Enter Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    style={{
                        width: "100%",
                        padding: "10px",
                        marginBottom: "10px"
                    }}
                />

                <button
                    type="submit"
                    style={{
                        width: "100%",
                        padding: "10px"
                    }}
                >
                    Login
                </button>

            </form>

        </div>

    );

}

export default Login;