import Header from "../components/Header";

export default function Stats({ loggedIn }:
  {
    loggedIn: boolean;
    // setLoggedIn: React.SetStateAction<boolean>;
  }) {
  if (!loggedIn) {

    return (
      <div className="page">
        <h1 className="center">Please log in!</h1>
      </div>
    );
  }

  return (
    <div className="page">
      <Header />
      <h1>About</h1>
    </div>
  )
}