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
      <h1>Sexy Statistics</h1>
      <p>Your child is dumb </p>
    </div>
  ) : (
    <div className="page">
      <h1 className="center">Please log in!</h1>
    </div>
  );
}