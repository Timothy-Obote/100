import React from "react";

const Message = ({ text, sender }) => {
  const className = sender === "me" ? "message me" : "message other";
  return <div className={className}>{text}</div>;
};

export default Message;
