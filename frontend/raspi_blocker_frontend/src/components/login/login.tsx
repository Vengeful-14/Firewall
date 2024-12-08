// import React, { useState } from "react";
// import { auth, signInWithEmailAndPassword } from "../../services/firebase.service";
// import { useNavigate } from "react-router-dom"; // Import useNavigate
// import "./login.css";

// const Login: React.FC = () => {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [error, setError] = useState("");
//   const [loading, setLoading] = useState(false); // Add loading state

//   const navigate = useNavigate(); // Initialize the navigate function

//   const handleLogin = async (e: React.FormEvent) => {
//     e.preventDefault();
//     setLoading(true); // Set loading to true when starting the login process

//     try {
//       // Firebase Authentication Sign-In
//       await signInWithEmailAndPassword(auth, email, password);
//     //   alert("Login successful!");

//       // Redirect to the DashboardHome
//       navigate("/dashboard"); // Navigates to the Dashboard route
//     } catch (err: any) {
//       console.error("Login failed:", err);
//       setError("Wrong email or password!");
//     } finally {
//       setLoading(false); // Set loading to false once the authentication is complete (success or error)
//     }
//   };

//   return (
//     <div className="login-container">
//       <h1>LOGIN</h1>
//       <form onSubmit={handleLogin}>
//         <div className="form-group">
//           <input
//             type="email"
//             id="email"
//             placeholder="Email"
//             value={email}
//             onChange={(e) => setEmail(e.target.value)}
//             required
//           />
//         </div>
//         <div className="form-group">
//           <input
//             type="password"
//             id="password"
//             placeholder="Password"
//             value={password}
//             onChange={(e) => setPassword(e.target.value)}
//             required
//           />
//         </div>
//         {error && <p className="error-message">{error}</p>}
//         {loading ? (
//           <div className="loader"></div> // Show loader when loading is true
//         ) : (
//           <button id="submitBtn" type="submit">Login</button>
//         )}
//       </form>
//     </div>
//   );
// };

// export default Login;


import React, { useState } from "react";
import { auth, signInWithEmailAndPassword } from "../../services/firebase.service";
import { useNavigate } from "react-router-dom"; // Import useNavigate
import { FaEye, FaEyeSlash } from "react-icons/fa"; // Import Eye icons from react-icons
import "./login.css";

const Login: React.FC = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false); // Add loading state
  const [passwordVisible, setPasswordVisible] = useState(false); // State for password visibility toggle

  const navigate = useNavigate(); // Initialize the navigate function

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true); // Set loading to true when starting the login process

    try {
      // Firebase Authentication Sign-In
      await signInWithEmailAndPassword(auth, email, password);
      // Redirect to the DashboardHome
      navigate("/dashboard"); // Navigates to the Dashboard route
    } catch (err: any) {
      console.error("Login failed:", err);
      setError("Wrong email or password!");
    } finally {
      setLoading(false); // Set loading to false once the authentication is complete (success or error)
    }
  };

  const togglePasswordVisibility = () => {
    setPasswordVisible((prev) => !prev); // Toggle password visibility
  };

  return (
    <div className="login-container">
      <h1>LOGIN</h1>
      <form onSubmit={handleLogin}>
        <div className="form-group">
          <input
            type="email"
            id="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <input
            type={passwordVisible ? "text" : "password"} // Toggle the input type between "text" and "password"
            id="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          {/* Toggle button for password visibility */}
          <span
            className="password-toggle-icon"
            onClick={togglePasswordVisibility}
          >
            {passwordVisible ? <FaEyeSlash /> : <FaEye />}
          </span>
        </div>
        {error && <p className="error-message">{error}</p>}
        {loading ? (
          <div className="loader"></div> // Show loader when loading is true
        ) : (
          <button id="submitBtn" type="submit">Login</button>
        )}
      </form>
    </div>
  );
};

export default Login;
