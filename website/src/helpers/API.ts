import { word_response } from "../types/api_types";

export default class API {
  static async getWord(): Promise<word_response> {
    const response = await fetch("http://127.0.0.1:5000/api/get-word");
    return await response.json();
  }

  static async sendAudio(blob: Blob) {
    const audioFile = new File([blob], "audio-file.mp3", {
      type: "audio/mp3",
    });

    const formData = new FormData();
    formData.append("audio", audioFile, "audio-file.mp3");

    const response = await fetch("http://127.0.0.1:5000/api/submit-audio", {
      method: "POST",
      body: formData,
    });

    return await response.json();
  }

  static async getStats() {}
}
