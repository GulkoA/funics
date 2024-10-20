import Header from "../components/Header"
import MicIcon from '@mui/icons-material/Mic';
import StopCircleOutlinedIcon from '@mui/icons-material/StopCircleOutlined';
import { useEffect, useState } from "react";
import API from "../helpers/API";

export default function Practice({ setLoggedIn }: { setLoggedIn: (value: boolean) => void }) {
  const [listening, setListening] = useState(false);
  const [word, setWord] = useState("");

  useEffect(() => {
    (async () => {
      setWord((await API.get_word()).word);
    })();
  }, []);

  function switchListening() {
    setListening((oldListening) => !oldListening);
  }

  return (
    <div className="page">
      <Header setLoggedIn={setLoggedIn} />
      <p className="say">Say</p>
      <div className="wordToSayBox">
        <div className="wordToSayBox2">
          <h1 className="wordToSay">{word}</h1>
        </div>
      </div>

      <div className="fill" />

      <div onClick={() => {
        switchListening();
      }}>
        {listening ?
          (<StopCircleOutlinedIcon className="mic" style={{ fontSize: "100" }} />) :
          (<MicIcon className="stopMi" style={{ fontSize: "100" }} />)
        }
      </div>
    </div>
  )
}