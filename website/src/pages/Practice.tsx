import Header from "../components/Header"
import MicIcon from '@mui/icons-material/Mic';
import StopCircleOutlinedIcon from '@mui/icons-material/StopCircleOutlined';
import { useEffect, useState } from "react";
import API from "../helpers/API";
import confetti from 'canvas-confetti';
import { Box, CircularProgress, Modal } from "@mui/material";

export default function Practice({ setLoggedIn }: { setLoggedIn: (value: boolean) => void }) {
  const [recording, setRecording] = useState(false);
  const [stream, setStream] = useState<MediaStream | null>(null);

  const [word, setWord] = useState("");
  const [audio, setAudio] = useState<HTMLAudioElement | null>(null);
  const [loadingModal, setLoadingModal] = useState(false);

  useEffect(() => {
    (async () => {
      const wordData = await API.getWord();
      setWord(wordData.word);
      setAudio(new Audio(wordData.audioURL));
    })();
  }, []);

  function startRecording() {
    console.log("=recording started");
    navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
      const audioChunks: Blob[] = [];

      const mediaRecorder = new MediaRecorder(stream);

      mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
      };

      mediaRecorder.start();

      setRecording(true);
      setStream(stream);

      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
        sendAudio(audioBlob);
      };
    });
  };

  function stopRecording() {
    stream!.getTracks().forEach((track) => track.stop());
    setRecording(false);
    console.log("recording stopped");
  };

  function switchListening() {
    if (recording) {
      stopRecording();
      console.log("Recording stopped");
    } else {
      startRecording();
      console.log("Recording started");
    }
  }

  async function sendAudio(blob: Blob) {
    console.log("Sending audio");

    const audioUrl = URL.createObjectURL(blob);
    const audio = new Audio(audioUrl);

    console.log("Playing audio");

    audio.play();
    console.log("Audio played");

    setLoadingModal(true);
    const response = await API.sendAudio(blob);
    setLoadingModal(false);

    if (response.good) {
      confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 }
      });
    }

    const wordData = await API.getWord();
    setWord(wordData.word);
    setAudio(new Audio(wordData.audioURL));
  }

  function sayWord() {
    audio!.play();
  }

  return (
    <div className="page">
      <Modal
        open={loadingModal}
        sx={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}
      >
        <Box sx={{ backgroundColor: '#000000', padding: '30px', borderRadius: '15px', userSelect: 'none' }}>
          <CircularProgress />
        </Box>
      </Modal>
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
        {recording ?
          (<StopCircleOutlinedIcon className="mic" style={{ fontSize: "100" }} />) :
          (<MicIcon className="stopMi" style={{ fontSize: "100" }} />)
        }
      </div>
    </div>
  )
}