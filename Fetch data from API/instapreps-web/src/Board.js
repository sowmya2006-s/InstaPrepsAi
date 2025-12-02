import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Board() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get("http://staging.instapreps.com/api/board")
      .then((res) => {
        setData(res.data);
      })
      .catch((err) => {
        console.error("API Error:", err);
      });
  }, []);

  return (
    <div>
      <h1>Board Data</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
