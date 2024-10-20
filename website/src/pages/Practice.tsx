import Header from "../components/Header"
import MicIcon from '@mui/icons-material/Mic';
import StopCircleOutlinedIcon from '@mui/icons-material/StopCircleOutlined';
import { useEffect, useState } from "react";
import API from "../helpers/API";
import { AudioRecorder, useAudioRecorder } from "react-audio-voice-recorder";
import confetti from 'canvas-confetti';

export default function Practice({ setLoggedIn }: { setLoggedIn: (value: boolean) => void }) {
  const [listening, setListening] = useState(false);
  const [word, setWord] = useState("bob");
  const [audio, setAudio] = useState<HTMLAudioElement | null>(null);

  const recorderControls = useAudioRecorder();

  useEffect(() => {
    (async () => {
      const wordData = await API.getWord();
      setWord(wordData.word);
      setAudio(new Audio(wordData.audioURL));
    })();
  }, []);

  function switchListening() {
    if (listening) {
      recorderControls.stopRecording();
      console.log("Recording stopped");
    } else {
      recorderControls.startRecording();
      console.log("Recording started");
    }
    setListening((oldListening) => !oldListening);
  }

  function sendAudio(blob: Blob) {
    // console.log("Sending audio");

    // const audioUrl = URL.createObjectURL(blob);
    // const audio = new Audio(audioUrl);

    // console.log("Playing audio");

    // audio.play();
    // console.log("Audio played");

    API.sendAudio(blob);
  }

  function sayWord() {
    confetti({
      particleCount: 100,
      spread: 70,
      origin: { y: 0.6 }
    });

    audio!.play();
  }

  return (
    <div className="page">
      <Header setLoggedIn={setLoggedIn} />

      <div className="fill" />

      <p className="say">Say</p>
      {word === "" ? <p>Loading...</p> : (
        <div className="wordToSayBox">
          <div className="wordToSayBox2" onClick={() => sayWord()}>
            <h1 className="wordToSay">{word}</h1>
          </div>
        </div>
      )}

      <div className="fill" />

      <div onClick={() => {
        switchListening();
      }}>
        {listening ?
          (<StopCircleOutlinedIcon className="mic" style={{ fontSize: "100" }} />) :
          (<MicIcon className="stopMi" style={{ fontSize: "100" }} />)
        }
      </div>
      <div className="hidden">
        <AudioRecorder
          onRecordingComplete={sendAudio}
          audioTrackConstraints={{
            noiseSuppression: true,
            echoCancellation: true,
          }}
          recorderControls={recorderControls}
        />
      </div>
    </div>
  )
}