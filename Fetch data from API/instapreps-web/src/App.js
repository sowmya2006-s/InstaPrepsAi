import React, { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get("http://staging.instapreps.com/api/board")
      .then((res) => {
        console.log("API Response:", res.data);
        setData(res.data);
      })
      .catch((err) => {
        console.error("API Error:", err);
      });
  }, []);

  return (
    <div className="App">
      <h1>Board Data</h1>

      {/* Display Data */}
      <pre style={{ textAlign: "left", padding: "20px" }}>
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
}

export default App;
