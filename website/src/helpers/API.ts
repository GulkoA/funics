import { word_response } from "../types/api_types";

export default class API {
  static async getWord(): Promise<word_response> {
    const response = await fetch("/api/get-word");
    return await response.json();
  }

  static async sendAudio(blob: Blob) {
    const audioFile = new File([blob], "audio-file.webm", { type: "audio/webm" });
    console.log("Audio File:", audioFile);  // Log file details
  
    const formData = new FormData();
    formData.append("audio", audioFile, "audio-file.webm");
  
    const response = await fetch("/api/submit-audio", {
      method: "POST",
      body: formData,
    });
  
    return await response.json();
  }

  static async getStats() {}
}
