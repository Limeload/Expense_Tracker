import React, { useEffect, useState } from "react";
import axios from "axios";

const App: React.FC = () => {
  const [user, setUser] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/api/user/1")
      .then(response => setUser(response.data))
      .catch(error => {
        console.error("Error fetching user:", error);
        setError("Failed to fetch user data");
      });
  }, []);

  return (
    <div>
      <h1>Flask + React + TypeScript</h1>
      {error ? (
        <p style={{ color: "red" }}>{error}</p>
      ) : user ? (
        <div>
          <h2>User Info</h2>
          <p><strong>ID:</strong> {user.id}</p>
          <p><strong>Username:</strong> {user.username}</p>
          <p><strong>Email:</strong> {user.email}</p>
        </div>
      ) : (
        <p>Loading user data...</p>
      )}
    </div>
  );
};

export default App;
