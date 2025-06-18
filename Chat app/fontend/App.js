import React, { useState } from "react";
import ChatRoom from "./components/ChatRoom";
import "./style.css";


function App() {
  const [username, setUsername] = useState("");
  const [chatReady, setChatReady] = useState(false);

  const handleJoin = () => {
    if (username.trim() !== "") setChatReady(true);
  };

  return (
    <div className="App">
      {!chatReady ? (
        <div>
          <h2>Enter Username</h2>
          <input
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <button onClick={handleJoin}>Join Chat</button>
        </div>
      ) : (
        <ChatRoom username={username} />
      )}
    </div>
  );
}

export default App;
