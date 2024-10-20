import { useNavigate } from "react-router-dom";
import Header from "../components/Header";
import { useEffect } from "react";

export default function Stats({ loggedIn, setLoggedIn }:
  {
    loggedIn: boolean;
    setLoggedIn: (value: boolean) => void;
  }) {
  const navigate = useNavigate();

  useEffect(() => {
    if (!loggedIn) {
      const password = window.prompt("Please enter some text:");

      if (password === "thisisthepassword") {
        setLoggedIn(true);
      } else {
        navigate('/');
      }
    }
  }, [loggedIn, navigate, setLoggedIn]);

  return loggedIn ? (
    <div className="page">
      <Header setLoggedIn={setLoggedIn} />
      <div>
        <h1>Statistics</h1>
        <p>Your child struggles with the following Phonemes: </p>
      </div>
    </div>
  ) : (
    <div className="page">
      <h1 className="center">Please log in!</h1>
    </div>
  );
}